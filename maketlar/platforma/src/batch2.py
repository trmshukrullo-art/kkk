"""2-partiya: Test natijasi, Natijalarim, Mening kurslarim, Birinchi kirish."""
import os
from shell import page, ic, tools

OUT = os.path.join(os.path.dirname(__file__), "..")


def write(name, html):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(html)


def smooth(pts):
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d


def line_chart(W, H, labels, series, lo=40, hi=100, ticks=(40, 55, 70, 85, 100), focus=None, threshold=None):
    L, R, T, B = 40, 8, 8, 26
    pw, ph = W - L - R, H - T - B
    n = len(labels)
    X = lambda i: L + pw * i / (n - 1)
    Y = lambda v: T + ph * (1 - (v - lo) / (hi - lo))
    s = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" class="lc" role="img" aria-label="Ballar dinamikasi">', '<defs>']
    for k, (_, col, _) in enumerate(series):
        s.append(f'<linearGradient id="lg{k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{col}" stop-opacity=".14"/><stop offset="1" stop-color="{col}" stop-opacity="0"/></linearGradient>')
    s.append('</defs>')
    for v in ticks:
        y = Y(v)
        s.append(f'<line x1="{L}" x2="{W-R}" y1="{y:.1f}" y2="{y:.1f}" class="gl"/><text x="{L-10}" y="{y+4:.1f}" class="ax" text-anchor="end">{v}</text>')
    for i, m in enumerate(labels):
        x = X(i)
        s.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{T}" y2="{T+ph}" class="gl"/><text x="{x:.1f}" y="{H-6}" class="ax" text-anchor="middle">{m}</text>')
    if threshold:
        y = Y(threshold)
        s.append(f'<line x1="{L}" x2="{W-R}" y1="{y:.1f}" y2="{y:.1f}" stroke="#B4232F" stroke-opacity=".55" stroke-dasharray="5 4"/>'
                 f'<text x="{W-R-4}" y="{y-6:.1f}" text-anchor="end" style="font:600 10.5px Inter;fill:#B4232F">Oʻtish bali · {threshold}</text>')
    for k, (data, col, _) in reversed(list(enumerate(series))):
        pts = [(X(i), Y(v)) for i, v in enumerate(data)]
        d = smooth(pts)
        s.append(f'<path d="{d} L{X(n-1):.1f},{T+ph} L{L},{T+ph} Z" fill="url(#lg{k})"/>')
        s.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="1.7" stroke-dasharray="2.5 3" stroke-linecap="round"/>')
    tip = None
    if focus is not None:
        i, v = focus
        x, y = X(i), Y(v)
        s.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{y:.1f}" y2="{T+ph}" stroke="#2550C0" stroke-opacity=".35"/><circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="#fff" stroke="#2550C0" stroke-width="2"/>')
        tip = (x, y)
    s.append('</svg>')
    return "".join(s), tip


CHART_CSS = """
.lc .gl{stroke:var(--grid);stroke-dasharray:3 3}
.lc .ax{font:500 11px Inter;fill:var(--subtle)}
.cw{position:relative;padding:4px 20px 18px}
.tip{position:absolute;padding:8px 10px;border-radius:8px;background:rgba(11,26,63,.92);color:#fff;font-size:11.5px;line-height:1.35;box-shadow:0 8px 20px -6px rgba(0,0,0,.35);white-space:nowrap}
.tip span{color:rgba(255,255,255,.7)}
.tip b{display:block;font-size:13.5px;font-weight:700;margin-top:2px}
.leg{display:flex;gap:16px;font-size:11px;font-weight:600;letter-spacing:.07em;color:var(--muted)}
.leg span{display:inline-flex;align-items:center;gap:7px}
.leg i{width:9px;height:9px;border-radius:50%;box-shadow:inset 0 0 0 2.2px currentColor}
.per{display:inline-flex;align-items:center;gap:10px;height:34px;padding:0 10px;border-radius:9px;background:#fff;box-shadow:var(--sh);font-size:13px;font-weight:500;color:var(--ink)}
.per .ic{width:15px;height:15px;color:var(--muted)}
"""

