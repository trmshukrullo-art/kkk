// HTML → Figma Import — main (sandbox) side.
// The UI renders the HTML in an iframe, measures every element and sends a
// tree of absolutely-positioned nodes here; we turn it into Figma layers.

figma.showUI(__html__, { width: 380, height: 540, themeColors: true });

const FALLBACK_FAMILY = 'Inter';
const GENERIC = /^(serif|sans-serif|monospace|cursive|fantasy|system-ui|ui-sans-serif|ui-serif|ui-monospace|-apple-system|blinkmacsystemfont)$/i;

let fontIndex = null; // lower-cased family -> { family, styles: [{ style, weight, italic }] }
const fontCache = new Map();
const missingFonts = new Set();

function styleWeight(style) {
  const s = style.toLowerCase().replace(/[\s_-]/g, '');
  if (/thin|hairline/.test(s)) return 100;
  if (/(extra|ultra)light/.test(s)) return 200;
  if (/light/.test(s)) return 300;
  if (/(semi|demi)bold/.test(s)) return 600;
  if (/(extra|ultra)bold/.test(s)) return 800;
  if (/black|heavy/.test(s)) return 900;
  if (/bold/.test(s)) return 700;
  if (/medium/.test(s)) return 500;
  return 400;
}

async function getFontIndex() {
  if (fontIndex) return fontIndex;
  fontIndex = new Map();
  for (const f of await figma.listAvailableFontsAsync()) {
    const key = f.fontName.family.toLowerCase();
    if (!fontIndex.has(key)) fontIndex.set(key, { family: f.fontName.family, styles: [] });
    fontIndex.get(key).styles.push({
      style: f.fontName.style,
      weight: styleWeight(f.fontName.style),
      italic: /italic|oblique/i.test(f.fontName.style),
    });
  }
  return fontIndex;
}

