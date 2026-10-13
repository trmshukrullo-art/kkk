// Walks the rendered slides and dumps boxes, text blocks and icons (px, slide-relative) to JSON.
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
(async () => {
  const [html, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1526, height: 860 } });
  await p.route(/fonts\.googleapis\.com/, r => r.abort());
  await p.goto('file://' + html + '#export', { waitUntil: 'networkidle' });
  for (const w of [300, 400, 500, 600, 700, 800])
    await p.addStyleTag({ url: 'https://cdn.jsdelivr.net/npm/@fontsource/montserrat@5.0.18/' + w + '.css' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);

  const data = await p.evaluate(() => {
    const rgb = s => {
      const m = s && s.match(/rgba?\(([^)]+)\)/);
      if (!m) return null;
      const v = m[1].split(',').map(x => parseFloat(x));
      if (v.length === 4 && v[3] === 0) return null;
      return v.slice(0, 3).map(n => Math.round(n).toString(16).padStart(2, '0')).join('').toUpperCase();
    };
    const mix = img => { // average the colour stops of a linear-gradient
      const cs = [...img.matchAll(/rgba?\([^)]+\)/g)].map(m => rgb(m[0])).filter(Boolean);
      if (!cs.length) return null;
      const avg = [0, 2, 4].map(i => Math.round(cs.reduce((a, c) => a + parseInt(c.substr(i, 2), 16), 0) / cs.length));
      return avg.map(n => n.toString(16).padStart(2, '0')).join('').toUpperCase();
    };
    const slides = [];
    for (const sl of document.querySelectorAll('.slide')) {
      const o = sl.getBoundingClientRect();
      const R = r => ({ x: r.left - o.left, y: r.top - o.top, w: r.width, h: r.height });
      const items = [];
      const isTextBlock = el => [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
      const walk = (el, inText) => {
        const cs = getComputedStyle(el);
        if (cs.display === 'none') return;
        const r = el.getBoundingClientRect();
        if (el.tagName === 'I') {
          const cls = [...el.classList];
          const name = cls.find(c => c.startsWith('fa-') && c !== 'fa-solid' && c !== 'fa-regular');
          const ib = el.getBoundingClientRect();
          items.push({ t: 'icon', name, reg: cls.includes('fa-regular'), color: rgb(cs.color), size: parseFloat(cs.fontSize), ...R(ib) });
          return;
        }
        if (el.tagName === 'svg') { items.push({ t: 'donut', ...R(r) }); return; }
        if (!inText) {
          let fill = rgb(cs.backgroundColor);
          if (!fill && cs.backgroundImage.includes('gradient') && cs.backgroundClip !== 'text' && cs.webkitBackgroundClip !== 'text') fill = mix(cs.backgroundImage);
          const bw = parseFloat(cs.borderTopWidth);
          const line = bw > 0 && cs.borderTopStyle !== 'none' ? { w: bw, color: rgb(cs.borderTopColor) } : null;
          const rad = [cs.borderTopLeftRadius, cs.borderTopRightRadius, cs.borderBottomRightRadius, cs.borderBottomLeftRadius].map(parseFloat);
          if ((fill || line) && el !== sl)
            items.push({ t: 'box', fill, line, rad, cls: el.className, clip: cs.clipPath !== 'none', ...R(r) });
          if (el.classList.contains('leaf')) {
            const c = el.classList.contains('t') ? '27A9AE' : '2E7BD8';
            const x0 = r.left - o.left + 8, w0 = r.width - 16, y0 = r.top - o.top;
            items.push({ t: 'box', fill: c, rad: [2, 2, 2, 2], x: x0, y: y0, w: w0 * .22, h: 4 });
            items.push({ t: 'box', fill: c, rad: [2, 2, 2, 2], x: x0 + w0 * .78, y: y0, w: w0 * .22, h: 4 });
            items.push({ t: 'box', fill: c, rad: [2, 2, 2, 2], x: x0, y: y0 + r.height - 4, w: w0, h: 4 });
          }
          if (el.classList.contains('branch')) {
            const x = r.left - o.left, y = r.top - o.top, w = r.width;
            items.push({ t: 'path', color: 'B9D3EC', pts: [[x + w / 2, y], [x + w / 2, y + r.height]] });
            items.push({ t: 'path', color: 'B9D3EC', pts: [[x + w * .1666, y + r.height], [x + w * .1666, y + 12], [x + w * .8334, y + 12], [x + w * .8334, y + r.height]] });
          }
        }
        if (!inText && isTextBlock(el)) {
          const runs = [];
          const add = (node, parentEl) => {
            if (node.nodeType === 3) {
              const ps = getComputedStyle(parentEl);
              let txt = node.textContent.replace(/\s+/g, ' ');
              if (ps.textTransform === 'uppercase') txt = txt.toUpperCase();
              let color = rgb(ps.color);
              if (!color) color = '1E7CC0'; // gradient-clipped heading text
              runs.push({ text: txt, size: parseFloat(ps.fontSize), weight: parseInt(ps.fontWeight), color });
            } else if (node.nodeType === 1) {
              if (node.tagName === 'BR') { runs.push({ br: true }); return; }
              if (node.tagName === 'I') { walk(node, true); return; }
              for (const c of node.childNodes) add(c, node);
            }
          };
          for (const c of el.childNodes) add(c, el);
          // trim leading/trailing spaces per line
          const lines = [[]];
          runs.forEach(r => r.br ? lines.push([]) : lines[lines.length - 1].push(r));
          lines.forEach(l => {
            while (l.length && !l[0].text.trim()) l.shift();
            while (l.length && !l[l.length - 1].text.trim()) l.pop();
            if (l.length) { l[0].text = l[0].text.replace(/^ /, ''); l[l.length - 1].text = l[l.length - 1].text.replace(/ $/, ''); }
          });
          // tight rect of the text itself (excludes icons sharing the element)
          const rg = document.createRange();
          const kids = [...el.childNodes].filter(n => !(n.nodeType === 1 && n.tagName === 'I') && !(n.nodeType === 3 && !n.textContent.trim()));
          rg.setStartBefore(kids[0]); rg.setEndAfter(kids[kids.length - 1]);
          const tr = rg.getBoundingClientRect();
          const lh = cs.lineHeight === 'normal' ? parseFloat(cs.fontSize) * 1.22 : parseFloat(cs.lineHeight);
          items.push({ t: 'text', lines, align: cs.textAlign === 'start' ? 'left' : cs.textAlign, lh, ...R(tr) });
          for (const c of el.children) if (c.tagName === 'I') { /* handled in add */ }
          return;
        }
        for (const c of el.children) walk(c, inText);
      };
      walk(sl, false);
      slides.push({ id: sl.id, items });
    }
    return slides;
  });
  fs.writeFileSync(out, JSON.stringify(data, null, 1));
  console.log(data.map(s => s.id + ': ' + s.items.length + ' items').join('\n'));
  await b.close();
})();