# ---------------------------------------------------------------- 6. Test natijasi
css_result = """
.res{position:relative;overflow:hidden;padding:40px 32px 0;text-align:center}
.res:before{content:"";position:absolute;left:50%;top:-140px;width:640px;height:420px;margin-left:-320px;background:radial-gradient(closest-side,rgba(14,122,82,.16),rgba(14,122,82,.05) 60%,transparent);pointer-events:none}
.res>*{position:relative}
.okc{width:72px;height:72px;border-radius:50%;margin:0 auto;display:grid;place-items:center;background:#fff;box-shadow:0 0 0 10px rgba(14,122,82,.08),0 0 0 1px var(--green-100),0 10px 24px -8px rgba(14,122,82,.35);color:var(--green)}
.okc .ic{width:32px;height:32px;stroke-width:2.4}
.res h2{font-size:24px;letter-spacing:-.02em;color:var(--ink);margin:20px 0 6px}
.res p{color:var(--muted);font-size:14px}
.score{display:flex;align-items:baseline;justify-content:center;gap:8px;margin:22px 0 6px}
.score b{font-size:56px;line-height:1;font-weight:800;letter-spacing:-.04em;color:var(--ink);font-variant-numeric:tabular-nums}
.score span{font-size:18px;color:var(--subtle);font-weight:500}
.scale{max-width:520px;margin:34px auto 0;position:relative}
.scale .bar{height:10px}
.scale .bar i{background:linear-gradient(90deg,#0E7A52,#18A06B)}
.scale .th{position:absolute;left:60%;top:-6px;bottom:-6px;width:2px;background:var(--ink);border-radius:2px}
.scale .th span{position:absolute;bottom:100%;left:50%;transform:translateX(-50%);font-size:11.5px;font-weight:700;color:var(--ink);white-space:nowrap;margin-bottom:4px}
.scale .ends{display:flex;justify-content:space-between;font-size:11.5px;color:var(--subtle);margin-top:8px;font-variant-numeric:tabular-nums}
.rs{display:grid;grid-template-columns:repeat(4,1fr);margin:32px -32px 0;border-top:1px solid var(--line)}
.rs div{padding:16px 20px;text-align:left}
.rs div+div{border-left:1px solid var(--line)}
.rs b{display:block;font-size:22px;font-weight:700;letter-spacing:-.02em;color:var(--ink);margin-top:4px;font-variant-numeric:tabular-nums}
.rs b.g{color:var(--green)}.rs b.r{color:var(--red)}
.topic{padding:0 20px 18px;display:grid;gap:16px}
.tp-h{display:flex;align-items:center;gap:10px;font-size:13.5px;color:var(--ink);margin-bottom:8px}
.tp-h b{margin-left:auto;font-weight:700;font-variant-numeric:tabular-nums}
.tp-h small{font-size:12px;color:var(--muted)}
.tp .bar{height:8px}
.tp.am .bar i{background:var(--amber)}.tp.am .tp-h b{color:var(--amber)}
.tp.rd .bar i{background:var(--red)}.tp.rd .tp-h b{color:var(--red)}
.tp.gr .bar i{background:var(--green)}.tp.gr .tp-h b{color:var(--green)}
.rec{display:flex;gap:12px;align-items:center;padding:12px 20px;border-top:1px solid var(--line-2)}
.rec .ri{width:34px;height:34px;border-radius:9px;display:grid;place-items:center;flex:none;box-shadow:inset 0 0 0 1px var(--line);color:var(--muted)}
.rec .ri .ic{width:16px;height:16px}
.rec b{display:block;font-size:13.5px;font-weight:600;color:var(--ink)}
.rec span{font-size:12.5px;color:var(--muted)}
.rec .btn{margin-left:auto}
table{width:100%;border-collapse:collapse}
th{text-align:left;font-size:12.5px;font-weight:500;color:var(--muted);padding:10px 20px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:#FAFBFD;white-space:nowrap}
td{padding:0 20px;height:52px;border-bottom:1px solid var(--line-2);font-size:13.5px;color:var(--ink)}
tr:last-child td{border-bottom:0}
td.n{width:56px;color:var(--muted);font-variant-numeric:tabular-nums}
td.q{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ans{display:inline-grid;place-items:center;width:24px;height:24px;border-radius:6px;font-size:12px;font-weight:700;background:var(--bg);box-shadow:inset 0 0 0 1px var(--line);color:var(--muted)}
.ans.ok{background:var(--green-50);color:var(--green);box-shadow:inset 0 0 0 1px var(--green-100)}
.ans.no{background:var(--red-50);color:var(--red);box-shadow:inset 0 0 0 1px var(--red-100)}
.tfoot{display:flex;align-items:center;padding:12px 20px;border-top:1px solid var(--line);font-size:13px;color:var(--muted)}
"""