function resolveFont(familyList, weight, italic) {
  const cacheKey = familyList + '|' + weight + '|' + italic;
  if (fontCache.has(cacheKey)) return fontCache.get(cacheKey);
  const names = familyList.split(',').map((s) => s.trim().replace(/^["']|["']$/g, '')).filter(Boolean);
  let entry = null;
  for (const n of names) {
    if (GENERIC.test(n)) continue;
    entry = fontIndex.get(n.toLowerCase());
    if (entry) break;
  }
  if (!entry) {
    const wanted = names.find((n) => !GENERIC.test(n));
    if (wanted) missingFonts.add(wanted);
    entry = fontIndex.get(FALLBACK_FAMILY.toLowerCase()) || fontIndex.values().next().value;
  }
  let best = null, bestScore = Infinity;
  for (const s of entry.styles) {
    const score = Math.abs(s.weight - weight) + (s.italic === italic ? 0 : 1000);
    if (score < bestScore) { best = s; bestScore = score; }
  }
  const font = { family: entry.family, style: best.style };
  fontCache.set(cacheKey, font);
  return font;
}

function collectFonts(node, out) {
  if (node.type === 'TEXT') {
    for (const s of node.styles) out.add(JSON.stringify(resolveFont(s.family, s.weight, s.italic)));
  }
  if (node.children) for (const c of node.children) collectFonts(c, out);
}

// ---------- paints ----------
function rgb(c) { return { r: c.r, g: c.g, b: c.b }; }

function toPaint(p) {
  if (p.type === 'SOLID') return { type: 'SOLID', color: rgb(p.color), opacity: p.color.a };
  if (p.type === 'GRADIENT_LINEAR' || p.type === 'GRADIENT_RADIAL') {
    return {
      type: p.type,
      gradientTransform: p.transform,
      gradientStops: p.stops.map((s) => ({ position: s.position, color: { r: s.color.r, g: s.color.g, b: s.color.b, a: s.color.a } })),
    };
  }
  if (p.type === 'IMAGE') {
    if (!p.bytes) return null;
    try {
      return { type: 'IMAGE', imageHash: figma.createImage(p.bytes).hash, scaleMode: p.scaleMode || 'FILL' };
    } catch (e) {
      return null;
    }
  }
  return null;
}

function effectsOf(d) {
  const fx = [];
  for (const s of d.shadows || []) {
    fx.push({
      type: s.inset ? 'INNER_SHADOW' : 'DROP_SHADOW',
      color: { r: s.color.r, g: s.color.g, b: s.color.b, a: s.color.a },
      offset: { x: s.x, y: s.y },
      radius: s.blur,
      spread: s.spread,
      visible: true,
      blendMode: 'NORMAL',
    });
  }
  if (d.blur) fx.push({ type: 'LAYER_BLUR', radius: d.blur, visible: true });
  if (d.backgroundBlur) fx.push({ type: 'BACKGROUND_BLUR', radius: d.backgroundBlur, visible: true });
  return fx;
}

// ---------- builders ----------
let built = 0;

async function build(d, parent, px, py) {
  if (d.type === 'FRAME') return buildFrame(d, parent, px, py);
  // A single broken text/svg must not abort the whole import.
  try {
    return d.type === 'TEXT' ? buildText(d, parent, px, py) : buildSvg(d, parent, px, py);
  } catch (e) {
    console.warn('HTML import: skipped node', d.name, e);
    return null;
  }
}

async function buildFrame(d, parent, px, py) {
  const f = figma.createFrame();
  parent.appendChild(f);
  f.name = d.name || 'frame';
  f.resizeWithoutConstraints(Math.max(0.01, d.w), Math.max(0.01, d.h));
  f.x = d.x - px;
  f.y = d.y - py;
  f.fills = (d.fills || []).map(toPaint).filter(Boolean);
  f.clipsContent = !!d.clip;
  if (d.radii) {
    const [tl, tr, br, bl] = d.radii;
    if (tl === tr && tr === br && br === bl) f.cornerRadius = tl;
    else { f.topLeftRadius = tl; f.topRightRadius = tr; f.bottomRightRadius = br; f.bottomLeftRadius = bl; }
  }
  if (d.stroke) {
    f.strokes = [{ type: 'SOLID', color: rgb(d.stroke), opacity: d.stroke.a }];
    f.strokeAlign = d.strokeAlign || 'INSIDE';
    const [t, r, b, l] = d.strokeWeights;
    if (t === r && r === b && b === l) f.strokeWeight = t;
    else { f.strokeTopWeight = t; f.strokeRightWeight = r; f.strokeBottomWeight = b; f.strokeLeftWeight = l; }
    if (d.dashed) f.dashPattern = [Math.max(2, t || l) * 2, Math.max(2, t || l)];
  }
  const fx = effectsOf(d);
  if (fx.length) f.effects = fx;
  if (d.opacity != null && d.opacity < 1) f.opacity = d.opacity;
  if (++built % 200 === 0) figma.ui.postMessage({ type: 'progress', text: `… ${built} ta qatlam` });
  for (const c of d.children || []) await build(c, f, d.x, d.y);
  return f;
}

function buildSvg(d, parent, px, py) {
  let n;
  try {
    n = figma.createNodeFromSvg(d.svg);
  } catch (e) {
    n = figma.createRectangle();
    n.fills = [{ type: 'SOLID', color: { r: 0.9, g: 0.9, b: 0.9 } }];
    n.resize(Math.max(0.01, d.w), Math.max(0.01, d.h));
  }
  parent.appendChild(n);
  n.name = d.name || 'svg';
  if (Math.abs(n.width - d.w) > 0.5 || Math.abs(n.height - d.h) > 0.5) {
    if ('rescale' in n && n.width > 0) n.rescale(d.w / n.width);
  }
  n.x = d.x - px;
  n.y = d.y - py;
  if (d.opacity != null && d.opacity < 1) n.opacity = d.opacity;
  built++;
  return n;
}

const SLACK = 3;

function buildText(d, parent, px, py) {
  const fonts = d.styles.map((s) => resolveFont(s.family, s.weight, s.italic));
  const t = figma.createText();
  parent.appendChild(t);
  try {
    fillText(t, d, fonts, px, py);
  } catch (e) {
    t.remove();
    throw e;
  }
  return t;
}

function fillText(t, d, fonts, px, py) {
  t.fontName = fonts[d.segs[0].style];
  t.characters = d.characters;
  for (const seg of d.segs) {
    if (seg.end <= seg.start) continue;
    const s = d.styles[seg.style];
    t.setRangeFontName(seg.start, seg.end, fonts[seg.style]);
    t.setRangeFontSize(seg.start, seg.end, Math.max(1, s.size));
    t.setRangeFills(seg.start, seg.end, [{ type: 'SOLID', color: rgb(s.color), opacity: s.color.a }]);
    if (s.letterSpacing) t.setRangeLetterSpacing(seg.start, seg.end, { unit: 'PIXELS', value: s.letterSpacing });
    if (s.decoration !== 'NONE') t.setRangeTextDecoration(seg.start, seg.end, s.decoration);
    if (s.textCase !== 'ORIGINAL') t.setRangeTextCase(seg.start, seg.end, s.textCase);
  }
  t.lineHeight = d.lineHeight ? { unit: 'PIXELS', value: d.lineHeight } : { unit: 'AUTO' };
  t.textAlignHorizontal = d.align;
  if (d.name) t.name = d.name;

  let x = d.x;
  if (d.multiLine) {
    // Fixed width with a little slack so Figma's font metrics don't add extra wraps.
    const w = d.align === 'JUSTIFIED' ? d.w : d.w + SLACK;
    t.textAutoResize = 'HEIGHT';
    t.resize(w, t.height);
    if (d.align === 'CENTER') x -= SLACK / 2;
    else if (d.align === 'RIGHT') x -= SLACK;
  } else {
    t.textAutoResize = 'WIDTH_AND_HEIGHT';
    if (d.align === 'CENTER') x = d.x + d.w / 2 - t.width / 2;
    else if (d.align === 'RIGHT') x = d.x + d.w - t.width;
  }
  const firstLine = d.multiLine && d.lineHeight ? d.lineHeight : t.height;
  t.x = x - px;
  t.y = d.firstLineCenter - firstLine / 2 - py;
  if (d.opacity != null && d.opacity < 1) t.opacity = d.opacity;
  built++;
}

// ---------- messages ----------
function freeX() {
  let right = null;
  for (const n of figma.currentPage.children) right = Math.max(right == null ? -Infinity : right, n.x + n.width);
  return right == null ? 0 : Math.round(right + 200);
}

figma.ui.onmessage = async (msg) => {
  if (msg.type !== 'import') return;
  try {
    await getFontIndex();
    missingFonts.clear();
    const created = [];
    let x = freeX();
    for (const page of msg.pages) {
      const fonts = new Set([JSON.stringify({ family: FALLBACK_FAMILY, style: 'Regular' })]);
      collectFonts(page.tree, fonts);
      figma.ui.postMessage({ type: 'progress', text: `⏳ ${page.name}: ${fonts.size} ta shrift yuklanmoqda...` });
      await Promise.all([...fonts].map((f) => figma.loadFontAsync(JSON.parse(f)).catch(() => {})));

      built = 0;
      const root = await buildFrame(page.tree, figma.currentPage, 0, 0);
      root.name = page.name;
      root.x = x;
      root.y = 0;
      x += root.width + 200;
      created.push(root);
      figma.ui.postMessage({ type: 'progress', text: `✓ ${page.name}: ${built} ta qatlam` });
    }
    figma.currentPage.selection = created;
    figma.viewport.scrollAndZoomIntoView(created);
    figma.ui.postMessage({ type: 'done', pages: created.length, missingFonts: [...missingFonts] });
  } catch (e) {
    figma.ui.postMessage({ type: 'error', text: String(e && e.message || e) });
  }
};
