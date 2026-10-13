// Builds an editable PPTX from slides.json (1 px of the HTML slide = 1 pt, same page size as the source deck).
const fs = require('fs');
const pptxgen = require('pptxgenjs');
const React = require('react');
const RDS = require('react-dom/server');
const fa = require('react-icons/fa6');
const sharp = require('sharp');

const [jsonPath, outPath] = process.argv.slice(2);
const slides = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
const P = v => v / 72;
const FONT = { 300: ['Montserrat Light', false], 400: ['Montserrat', false], 500: ['Montserrat Medium', false],
  600: ['Montserrat SemiBold', false], 700: ['Montserrat', true], 800: ['Montserrat ExtraBold', false] };
const TITLES = { s07: 'Иқтидорли ёшларни қўллаб-қувватлаш', s08: 'Лойиҳа офиси, халқаро ҳамкорлик ва ижро' };

const iconCache = new Map();
async function iconPng(name, reg, color) {
  const key = name + reg + color;
  if (iconCache.has(key)) return iconCache.get(key);
  const pascal = name.replace(/^fa-/, '').split('-').map(s => s[0].toUpperCase() + s.slice(1)).join('');
  const Comp = fa[(reg ? 'FaReg' : 'Fa') + pascal] || fa['Fa' + pascal];
  if (!Comp) throw new Error('icon missing: ' + name);
  const svg = RDS.renderToStaticMarkup(React.createElement(Comp, { color: '#' + color, size: 512 }));
  const vb = svg.match(/viewBox="([^"]+)"/)[1].split(/\s+/).map(Number);
  const buf = await sharp(Buffer.from(svg), { density: 300 }).resize({ height: 384 }).png().toBuffer();
  const v = { data: 'image/png;base64,' + buf.toString('base64'), aspect: vb[2] / vb[3] };
  iconCache.set(key, v);
  return v;
}

(async () => {
  const pres = new pptxgen();
  pres.defineLayout({ name: 'DECK', width: P(1526), height: P(860) });
  pres.layout = 'DECK';
  pres.theme = { headFontFace: 'Montserrat', bodyFontFace: 'Montserrat' };
  pres.title = 'Таълим соҳасида СИ — слайдлар 07–08';

  for (const s of slides) {
    const sl = pres.addSlide();
    sl.background = { color: 'FFFFFF' };
    let n = 0;
    const nm = t => `${t}-${++n}`;
    const items = s.items;
    for (let i = 0; i < items.length; i++) {
      const it = items[i];
      if (it.t === 'box') {
        const cls = it.cls || '';
        const fill = it.fill ? { color: it.fill } : { type: 'none' };
        const line = it.line ? { color: it.line.color, width: it.line.w * 0.75 } : { type: 'none' };
        const base = { x: P(it.x), y: P(it.y), w: P(it.w), h: P(it.h), fill, line };
        if (/\bgl\b/.test(cls)) { // goal bar left: arrow-shaped block, with a white chevron gap after it
          const j = items.findIndex((x, k) => k > i && x.t === 'box' && /\bgr\b/.test(x.cls || '') && x.clip);
          if (j > 0) { const g = items[j]; g.done = true;
            sl.addShape(pres.shapes.RECTANGLE, { x: P(g.x), y: P(g.y), w: P(g.w), h: P(g.h), fill: { color: g.fill }, line: { type: 'none' }, objectName: nm('goal') }); }
          sl.addShape('homePlate', { ...base, x: P(it.x), w: P(it.w + 12), fill: { color: 'FFFFFF' }, line: { type: 'none' }, objectName: nm('gap') });
          sl.addShape('homePlate', { ...base, objectName: nm('goal') });
          continue;
        }
        if (it.done) continue;
        if (cls === 'n') { // annex number tab: rounded on the left only
          sl.addShape(pres.shapes.ROUNDED_RECTANGLE, { ...base, rectRadius: P(10), objectName: nm('tab') });
          sl.addShape(pres.shapes.RECTANGLE, { ...base, x: P(it.x + it.w / 2), w: P(it.w / 2), objectName: nm('tab') });
          continue;
        }
        const [tl, tr, br, bl] = it.rad;
        if (tl > 0 && br > 0 && tr === 0 && bl === 0) {
          sl.addShape('round2DiagRect', { ...base, objectName: nm('badge') });
        } else if (tl > 0) {
          sl.addShape(pres.shapes.ROUNDED_RECTANGLE, { ...base, rectRadius: P(Math.min(tl, it.h / 2, it.w / 2)), objectName: nm('box') });
        } else {
          sl.addShape(pres.shapes.RECTANGLE, { ...base, objectName: nm('box') });
        }
      } else if (it.t === 'path') {
        for (let k = 1; k < it.pts.length; k++) {
          const [a, b] = [it.pts[k - 1], it.pts[k]];
          sl.addShape(pres.shapes.LINE, { x: P(Math.min(a[0], b[0])), y: P(Math.min(a[1], b[1])), w: P(Math.abs(b[0] - a[0])), h: P(Math.abs(b[1] - a[1])),
            line: { color: it.color, width: 1.5 }, objectName: nm('connector') });
        }
      } else if (it.t === 'icon') {
        const ic = await iconPng(it.name, it.reg, it.color);
        const h = it.size, w = h * ic.aspect;
        sl.addImage({ data: ic.data, x: P(it.x + (it.w - w) / 2), y: P(it.y + (it.h - h) / 2), w: P(w), h: P(h), altText: it.name.replace('fa-', '') + ' icon', objectName: nm('icon') });
      } else if (it.t === 'donut') {
        const d = it.w * 136 / 150, ox = it.x + (it.w - d) / 2, oy = it.y + (it.h - d) / 2;
        for (const [c, ang] of [['026DD1', [270, 90]], ['05BAB6', [90, 270]]])
          sl.addShape(pres.shapes.BLOCK_ARC, { x: P(ox), y: P(oy), w: P(d), h: P(d), fill: { color: c }, line: { color: 'FFFFFF', width: 0.75 },
            angleRange: ang, arcThicknessRatio: 16 / 68, objectName: nm('donut') });
      } else if (it.t === 'text') {
        const runs = [];
        it.lines.forEach((l, li) => {
          l.forEach((r, ri) => {
            const [face, bold] = FONT[r.weight] || FONT[400];
            const o = { fontFace: face, bold, fontSize: r.size, color: r.color };
            if (ri === l.length - 1 && li < it.lines.length - 1) o.breakLine = true;
            runs.push({ text: r.text, options: o });
          });
          if (!l.length && li < it.lines.length - 1) runs.push({ text: '', options: { breakLine: true } });
        });
        if (!runs.length) continue;
        const single = it.h < it.lh * 1.5;
        const w = it.w * (single ? 1.08 : 1.035) + 6;
        let x = it.x;
        if (it.align === 'center') x -= (w - it.w) / 2;
        else if (it.align === 'right') x -= (w - it.w);
        sl.addText(runs, { x: P(x), y: P(it.y), w: P(w), h: P(it.h + it.lh * 0.25), margin: 0, valign: 'top',
          align: it.align === 'justify' ? 'left' : it.align, lineSpacing: it.lh, wrap: !single, fit: 'none',
          isTextBox: true, objectName: nm('text') });
      }
    }
    sl.addNotes(TITLES[s.id] || '');
  }
  await pres.writeFile({ fileName: outPath });
  console.log('wrote', outPath);
})();