qrows = [
    (1, "HR menejmentining asosiy maqsadi nima?", "HR asoslari", "B", "B"),
    (4, "Mehnat shartnomasi qaysi shaklda tuziladi?", "Mehnat huquqi", "A", "A"),
    (9, "Sinov muddati eng koʻpi bilan qancha boʻlishi mumkin?", "Mehnat huquqi", "C", "B"),
    (13, "Kompetensiyalar modeli nima uchun kerak?", "Xodimlarni tanlash", "D", "A"),
    (17, "Herzberg nazariyasidagi gigiyena omillari qaysilar?", "Motivatsiya", "A", "C"),
    (21, "Nomzodning qaysi maʼlumotlari qarorga taʼsir qilmasligi kerak?", "Mehnat huquqi", "B", "B"),
]


def qrow(n, q, t, me, ok):
    good = me == ok
    st = '<span class="st green"><i></i>Toʻgʻri</span>' if good else '<span class="st red"><i></i>Xato</span>'
    return (f'<tr><td class="n">{n}</td><td class="q">{q}</td><td class="mut">{t}</td>'
            f'<td><span class="ans {"ok" if good else "no"}">{me}</span></td><td><span class="ans ok">{ok}</span></td><td>{st}</td></tr>')


result_body = f"""
<main class="ct two">
<div class="col">
  <section class="card res">
    <span class="okc">{ic("check")}</span>
    <h2>Tabriklaymiz, siz testdan oʻtdingiz!</h2>
    <p>Oraliq test (1-modul) · 16.10.2026, 14:52 da yakunlandi</p>
    <div class="score"><b>72</b><span>/ 100 ball</span></div>
    <span class="st green"><i></i>Oʻtdi · oʻtish bali 60</span>
    <div class="scale"><div class="bar"><i style="width:72%"></i></div><span class="th"><span>60</span></span><div class="ends"><span>0</span><span>100</span></div></div>
    <div class="rs">
      <div><span class="cap">Toʻgʻri javob</span><b class="g">18</b></div>
      <div><span class="cap">Xato javob</span><b class="r">7</b></div>
      <div><span class="cap">Sarflangan vaqt</span><b>18:47 <small style="font-size:13px;color:var(--subtle);font-weight:500">/ 20:00</small></b></div>
      <div><span class="cap">Urinish</span><b>1 <small style="font-size:13px;color:var(--subtle);font-weight:500">/ 2</small></b></div>
    </div>
  </section>

  <section class="card">
    <div class="ch"><h3>Savollar boʻyicha natija</h3><div class="seg ml"><span class="on">Barchasi <em>25</em></span><span>Toʻgʻri <em>18</em></span><span>Xato <em>7</em></span></div></div>
    <table style="table-layout:fixed"><thead><tr><th style="width:56px">№</th><th>Savol</th><th style="width:160px">Mavzu</th><th style="width:104px">Javobingiz</th><th style="width:112px">Toʻgʻri javob</th><th style="width:110px">Natija</th></tr></thead>
    <tbody>{"".join(qrow(*r) for r in qrows)}</tbody></table>
    <div class="tfoot">25 ta savoldan 6 tasi koʻrsatilgan<a class="btn b-sm b-white ml">Barcha savollar{ic("chevd")}</a></div>
  </section>
</div>

<aside class="col">
  <section class="card">
    <div class="ch"><h3>Mavzular boʻyicha tahlil</h3></div>
    <div class="topic">
      <div class="tp gr"><div class="tp-h">HR asoslari<small>7/8</small><b>88%</b></div><div class="bar"><i style="width:88%"></i></div></div>
      <div class="tp gr"><div class="tp-h">Mehnat huquqi<small>6/8</small><b>75%</b></div><div class="bar"><i style="width:75%"></i></div></div>
      <div class="tp am"><div class="tp-h">Xodimlarni tanlash<small>3/5</small><b>60%</b></div><div class="bar"><i style="width:60%"></i></div></div>
      <div class="tp rd"><div class="tp-h">Motivatsiya<small>2/4</small><b>50%</b></div><div class="bar"><i style="width:50%"></i></div></div>
    </div>
  </section>
  <section class="card">
    <div class="ch"><h3>Takrorlash uchun tavsiya</h3></div>
    <div class="rec"><span class="ri">{ic("video")}</span><div><b>Motivatsiya nazariyalari</b><span>1-modul, 4-dars · 14 daq</span></div><a class="btn b-sm b-white">Ochish</a></div>
    <div class="rec"><span class="ri">{ic("text")}</span><div><b>Kompetensiyalar modeli</b><span>1-modul, 3-dars · 8 daq</span></div><a class="btn b-sm b-white">Ochish</a></div>
  </section>
  <div class="alert a-blue">{ic("info")}<span>Natijani yaxshilash uchun testni <b>yana 1 marta</b> topshirishingiz mumkin. Eng yuqori ball hisobga olinadi.</span></div>
</aside>
</main>"""

