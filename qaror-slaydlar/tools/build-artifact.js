// Turns the slide HTML into one self-contained, self-saving artifact page (icons inlined as SVG).
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const path = require('path');
const React = require('react');
const RDS = require('react-dom/server');
const fa = require('react-icons/fa6');

const [src, out, cssPath] = process.argv.slice(2);
const RESET = ':root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000}img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}';

function svgFor(cls) {
  const name = cls.split(/\s+/).find(c => c.startsWith('fa-') && c !== 'fa-solid' && c !== 'fa-regular');
  const reg = /\bfa-regular\b/.test(cls);
  const P = name.replace(/^fa-/, '').split('-').map(s => s[0].toUpperCase() + s.slice(1)).join('');
  const C = fa[(reg ? 'FaReg' : 'Fa') + P] || fa['Fa' + P];
  if (!C) throw new Error('icon ' + name);
  return RDS.renderToStaticMarkup(React.createElement(C, { 'aria-hidden': 'true' }))
    .replace(/ (height|width)="1em"/g, '').replace(/ style="[^"]*"/, '');
}

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1526, height: 860 } });
  await p.route(/fonts\.googleapis\.com|cdnjs/, r => r.abort());
  await p.goto('file://' + src + '#export');
  const slides = await p.evaluate(() => {
    // wrap the text of blocks that also hold an icon, so editing never touches the icon
    document.querySelectorAll('.slide *').forEach(el => {
      const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
      const hasIcon = [...el.children].some(c => c.tagName === 'I');
      if (hasText && hasIcon) {
        const span = document.createElement('span');
        const nodes = [...el.childNodes].filter(n => !(n.nodeType === 1 && n.tagName === 'I'));
        const firstText = nodes.find(n => n.nodeType === 3 && n.textContent.trim() || n.nodeType === 1);
        el.insertBefore(span, firstText);
        nodes.forEach(n => span.appendChild(n));
      }
    });
    return [...document.querySelectorAll('.slide')].map(s => ({ id: s.id, html: s.outerHTML.replace(/ style="transform:[^"]*"/, '') }));
  });
  await b.close();

  for (const s of slides) {
    s.html = s.html.replace(/<i class="([^"]+)"([^>]*)><\/i>/g, (m, cls, rest) => `<i class="${cls}"${rest}>${svgFor(cls)}</i>`)
      .replace(/\s{2,}/g, ' ');
  }

  const slideCss = fs.readFileSync(cssPath, 'utf8').replace(/<\/?style>/g, '');
  const pageCss = `
/* Sahifa: yopishqoq asboblar paneli, ostida slaydlar ustma-ust; slayd 1526×860 kenglikka moslab kichraytiriladi. */
:root{--page:#E9EEF5;--page-ink:#17254A;--muted:#5E6B7D;--edit:#E0920F;--edit-bg:rgba(224,146,15,.08)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--page:#0E1626;--page-ink:#DCE6F5;--muted:#9AA9BF;--edit:#F2B24A;--edit-bg:rgba(242,178,74,.12);color-scheme:dark}}
:root[data-theme="dark"]{--page:#0E1626;--page-ink:#DCE6F5;--muted:#9AA9BF;--edit:#F2B24A;--edit-bg:rgba(242,178,74,.12);color-scheme:dark}
body{background:var(--page);color:var(--page-ink);font-family:'Montserrat',system-ui,sans-serif}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:41;background:#17254A}
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:40;background:#17254A;color:#fff;border-bottom:3px solid #2FC1FF;padding-block:10px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.bar-in{max-width:1526px;margin:0 auto;display:flex;flex-wrap:wrap;align-items:center;gap:10px 16px}
.bar h1{margin:0;font-size:15px;font-weight:700;letter-spacing:.02em;min-width:0}
.bar .st{font-size:12px;color:#A9C4E4;font-weight:500;min-width:0}
.tools{display:flex;flex-wrap:wrap;gap:8px;margin-left:auto}
.tb{font:600 12.5px 'Montserrat',system-ui,sans-serif;border-radius:7px;padding:7px 13px;cursor:pointer;border:1px solid rgba(255,255,255,.25);background:rgba(255,255,255,.08);color:#fff}
.tb:hover{background:rgba(255,255,255,.16)}
.tb:focus-visible{outline:2px solid #2FC1FF;outline-offset:2px}
.tb[aria-pressed="true"]{background:#2FC1FF;border-color:#2FC1FF;color:#0B1D33}
.tb.pri{background:#2FC1FF;border-color:#2FC1FF;color:#0B1D33}
.tb:disabled{opacity:.45;cursor:default}
.tb.sm{padding:5px 11px;font-size:12px;border-color:var(--muted);background:transparent;color:var(--page-ink)}
.tb.sm:hover{background:rgba(127,140,160,.15)}
.help{max-width:1526px;margin:12px auto 0;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));font-size:12.5px;color:var(--muted);line-height:1.5}
#slides{max-width:1526px;margin:0 auto;padding-block:4px 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.sw{margin-top:18px}
.cap{display:flex;align-items:center;justify-content:space-between;gap:12px;margin:0 0 8px;font-weight:700;font-size:13px;letter-spacing:.02em}
.cap span{min-width:0}
.stage{width:100%;overflow:hidden;border-radius:6px;box-shadow:0 2px 16px rgba(10,30,60,.18);background:#fff}
i[class*="fa-"]{font-style:normal;display:inline-block;line-height:1}
i[class*="fa-"] svg{height:1em;width:auto;display:inline-block;vertical-align:-.125em;fill:currentColor}
body.editing [data-k]{outline:1px dashed transparent;outline-offset:2px;border-radius:3px;cursor:text}
body.editing [data-k]:hover{outline-color:var(--edit)}
body.editing [data-k]:focus{outline:2px solid var(--edit);background:var(--edit-bg)}
body.export .bar,body.export .help,body.export .cap{display:none}
body.export #slides{padding:0;max-width:none}
body.export .sw{margin:0}
body.export .stage{border-radius:0;box-shadow:none;width:1526px}
@media (max-width:640px){.bar h1{font-size:13.5px}.cap{font-size:12px}}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
`;
  const css = slideCss.replace(/body\{margin:0;background:var\(--page\)[^}]*\}/, '').replace(/\.wrap\{[^}]*\}|\.cap\{[^}]*\}|\.stage\{[^}]*\}|body\.export[^{]*\{[^}]*\}/g, '') + pageCss;

  const pagehead = '<title>Қарор слайдлари 03–09</title><meta name="claude:viewport-fit-sides" content="cover">'
    + '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    + '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&display=swap">';
  const shell = '<header class="bar"><div class="bar-in"><h1>Таълимда СИ · қарор слайдлари 03–09</h1><span class="st" id="status" role="status"></span>'
    + '<div class="tools"><button type="button" class="tb" id="bCancel" hidden>Бекор қилиш</button>'
    + '<button type="button" class="tb" id="bEdit" aria-pressed="false">Таҳрирлаш</button>'
    + '<button type="button" class="tb pri" id="bSave" disabled>Сақлаш</button></div></div></header>'
    + '<p class="help">Матнни ўзгартириш: <b>Таҳрирлаш</b> → керакли ёзувни босиб ёзинг → <b>Сақлаш</b>. Изоҳ: слайд устидаги <b>Изоҳ қолдириш</b> тугмаси ёки изоҳ режимида керакли жойни белгиланг — Claude’га юборилган изоҳлар бўйича тузатиш киритилади.</p>'
    + '<main id="slides"></main>';
  const app = fs.readFileSync(path.join(__dirname, 'app.js'), 'utf8');
  const json = JSON.stringify({ slides }).replace(/<\//g, '<\\/');
  const content = pagehead
    + '<style id="st">' + css + '</style>'
    + shell
    + '<script type="application/json" id="deck">' + json + '</script>'
    + '<script type="text/plain" id="reset">' + RESET + '</script>'
    + '<script type="text/plain" id="pagehead">' + pagehead.replace(/<\//g, '<\\/') + '</script>'
    + '<script type="text/plain" id="shell">' + shell.replace(/<\//g, '<\\/') + '</script>'
    + '<script id="app">' + app + '</script>';
  fs.writeFileSync(out, content);
  console.log('wrote', out, (content.length / 1024).toFixed(0) + ' KB', slides.length + ' slides');
})();