result_hd = (f'<span class="bk">{ic("back")}</span><span class="crumb">Zamonaviy HR{ic("chevr")}Oraliq test (1-modul){ic("chevr")}<b>Natija</b></span>'
             f'<span class="ml"></span><a class="btn b-white">Qayta topshirish</a><a class="btn b-pri">Kursga qaytish{ic("arrow")}</a>')

# ---------------------------------------------------------------- 7. Natijalarim
css_results = CHART_CSS + """
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.kpi{padding:16px 18px 18px}
.kpi-h{display:flex;align-items:center;justify-content:space-between;font-size:13.5px;font-weight:500;color:var(--ink)}
.ki{width:30px;height:30px;border-radius:8px;display:grid;place-items:center;box-shadow:inset 0 0 0 1px var(--line);color:var(--muted)}
.ki .ic{width:16px;height:16px}
.kv{display:flex;align-items:center;gap:8px;margin-top:16px}
.kv b{font-size:30px;font-weight:700;letter-spacing:-.03em;color:var(--ink);line-height:1;font-variant-numeric:tabular-nums}
.kv small{font-size:14px;font-weight:500;color:var(--subtle)}
.kf{margin-top:10px;font-size:12.5px;color:var(--muted)}
.dl{display:inline-flex;align-items:center;gap:3px;height:22px;padding:0 7px;border-radius:6px;font-size:12px;font-weight:600;background:var(--green-50);color:var(--green)}
.dl .ic{width:12px;height:12px;stroke-width:2.2}
table{width:100%;border-collapse:collapse}
th{text-align:left;font-size:12.5px;font-weight:500;color:var(--muted);padding:10px 20px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:#FAFBFD}
td{padding:0 20px;height:54px;border-bottom:1px solid var(--line-2);font-size:13.5px;color:var(--ink)}
tr:last-child td{border-bottom:0}
td b{font-weight:600}
td small{display:block;font-size:12px;color:var(--muted)}
.sc{font-weight:700;font-variant-numeric:tabular-nums}
.cert{display:flex;gap:14px;align-items:center;padding:14px 20px;border-top:1px solid var(--line-2)}
.cert .cimg{width:56px;height:40px;border-radius:6px;background:linear-gradient(135deg,#FCF1E1,#fff);box-shadow:inset 0 0 0 1px var(--amber-100);display:grid;place-items:center;color:var(--amber);flex:none}
.cert .cimg .ic{width:18px;height:18px}
.cert b{display:block;font-size:13.5px;font-weight:600;color:var(--ink)}
.cert span{font-size:12.5px;color:var(--muted)}
.cert .acts{margin-left:auto;display:flex;gap:6px}
.icb{width:32px;height:32px;border-radius:8px;display:grid;place-items:center;color:var(--muted);box-shadow:var(--sh);background:#fff}
.icb .ic{width:15px;height:15px}
.cp{padding:0 20px 18px;display:grid;gap:14px}
.cp .pt{display:flex;justify-content:space-between;font-size:13px;color:var(--ink);margin-bottom:7px}
.cp .pt b{font-variant-numeric:tabular-nums}
"""

line_svg, tip = line_chart(1104, 240, ["Noy", "Dek", "Yan", "Fev", "Mar", "Apr", "May", "Iyn", "Iyl", "Avg", "Sen", "Okt"],
                           [([52, 58, 49, 61, 57, 66, 63, 72, 70, 81, 76, 84], "#2550C0", "Siz"),
                            ([55, 54, 57, 56, 60, 58, 62, 61, 64, 63, 66, 65], "#B7791F", "Guruh")],
                           focus=(9, 81), threshold=60)

tests = [
    ("Oraliq test (1-modul)", "Zamonaviy HR", "16.10.2026", 72, True),
    ("Kirish testi", "Zamonaviy HR", "02.09.2026", 64, True),
    ("Yakuniy test", "Mustaqil taʼlim", "14.07.2026", 86, True),
    ("Nazorat testi (3-modul)", "Mustaqil taʼlim", "20.06.2026", 54, False),
    ("Yakuniy test", "Ishlarni muvofiqlashtirish", "11.04.2026", 70, True),
]


def trow(t, c, d, s, ok):
    st = '<span class="st green"><i></i>Oʻtdi</span>' if ok else '<span class="st red"><i></i>Oʻtmadi</span>'
    col = "var(--ink)" if ok else "var(--red)"
    return f'<tr><td><b>{t}</b><small>{c}</small></td><td class="num mut">{d}</td><td><span class="sc" style="color:{col}">{s}</span><span class="mut"> / 100</span></td><td>{st}</td></tr>'


results_body = f"""
<main class="ct">
  <div class="kpis">
    <section class="card kpi"><div class="kpi-h">Oʻrtacha ball<span class="ki">{ic("target")}</span></div><div class="kv"><b>78</b><small>/ 100</small><span class="dl">+6{ic("arrow", style="transform:rotate(-45deg)")}</span></div><div class="kf">oʻtgan oyga nisbatan</div></section>
    <section class="card kpi"><div class="kpi-h">Topshirilgan testlar<span class="ki">{ic("task")}</span></div><div class="kv"><b>9</b><small>ta</small></div><div class="kf">8 tasidan oʻtilgan</div></section>
    <section class="card kpi"><div class="kpi-h">Sertifikatlar<span class="ki">{ic("award")}</span></div><div class="kv"><b>2</b><small>ta</small></div><div class="kf">2 ta kurs yakunlangan</div></section>
    <section class="card kpi"><div class="kpi-h">Oʻqish vaqti<span class="ki">{ic("clock")}</span></div><div class="kv"><b>132</b><small>soat</small><span class="dl">+8%{ic("arrow", style="transform:rotate(-45deg)")}</span></div><div class="kf">oxirgi 12 oyda</div></section>
  </div>

  <section class="card">
    <div class="ch"><h3>Ballar dinamikasi</h3>
      <div class="leg ml"><span style="color:var(--blue)"><i></i>SIZ</span><span style="color:var(--amber)"><i></i>GURUH OʻRTACHASI</span></div>
      <span class="per">{ic("chevl")}Oxirgi 12 oy{ic("chevr")}</span></div>
    <div class="cw">{line_svg}<div class="tip" style="left:{tip[0]+32:.0f}px;top:{tip[1]-8:.0f}px"><span>Avgust · Kirish testi</span><b>81 / 100</b></div></div>
  </section>

  <div class="ct two" style="padding:0">
    <section class="card">
      <div class="ch"><h3>Testlar tarixi</h3><div class="seg ml"><span class="on">Barchasi <em>9</em></span><span>Oʻtilgan <em>8</em></span><span>Oʻtilmagan <em>1</em></span></div></div>
      <table><thead><tr><th>Test</th><th>Sana</th><th>Ball</th><th>Natija</th></tr></thead><tbody>{"".join(trow(*t) for t in tests)}</tbody></table>
    </section>
    <div class="col">
      <section class="card">
        <div class="ch"><h3>Sertifikatlar</h3><a class="lnk">Tekshirish</a></div>
        <div class="cert"><span class="cimg">{ic("award")}</span><div><b>Mustaqil taʼlim</b><span>№ RM-2026-003112 · 86 ball</span></div><div class="acts"><span class="icb">{ic("eye")}</span><span class="icb">{ic("dl")}</span></div></div>
        <div class="cert"><span class="cimg">{ic("award")}</span><div><b>Ishlarni muvofiqlashtirish</b><span>№ RM-2026-001287 · 70 ball</span></div><div class="acts"><span class="icb">{ic("eye")}</span><span class="icb">{ic("dl")}</span></div></div>
      </section>
      <section class="card">
        <div class="ch"><h3>Kurslar progressi</h3></div>
        <div class="cp">
          <div><div class="pt"><span>Zamonaviy HR</span><b>29%</b></div><div class="bar"><i style="width:29%"></i></div></div>
          <div><div class="pt"><span>Mustaqil taʼlim</span><b>100%</b></div><div class="bar g"><i style="width:100%"></i></div></div>
          <div><div class="pt"><span>Ishlarni muvofiqlashtirish</span><b>100%</b></div><div class="bar g"><i style="width:100%"></i></div></div>
        </div>
      </section>
    </div>
  </div>
</main>"""

results_hd = (f'<h1>Natijalarim</h1><span class="ml"></span><div class="seg"><span>Oy</span><span>Yil</span><span class="on">Barcha vaqt</span></div>'
              f'<a class="btn b-white">{ic("dl")}Hisobotni yuklash</a>')

# ---------------------------------------------------------------- 8. Mening kurslarim
css_courses = """
.bar2{display:flex;align-items:center;gap:10px}
.fsearch{width:280px;height:36px;border-radius:9px;background:#fff;box-shadow:var(--sh);display:flex;align-items:center;gap:8px;padding:0 12px;font-size:13px;color:var(--subtle)}
.fsearch .ic{width:15px;height:15px}
.sel{height:36px;padding:0 12px;border-radius:9px;background:#fff;box-shadow:var(--sh);display:inline-flex;align-items:center;gap:8px;font-size:13px;color:var(--muted)}
.sel b{color:var(--ink);font-weight:600}
.sel .ic{width:15px;height:15px}
.cgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.cc{display:flex;flex-direction:column;overflow:hidden}
.cov{position:relative;height:112px;padding:16px;display:flex;justify-content:space-between;align-items:flex-start;overflow:hidden;background:linear-gradient(135deg,#0B1A3F,#1E3F9A)}
.cov.g{background:linear-gradient(135deg,#0A4A33,#0E7A52)}
.cov.a{background:linear-gradient(135deg,#5A3A0C,#B7791F)}
.cov:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.06) 1px,transparent 1px);background-size:24px 24px;mask-image:linear-gradient(120deg,transparent 30%,#000);-webkit-mask-image:linear-gradient(120deg,transparent 30%,#000)}
.cov>*{position:relative}
.cico{width:40px;height:40px;border-radius:10px;background:rgba(255,255,255,.14);box-shadow:inset 0 0 0 1px rgba(255,255,255,.2);display:grid;place-items:center;color:#fff}
.cico .ic{width:20px;height:20px}
.cb{padding:16px 18px;flex:1;display:flex;flex-direction:column}
.cb h4{font-size:15px;font-weight:600;color:var(--ink);line-height:1.35}
.cb .m{display:flex;flex-wrap:wrap;gap:6px 12px;margin-top:8px;font-size:12.5px;color:var(--muted)}
.cb .m span{display:inline-flex;align-items:center;gap:5px}
.cb .m .ic{width:14px;height:14px;color:var(--subtle)}
.cb .pr{margin-top:auto;padding-top:16px}
.cb .pt{display:flex;justify-content:space-between;font-size:12.5px;color:var(--muted);margin-bottom:7px}
.cb .pt b{color:var(--ink);font-variant-numeric:tabular-nums}
.cf{display:flex;align-items:center;gap:8px;padding:12px 18px;border-top:1px solid var(--line-2);background:#FCFDFE}
.cf .tch{display:flex;align-items:center;gap:8px;font-size:12.5px;color:var(--muted)}
.cf .btn{margin-left:auto}
.add{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:10px;border-radius:14px;border:1.5px dashed var(--line);padding:24px;min-height:300px;color:var(--muted);font-size:13px}
.add .pl{width:44px;height:44px;border-radius:12px;background:#fff;box-shadow:var(--sh);display:grid;place-items:center;color:var(--blue)}
.add .pl .ic{width:20px;height:20px}
.add b{display:block;font-size:14.5px;color:var(--ink)}
"""


def ccard(cov, icon, status, title, group, meta2, ptxt, pct, btn, teacher=("AS", "Atabayev S.")):
    barcls = "bar g" if pct == 100 else "bar"
    return f"""<article class="card cc">
  <div class="cov {cov}"><span class="cico">{ic(icon)}</span>{status}</div>
  <div class="cb"><h4>{title}</h4>
    <div class="m"><span>{ic("users")}{group}</span><span>{ic("layers")}{meta2}</span></div>
    <div class="pr"><div class="pt"><span>{ptxt}</span><b>{pct}%</b></div><div class="{barcls}"><i style="width:{pct}%"></i></div></div></div>
  <div class="cf"><span class="tch"><span class="av sm navy">{teacher[0]}</span>{teacher[1]}</span>{btn}</div>
</article>"""


courses_body = f"""
<main class="ct">
  <div class="bar2">
    <div class="seg"><span class="on">Barchasi <em>4</em></span><span>Faol <em>1</em></span><span>Rejada <em>1</em></span><span>Tugatilgan <em>2</em></span></div>
    <span class="ml"></span>
    <div class="fsearch">{ic("search")}Kurs nomi boʻyicha qidirish</div>
    <span class="sel">Saralash: <b>Oxirgi faollik</b>{ic("chevd")}</span>
  </div>
  <div class="cgrid">
    {ccard("", "users", '<span class="st blue"><i></i>Joriy</span>', "Zamonaviy inson resurslarini boshqarish", "17-26-guruh", "4 modul · 120 soat", "21 ta darsdan 6 tasi", 29, '<a class="btn b-sm b-pri">Davom etish</a>')}
    {ccard("a", "shield", '<span class="st amber"><i></i>Rejada</span>', "Mehnat muhofazasi asoslari", "21-04-guruh", "8 modul · 72 soat", "Boshlanish: 08.11.2026", 0, '<a class="btn b-sm b-white">Kurs dasturi</a>', ("KM", "Karimova M."))}
    {ccard("g", "layers", '<span class="st green"><i></i>Tugatilgan</span>', "Mustaqil taʼlim", "Test guruhi", "12 dars · 36 soat", "Ball: 86 / 100", 100, f'<a class="btn b-sm b-white">{ic("dl")}Sertifikat</a>')}
    {ccard("g", "users", '<span class="st green"><i></i>Tugatilgan</span>', "Ishlarni muvofiqlashtirish", "8-guruh", "16 dars · 48 soat", "Ball: 70 / 100", 100, f'<a class="btn b-sm b-white">{ic("dl")}Sertifikat</a>', ("RA", "Rasulov A."))}
    <div class="add"><span class="pl">{ic("arrow", style="transform:rotate(-45deg)")}</span><b>Yangi kursga yozilish</b>Individual oʻqish uchun ariza qoldiring — guruhga qoʻshilgach kurs shu yerda paydo boʻladi.<a class="btn b-sm b-white" style="margin-top:6px">Ariza qoldirish</a></div>
  </div>
</main>"""

courses_hd = f'<h1>Mening kurslarim</h1>' + tools()

# ---------------------------------------------------------------- 13. Birinchi kirish
css_first = """
.wl{position:relative;overflow:hidden;padding:48px 40px 40px;text-align:center}
.wl:before{content:"";position:absolute;left:50%;top:-160px;width:720px;height:460px;margin-left:-360px;background:radial-gradient(closest-side,rgba(37,80,192,.16),rgba(37,80,192,.05) 60%,transparent);pointer-events:none}
.wl>*{position:relative}
.wic{width:72px;height:72px;border-radius:20px;margin:0 auto;display:grid;place-items:center;background:#fff;color:var(--blue);box-shadow:0 0 0 10px rgba(37,80,192,.07),0 0 0 1px var(--blue-100),0 10px 24px -8px rgba(37,80,192,.35)}
.wic .ic{width:30px;height:30px}
.wl h2{font-size:26px;letter-spacing:-.02em;color:var(--ink);margin:22px 0 8px}
.wl p{max-width:520px;margin:0 auto;color:var(--muted);font-size:14.5px;line-height:1.6}
.wl .acts{display:flex;gap:10px;justify-content:center;margin-top:24px}
.steps3{display:grid;grid-template-columns:repeat(3,1fr);margin:36px -40px -40px;border-top:1px solid var(--line);text-align:left}
.steps3>div{padding:18px 22px;display:flex;gap:12px;align-items:flex-start}
.steps3>div+div{border-left:1px solid var(--line)}
.steps3 b{display:block;font-size:14px;font-weight:600;color:var(--ink)}
.steps3 span.s{font-size:12.5px;color:var(--muted)}
.steps3 .bar{margin-top:8px;width:140px}
.ring2{width:28px;height:28px;border-radius:50%;flex:none;background:conic-gradient(var(--blue) 0 40%,var(--line) 0);display:grid;place-items:center}
.ring2:after{content:"";width:20px;height:20px;border-radius:50%;background:#fff}
.wg{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.wc{padding:18px}
.wc .wi{width:40px;height:40px;border-radius:10px;display:grid;place-items:center;background:var(--blue-50);color:var(--blue);box-shadow:inset 0 0 0 1px var(--blue-100)}
.wc .wi .ic{width:19px;height:19px}
.wc h4{font-size:14.5px;font-weight:600;color:var(--ink);margin:14px 0 4px}
.wc p{font-size:13px;color:var(--muted);line-height:1.5}
.wc a{display:inline-flex;align-items:center;gap:6px;margin-top:12px;font-size:13px;font-weight:600;color:var(--blue)}
.wc a .ic{width:14px;height:14px}
.sh{display:flex;align-items:center;gap:10px;margin-top:8px}
.sh h3{font-size:15px;font-weight:600;color:var(--ink)}
"""

first_body = f"""
<main class="ct" style="max-width:1080px;margin:0 auto;width:100%">
  <section class="card wl">
    <span class="wic">{ic("book")}</span>
    <h2>Xush kelibsiz, Sarvar!</h2>
    <p>Hozircha sizda faol kurs yoʻq. Individual oʻqish uchun ariza qoldiring — guruhga qoʻshilganingizdan keyin darslar shu yerda paydo boʻladi.</p>
    <div class="acts"><a class="btn b-pri">{ic("file")}Ariza qoldirish</a><a class="btn b-white">Kurslar katalogi</a></div>
    <div class="steps3">
      <div><span class="ring2"></span><div><span class="cap">1-qadam</span><b>Profilni toʻldiring</b><span class="s">2 / 5 maydon toʻldirilgan</span><div class="bar"><i style="width:40%"></i></div></div></div>
      <div><span class="dotc">2</span><div><span class="cap">2-qadam</span><b>Ariza qoldiring</b><span class="s">3 ish kuni ichida koʻrib chiqiladi</span></div></div>
      <div><span class="dotc">3</span><div><span class="cap">3-qadam</span><b>Guruhga qoʻshiling</b><span class="s">Kirish maʼlumotlari SMS orqali keladi</span></div></div>
    </div>
  </section>
  <div class="sh"><h3>Kutayotganda nima qilish mumkin</h3></div>
  <div class="wg">
    <section class="card wc"><span class="wi">{ic("lib")}</span><h4>Elektron kutubxona</h4><p>42 ta qonunchilik hujjati, qoʻllanma va namunaviy hujjatlar.</p><a>Kutubxonaga oʻtish{ic("arrow")}</a></section>
    <section class="card wc"><span class="wi">{ic("video")}</span><h4>Ochiq maʼruzalar</h4><p>Bu hafta 3 ta ochiq videokonferensiya rejalashtirilgan.</p><a>Jadvalni koʻrish{ic("arrow")}</a></section>
    <section class="card wc"><span class="wi">{ic("user")}</span><h4>Profilni toʻldirish</h4><p>Lavozim va ish joyini koʻrsating — mos kurs tavsiya qilamiz.</p><a>Profilga oʻtish{ic("arrow")}</a></section>
  </div>
</main>"""

first_hd = '<h1>Asosiy sahifa</h1>' + tools()

if __name__ == "__main__":
    write("6-test-natijasi.html", page("Test natijasi", result_hd, result_body, css_result, active="courses"))
    write("7-natijalarim.html", page("Natijalarim", results_hd, results_body, css_results, active="results"))
    write("8-mening-kurslarim.html", page("Mening kurslarim", courses_hd, courses_body, css_courses, active="courses"))
    write("9-birinchi-kirish.html", page("Birinchi kirish", first_hd, first_body, css_first, active="home", badges=False))
    print("ok")
