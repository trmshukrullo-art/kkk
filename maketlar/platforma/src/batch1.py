"""1-partiya: Kurs ichi, Dars, Case study, Test."""
import os
from shell import page, ic, tools

OUT = os.path.join(os.path.dirname(__file__), "..")


def write(name, html):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(html)


# ---------------------------------------------------------------- 2. Kurs ichi
css_course = """
.sum{padding:20px}
.sum-top{display:flex;gap:16px;align-items:flex-start}
.tile{width:48px;height:48px;border-radius:12px;display:grid;place-items:center;flex:none;background:var(--blue-50);color:var(--blue);box-shadow:inset 0 0 0 1px var(--blue-100)}
.tile .ic{width:22px;height:22px}
.sum h2{font-size:20px;line-height:1.3;letter-spacing:-.015em;color:var(--ink);font-weight:700}
.meta{display:flex;align-items:center;flex-wrap:wrap;gap:8px 14px;margin-top:8px;font-size:13px;color:var(--muted)}
.meta span{display:inline-flex;align-items:center;gap:6px}
.meta .ic{width:15px;height:15px;color:var(--subtle)}
.sum-act{margin-left:auto;display:flex;gap:8px}
.stats{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;margin-top:20px;border-radius:12px;box-shadow:inset 0 0 0 1px var(--line);background:var(--soft)}
.stats>div{padding:14px 16px}
.stats>div+div{border-left:1px solid var(--line)}
.stats b{display:block;font-size:22px;font-weight:700;letter-spacing:-.02em;color:var(--ink);font-variant-numeric:tabular-nums;line-height:1.1;margin-top:6px}
.stats b small{font-size:13px;font-weight:500;color:var(--subtle);letter-spacing:0}
.stats .bar{margin-top:10px}
.mod{border-top:1px solid var(--line)}
.mod-h{display:flex;align-items:center;gap:14px;padding:16px 20px}
.mn{width:36px;height:36px;border-radius:10px;display:grid;place-items:center;font-weight:700;font-size:14px;flex:none;box-shadow:inset 0 0 0 1px var(--line);color:var(--muted);background:#fff}
.mn.done{background:var(--green-50);color:var(--green);box-shadow:inset 0 0 0 1px var(--green-100)}
.mn.cur{background:var(--blue);color:#fff;box-shadow:none}
.mn .ic{width:16px;height:16px}
.mod-h h4{font-size:14.5px;font-weight:600;color:var(--ink);margin-top:2px}
.mod-h .r{margin-left:auto;display:flex;align-items:center;gap:14px;font-size:13px;color:var(--muted);white-space:nowrap}
.mod-h .r>.ic{color:var(--subtle)}
.mod.locked .mod-h h4{color:var(--muted)}
.mini{display:flex;align-items:center;gap:8px}
.mini .bar{width:64px}
.lessons{padding:0 20px 14px 70px}
.ls{display:grid;grid-template-columns:28px 1fr auto 96px 120px;gap:14px;align-items:center;padding:10px 12px;border-radius:10px}
.ls+.ls{margin-top:2px}
.ls.cur{background:var(--blue-50);box-shadow:inset 0 0 0 1px var(--blue-100)}
.dotc{width:28px;height:28px;border-radius:50%;display:grid;place-items:center;font-size:12px;font-weight:700;box-shadow:inset 0 0 0 1.5px var(--line);color:var(--muted);background:#fff}
.dotc.done{box-shadow:inset 0 0 0 1.5px var(--green);color:var(--green);background:var(--green-50)}
.dotc.cur{background:var(--blue);color:#fff;box-shadow:none}
.dotc .ic{width:14px;height:14px;stroke-width:2.4}
.ls small{display:block;font-size:11px;font-weight:600;letter-spacing:.06em;color:var(--subtle)}
.ls b{font-size:14px;font-weight:500;color:var(--ink)}
.ls.cur b{font-weight:600}
.ls .du{font-size:12.5px;color:var(--muted);text-align:right;font-variant-numeric:tabular-nums}
.ls .act{text-align:right;font-size:12.5px;color:var(--muted)}
.tch{padding:0 20px 20px}
.tch-p{display:flex;gap:12px;align-items:center}
.tch-p b{display:block;font-size:14.5px;font-weight:600;color:var(--ink)}
.tch-p span{font-size:12.5px;color:var(--muted)}
.tch .kvrow{margin:16px 0}
.row{display:flex;gap:12px;align-items:center;padding:12px 20px;border-top:1px solid var(--line-2)}
.row b{display:block;font-size:13.5px;font-weight:600;color:var(--ink)}
.row span.s{font-size:12.5px;color:var(--muted)}
.row .r{margin-left:auto;text-align:right}
.row .r .d{display:block;font-size:12px;color:var(--muted);margin-top:4px;font-variant-numeric:tabular-nums}
.dlb{width:32px;height:32px;border-radius:8px;display:grid;place-items:center;color:var(--muted);box-shadow:var(--sh);margin-left:auto}
.dlb .ic{width:15px;height:15px}
"""


def lesson(n, title, kind, kcls, dur, state, act=""):
    mark = {"done": ic("check"), "cur": str(n), "todo": str(n)}[state]
    return (f'<div class="ls{" cur" if state == "cur" else ""}"><span class="dotc {state}">{mark}</span>'
            f'<div><small>{n}-DARS</small><b>{title}</b></div><span class="tag {kcls}">{kind}</span>'
            f'<span class="du">{dur}</span><span class="act">{act}</span></div>')


course_body = f"""
<main class="ct two">
<div class="col">
  <section class="card sum">
    <div class="sum-top">
      <span class="tile">{ic("users")}</span>
      <div>
        <h2>Zamonaviy inson resurslarini boshqarish</h2>
        <div class="meta"><span class="st blue"><i></i>Joriy</span><span>{ic("users")}17-26-guruh</span><span>{ic("layers")}4 modul · 21 dars · 120 soat</span><span>{ic("cal")}30.11.2026 gacha</span></div>
      </div>
    </div>
    <div class="stats">
      <div><span class="cap">Umumiy progress</span><b>29%</b><div class="bar"><i style="width:29%"></i></div></div>
      <div><span class="cap">Darslar</span><b>6 <small>/ 21</small></b></div>
      <div><span class="cap">Testlar</span><b>0 <small>/ 4</small></b></div>
      <div><span class="cap">Oʻrtacha ball</span><b>78 <small>/ 100</small></b></div>
    </div>
  </section>

  <section class="card">
    <div class="utabs"><span class="on">{ic("list")}Oʻquv yoʻli</span><span>{ic("file")}Materiallar <em>12</em></span><span>{ic("bell")}Eʼlonlar <em>2</em></span><span>{ic("users")}Guruh <em>24</em></span></div>
    <div class="mod" style="border-top:0">
      <div class="mod-h"><span class="mn done">{ic("check")}</span><div><span class="cap">1-modul</span><h4>Kirish: HR tizimiga umumiy nazar</h4></div>
        <div class="r"><span class="num">4 dars · 18 soat</span><span class="st amber"><i></i>Oraliq test kutilmoqda</span>{ic("chevd")}</div></div>
    </div>
    <div class="mod">
      <div class="mod-h"><span class="mn cur">2</span><div><span class="cap" style="color:var(--blue)">2-modul · joriy</span><h4>Zamonaviy inson resurslarini boshqarish asoslari</h4></div>
        <div class="r"><span class="num">6 dars · 36 soat</span><span class="mini"><span class="bar"><i style="width:33%"></i></span><b class="num" style="color:var(--ink)">2/6</b></span>{ic("chevd", style="transform:rotate(180deg)")}</div></div>
      <div class="lessons">
        {lesson(1, "HR menejment tushunchasi", "Video", "t-blue", "14:36", "done", "Bajarildi")}
        {lesson(2, "Kadrlar boʻlimidan strategik HR ga", "Slayd", "t-amber", "19 slayd", "done", "Bajarildi")}
        {lesson(3, "HR funksiyalari: klassik va zamonaviy yondashuv", "Video", "t-blue", "12:30", "cur", '<a class="btn b-sm b-pri">Davom etish</a>')}
        {lesson(4, "Modul boʻyicha nazorat testi", "Test", "t-gray", "10 savol", "todo", '<span class="num">28.10.2026</span>')}
        {lesson(5, "Oʻzbekiston mehnat bozori", "Matn", "t-green", "8 daq", "todo")}
        {lesson(6, "HR faoliyatining huquqiy asoslari", "Video", "t-blue", "16:05", "todo")}
      </div>
    </div>
    <div class="mod">
      <div class="mod-h"><span class="mn">3</span><div><span class="cap">3-modul</span><h4>Xodimlarni izlash, tanlash va ishga jalb qilish</h4></div>
        <div class="r"><span class="num">6 dars · 36 soat</span><span class="st gray"><i></i>Boshlanmagan</span>{ic("chevd")}</div></div>
    </div>
    <div class="mod locked">
      <div class="mod-h"><span class="mn">{ic("lock")}</span><div><span class="cap">4-modul</span><h4>Mehnat munosabatlari va ish haqi</h4></div>
        <div class="r"><span>2-modul nazorat testidan keyin ochiladi</span>{ic("lock")}</div></div>
    </div>
  </section>
</div>

<aside class="col">
  <section class="card">
    <div class="ch"><h3>Oʻqituvchi</h3></div>
    <div class="tch">
      <div class="tch-p"><span class="av lg navy">AS</span><div><b>Atabayev Sirojiddin</b><span>HR boʻyicha ekspert · 12 yillik tajriba</span></div></div>
      <dl class="kvrow"><dt>{ic("cal")}Konsultatsiya</dt><dd>Payshanba, 15:00–16:00</dd><dt>{ic("clock")}Javob vaqti</dt><dd>odatda 4 soat ichida</dd></dl>
      <a class="btn b-white" style="width:100%">{ic("chat")}Chatda yozish</a>
    </div>
  </section>
  <section class="card">
    <div class="ch"><h3>Muddatlar</h3><span class="st red ml"><i></i>1 ta shoshilinch</span></div>
    <div class="row"><div><b>Oraliq test (1-modul)</b><span class="s">25 savol · 20 daqiqa</span></div><div class="r"><span class="st red"><i></i>2 kun qoldi</span><span class="d">18.10.2026</span></div></div>
    <div class="row"><div><b>Case study: «Standart Servis»</b><span class="s">2-modul, 3-dars</span></div><div class="r"><span class="st amber"><i></i>5 kun qoldi</span><span class="d">21.10.2026</span></div></div>
    <div class="row"><div><b>Nazorat testi (2-modul)</b><span class="s">10 savol · 15 daqiqa</span></div><div class="r"><span class="st blue"><i></i>Rejada</span><span class="d">28.10.2026</span></div></div>
  </section>
  <section class="card">
    <div class="ch"><h3>Kurs hujjatlari</h3><a class="lnk">Barchasi</a></div>
    <div class="row"><span class="fileic pdf">PDF</span><div><b>Kurs dasturi</b><span class="s">PDF · 420 KB</span></div><span class="dlb">{ic("dl")}</span></div>
    <div class="row"><span class="fileic pdf">PDF</span><div><b>Baholash mezonlari</b><span class="s">PDF · 180 KB</span></div><span class="dlb">{ic("dl")}</span></div>
    <div class="row"><span class="fileic doc">DOC</span><div><b>Maʼruzalar toʻplami</b><span class="s">DOCX · 2,4 MB</span></div><span class="dlb">{ic("dl")}</span></div>
  </section>
</aside>
</main>"""

course_hd = (f'<span class="bk">{ic("back")}</span><span class="crumb">Mening kurslarim{ic("chevr")}<b>Zamonaviy inson resurslarini boshqarish</b></span>'
             + f'<span class="ml"></span><a class="btn b-white">{ic("dl")}Kurs dasturi</a><a class="btn b-pri">{ic("play")}Davom etish</a>')

# ---------------------------------------------------------------- 3. Dars
css_lesson = """
.ct.lesson{grid-template-columns:1fr 360px}
.player{position:relative;border-radius:14px;overflow:hidden;background:#0A1430;aspect-ratio:16/9;box-shadow:var(--sh)}
.slide{position:absolute;inset:0;padding:48px 56px;background:radial-gradient(600px 300px at 85% 10%,rgba(59,108,224,.35),transparent 60%),linear-gradient(160deg,#0B1A3F,#12275A);color:#fff}
.slide small{font-size:12px;font-weight:600;letter-spacing:.1em;color:var(--blue-300)}
.slide h2{font-size:30px;letter-spacing:-.02em;margin:10px 0 28px;font-weight:700}
.sgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.sgrid div{border-radius:12px;padding:16px;background:rgba(255,255,255,.06);box-shadow:inset 0 0 0 1px rgba(255,255,255,.1)}
.sgrid b{display:block;font-size:15px;margin:10px 0 4px}
.sgrid span{font-size:12.5px;color:rgba(255,255,255,.66);line-height:1.45}
.sgrid i{display:grid;place-items:center;width:30px;height:30px;border-radius:8px;background:rgba(59,108,224,.3);font-style:normal;font-weight:700;font-size:13px}
.ctrl{position:absolute;left:0;right:0;bottom:0;padding:28px 18px 14px;background:linear-gradient(180deg,transparent,rgba(5,10,28,.85))}
.track{position:relative;height:4px;border-radius:9px;background:rgba(255,255,255,.2)}
.track i{position:absolute;left:0;top:0;bottom:0;width:34%;border-radius:9px;background:var(--blue-500)}
.track em{position:absolute;top:-1px;width:2px;height:6px;background:rgba(255,255,255,.55)}
.track u{position:absolute;left:34%;top:50%;width:12px;height:12px;margin:-6px 0 0 -6px;border-radius:50%;background:#fff;box-shadow:0 0 0 4px rgba(59,108,224,.35)}
.cbar{display:flex;align-items:center;gap:14px;margin-top:12px;color:#fff;font-size:12.5px;font-variant-numeric:tabular-nums}
.cbar .ic{width:18px;height:18px}
.cbar .sp{margin-left:auto;display:flex;gap:14px;align-items:center}
.cbar .chap{color:rgba(255,255,255,.7)}
.speed{height:24px;padding:0 8px;border-radius:6px;background:rgba(255,255,255,.12);display:grid;place-items:center;font-weight:600;font-size:12px}
.lh{padding:18px 20px;display:flex;gap:16px;align-items:flex-start}
.lh h2{font-size:20px;line-height:1.3;letter-spacing:-.015em;color:var(--ink);margin-top:6px}
.lh .meta{display:flex;flex-wrap:wrap;gap:8px 14px;margin-top:8px;font-size:13px;color:var(--muted)}
.lh .meta span{display:inline-flex;align-items:center;gap:6px}
.lh .meta .ic{width:15px;height:15px;color:var(--subtle)}
.lh .acts{margin-left:auto;display:flex;gap:8px}
.tabc{padding:20px}
.tabc h4{font-size:14.5px;font-weight:600;color:var(--ink);margin-bottom:12px}
.kp{display:grid;grid-template-columns:28px 1fr auto;gap:12px;padding:12px 0;border-top:1px solid var(--line-2);align-items:start}
.kp:first-of-type{border-top:0;padding-top:0}
.kp>i{width:28px;height:28px;border-radius:8px;background:var(--blue-50);color:var(--blue);display:grid;place-items:center;font-style:normal;font-weight:700;font-size:12.5px}
.kp b{display:block;font-size:14px;color:var(--ink);font-weight:600}
.kp p{font-size:13.5px;color:var(--muted);margin-top:3px;line-height:1.55}
.ts{display:inline-flex;align-items:center;gap:5px;height:24px;padding:0 8px;border-radius:6px;background:var(--bg);box-shadow:inset 0 0 0 1px var(--line);font-size:12px;font-weight:600;color:var(--blue);font-variant-numeric:tabular-nums}
.ts .ic{width:11px;height:11px}
.note{margin-top:16px;display:flex;gap:10px;align-items:center;padding:10px 12px;border-radius:10px;background:var(--soft);box-shadow:inset 0 0 0 1px var(--line);font-size:13px;color:var(--subtle)}
.note .ic{width:16px;height:16px}
.note kbd{margin-left:auto;font:600 11px Inter;color:var(--muted);background:#fff;box-shadow:inset 0 0 0 1px var(--line);border-radius:6px;padding:3px 7px}
.mat{padding:0 12px 12px}
.mi{display:flex;align-items:center;gap:12px;padding:10px;border-radius:10px}
.mi+.mi{margin-top:4px}
.mi.on{background:var(--blue-50);box-shadow:inset 0 0 0 1.5px var(--blue)}
.mi .mic{width:36px;height:36px;border-radius:9px;display:grid;place-items:center;flex:none;box-shadow:inset 0 0 0 1px var(--line);background:#fff;color:var(--muted)}
.mi .mic .ic{width:17px;height:17px}
.mi.on .mic{color:var(--blue);box-shadow:inset 0 0 0 1px var(--blue-100)}
.mi b{display:block;font-size:13.5px;font-weight:600;color:var(--ink)}
.mi span.s{font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums}
.mi .chk{margin-left:auto;width:22px;height:22px;border-radius:50%;display:grid;place-items:center;flex:none;box-shadow:inset 0 0 0 1.5px var(--line-2),inset 0 0 0 1.5px var(--line)}
.mi .chk.ok{background:var(--green);box-shadow:none;color:#fff}
.mi .chk .ic{width:12px;height:12px;stroke-width:2.6}
.mi .pc{margin-left:auto;font-size:12px;font-weight:700;color:var(--blue);font-variant-numeric:tabular-nums}
.path{padding:4px 20px 18px;position:relative}
.ps{display:flex;align-items:center;gap:12px;padding:7px 0;position:relative;font-size:13.5px;color:var(--text)}
.ps:not(:last-child):after{content:"";position:absolute;left:13px;top:34px;height:14px;width:2px;background:var(--line)}
.ps.done:not(:last-child):after{background:var(--green-100)}
.ps .dotc{width:28px;height:28px}
.ps.cur{font-weight:600;color:var(--ink)}
.ps em{margin-left:auto;font-style:normal;font-size:12px;color:var(--subtle);font-variant-numeric:tabular-nums}
.ps.cur em{color:var(--blue);font-weight:600}
"""

lesson_body = f"""
<main class="ct lesson">
<div class="col">
  <div class="player" aria-label="Videomaʼruza pleyeri">
    <div class="slide">
      <small>2-MODUL · 3-DARS</small>
      <h2>HR funksiyalari: toʻrt asosiy yoʻnalish</h2>
      <div class="sgrid">
        <div><i>1</i><b>Rejalashtirish</b><span>Kadrlarga boʻlgan ehtiyojni prognozlash</span></div>
        <div><i>2</i><b>Tanlash</b><span>Nomzodlarni izlash va saralash</span></div>
        <div><i>3</i><b>Rivojlantirish</b><span>Oʻqitish va malaka oshirish</span></div>
        <div><i>4</i><b>Baholash</b><span>Samaradorlik va motivatsiya</span></div>
      </div>
    </div>
    <div class="ctrl">
      <div class="track"><i></i><em style="left:18%"></em><em style="left:46%"></em><em style="left:72%"></em><u></u></div>
      <div class="cbar">{ic("play")}<span>04:12 / 12:30</span><span class="chap">· Klassik yondashuv</span>
        <span class="sp">{ic("volume")}{ic("cc")}<span class="speed">1x</span>{ic("full")}</span></div>
    </div>
  </div>

  <section class="card">
    <div class="lh">
      <div><span class="cap">Zamonaviy inson resurslarini boshqarish · 2-modul</span>
        <h2>3-dars. HR funksiyalari: klassik va zamonaviy yondashuv</h2>
        <div class="meta"><span>{ic("user")}Atabayev Sirojiddin</span><span>{ic("video")}12:30 video</span><span>{ic("slides")}19 slayd</span><span>{ic("text")}8 daqiqa oʻqish</span></div></div>
      <div class="acts"><a class="btn b-white">{ic("bookmark")}Saqlash</a></div>
    </div>
    <div class="utabs bt"><span class="on">{ic("note")}Konspekt</span><span>{ic("text")}Transkript</span><span>{ic("paperclip")}Materiallar <em>3</em></span><span>{ic("chat")}Savol-javob <em>5</em></span></div>
    <div class="tabc">
      <h4>Darsning asosiy gʻoyalari</h4>
      <div class="kp"><i>1</i><div><b>Klassik yondashuv — maʼmuriy funksiya</b><p>Kadrlar boʻlimi hujjatlar, buyruqlar va hisobotlar bilan ishlaydi. Asosiy maqsad — mehnat qonunchiligiga rioya qilish.</p></div><span class="ts">{ic("play")}01:45</span></div>
      <div class="kp"><i>2</i><div><b>Zamonaviy yondashuv — strategik hamkor</b><p>HR tashkilot strategiyasini amalga oshirishda qatnashadi: talantlarni jalb qilish, rivojlantirish va saqlab qolish.</p></div><span class="ts">{ic("play")}05:20</span></div>
      <div class="kp"><i>3</i><div><b>Toʻrt funksiyaning oʻzaro bogʻliqligi</b><p>Rejalashtirish, tanlash, rivojlantirish va baholash yagona sikl sifatida ishlaydi — biri ikkinchisiga maʼlumot beradi.</p></div><span class="ts">{ic("play")}09:02</span></div>
      <div class="note">{ic("note")}04:12 vaqt belgisiga eslatma qoʻshish…<kbd>N</kbd></div>
    </div>
  </section>
</div>

<aside class="col">
  <section class="card">
    <div class="ch"><h3>Dars materiallari</h3><span class="cap ml">2 / 4 bajarildi</span></div>
    <div style="padding:0 20px 12px"><div class="bar"><i style="width:50%"></i></div></div>
    <div class="mat">
      <div class="mi on"><span class="mic">{ic("play")}</span><div><b>Videomaʼruza</b><span class="s">04:12 / 12:30</span></div><span class="pc">34%</span></div>
      <div class="mi"><span class="mic">{ic("slides")}</span><div><b>Taqdimot</b><span class="s">19 slayd</span></div><span class="chk ok">{ic("check")}</span></div>
      <div class="mi"><span class="mic">{ic("text")}</span><div><b>Maʼruza matni</b><span class="s">8 daqiqa</span></div><span class="chk ok">{ic("check")}</span></div>
      <div class="mi"><span class="mic">{ic("task")}</span><div><b>Case study</b><span class="s">21.10.2026 gacha</span></div><span class="st amber ml"><i></i>Topshiriq</span></div>
    </div>
  </section>
  <section class="card">
    <div class="ch"><h3>2-modul yoʻli</h3><span class="cap ml">2 / 6</span></div>
    <div class="path">
      <div class="ps done"><span class="dotc done">{ic("check")}</span>HR menejment tushunchasi<em>14:36</em></div>
      <div class="ps done"><span class="dotc done">{ic("check")}</span>Strategik HR ga oʻtish<em>19 sl.</em></div>
      <div class="ps cur"><span class="dotc cur">3</span>HR funksiyalari<em>Joriy</em></div>
      <div class="ps"><span class="dotc">4</span>Nazorat testi<em>10 savol</em></div>
      <div class="ps"><span class="dotc">5</span>Mehnat bozori<em>8 daq</em></div>
      <div class="ps"><span class="dotc">6</span>Huquqiy asoslar<em>16:05</em></div>
    </div>
  </section>
</aside>
</main>"""

lesson_hd = (f'<span class="bk">{ic("back")}</span><span class="crumb">Zamonaviy HR{ic("chevr")}2-modul{ic("chevr")}<b>3-dars</b></span>'
             f'<span class="ml"></span><a class="btn b-white">{ic("chevl")}Oldingi</a><a class="btn b-pri">Keyingi dars{ic("arrow")}</a>')

# ---------------------------------------------------------------- 4. Case study
css_case = """
.ct.case{grid-template-columns:1fr 360px}
.steps{display:flex;align-items:center;padding:18px 20px;gap:16px}
.steps h3{font-size:16px;font-weight:700;color:var(--ink);margin-top:4px}
.sx{margin-left:auto;display:flex;align-items:center}
.sx span{width:32px;height:32px;border-radius:50%;display:grid;place-items:center;font-size:13px;font-weight:700;color:var(--muted);background:#fff;box-shadow:inset 0 0 0 1.5px var(--line)}
.sx span.done{background:var(--green-50);color:var(--green);box-shadow:inset 0 0 0 1.5px var(--green)}
.sx span.cur{background:var(--blue);color:#fff;box-shadow:0 0 0 4px var(--blue-100)}
.sx span .ic{width:14px;height:14px;stroke-width:2.4}
.sx i{width:28px;height:2px;background:var(--line)}
.sx i.done{background:var(--green-100)}
.body{padding:0 20px 20px;font-size:14px;line-height:1.65;color:var(--text)}
.body p+p{margin-top:10px}
.body ul{margin:10px 0 0 0;list-style:none;display:grid;gap:8px}
.body li{display:flex;gap:10px}
.body li:before{content:"";width:6px;height:6px;border-radius:50%;background:var(--blue);margin-top:9px;flex:none}
.files{display:flex;gap:10px;margin-top:16px}
.fl{flex:1;display:flex;gap:10px;align-items:center;padding:10px 12px;border-radius:10px;box-shadow:inset 0 0 0 1px var(--line);background:var(--soft)}
.fl b{display:block;font-size:13px;font-weight:600;color:var(--ink)}
.fl span{font-size:12px;color:var(--muted)}
.fl .ic{margin-left:auto;width:16px;height:16px;color:var(--muted)}
.qh{display:flex;align-items:center;gap:10px;padding:16px 20px 0}
.qh .cap{color:var(--ink)}
.qt{padding:8px 20px 16px;font-size:15.5px;font-weight:600;color:var(--ink);line-height:1.45}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:0 20px 16px}
.cmp>div{border-radius:12px;padding:14px 16px;font-size:13.5px;line-height:1.6}
.cmp .mine{background:var(--soft);box-shadow:inset 0 0 0 1px var(--line);color:var(--text)}
.cmp .exp{background:var(--green-50);box-shadow:inset 0 0 0 1px var(--green-100);color:#123F2C}
.cmp .cap{display:flex;align-items:center;gap:6px;margin-bottom:8px}
.cmp .exp .cap{color:var(--green)}
.cmp .cap .ic{width:14px;height:14px}
.qf{display:flex;align-items:center;gap:10px;padding:12px 20px;border-top:1px solid var(--line-2);font-size:12.5px;color:var(--muted)}
.qf .ic{width:15px;height:15px}
.editor{margin:0 20px;border-radius:12px;box-shadow:inset 0 0 0 1.5px var(--blue),0 0 0 4px var(--blue-50);background:#fff}
.tb{display:flex;gap:4px;padding:8px 10px;border-bottom:1px solid var(--line-2)}
.tb span{width:30px;height:28px;border-radius:7px;display:grid;place-items:center;color:var(--muted)}
.tb span .ic{width:15px;height:15px}
.tb .sep{width:1px;height:18px;background:var(--line);margin:5px 4px}
.txt{padding:14px 16px;min-height:140px;font-size:14px;line-height:1.65;color:var(--text)}
.txt u{text-decoration:none;border-right:2px solid var(--blue);margin-left:1px}
.ef{display:flex;align-items:center;padding:8px 14px;border-top:1px solid var(--line-2);font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums}
.qa{display:flex;align-items:center;gap:8px;padding:16px 20px}
.locked{margin:0 20px 20px;border-radius:12px;border:1.5px dashed var(--line);padding:14px 16px;display:flex;gap:12px;align-items:center;font-size:13px;color:var(--muted)}
.locked .lk{width:34px;height:34px;border-radius:9px;background:var(--bg);display:grid;place-items:center;color:var(--subtle);flex:none}
.locked b{display:block;color:var(--ink);font-weight:600}
.qrow{display:flex;align-items:center;gap:12px;padding:14px 20px}
.qrow+.qrow{border-top:1px solid var(--line-2)}
.qrow .n{width:28px;height:28px;border-radius:50%;display:grid;place-items:center;font-size:12px;font-weight:700;color:var(--muted);box-shadow:inset 0 0 0 1.5px var(--line);flex:none}
.qrow b{font-size:13.5px;font-weight:500;color:var(--ink)}
.qrow .st{margin-left:auto}
.info{padding:0 20px 18px}
.info .kvrow{grid-template-columns:110px 1fr}
.desc{margin-top:14px;padding-top:14px;border-top:1px dashed var(--line);font-size:13px;line-height:1.6;color:var(--text)}
.desc .cap{display:block;margin-bottom:6px}
.crit{padding:0 20px 16px;display:grid;gap:10px}
.cr{display:flex;align-items:center;gap:10px;font-size:13px;color:var(--text)}
.cr .bx{width:18px;height:18px;border-radius:5px;box-shadow:inset 0 0 0 1.5px var(--line);flex:none}
.cr b{margin-left:auto;font-weight:600;color:var(--ink);font-variant-numeric:tabular-nums}
.tot{display:flex;justify-content:space-between;padding:12px 20px;border-top:1px solid var(--line);font-size:13px;font-weight:600;color:var(--ink)}
"""

case_body = f"""
<main class="ct case">
<div class="col">
  <section class="card steps">
    <div><span class="cap">Bajarilish</span><h3>4 ta savoldan 1 tasiga javob yuborildi</h3></div>
    <div class="sx"><span class="done">{ic("check")}</span><i class="done"></i><span class="cur">2</span><i></i><span>3</span><i></i><span>4</span></div>
  </section>

  <section class="card">
    <div class="ch"><h3>Vaziyat tavsifi</h3></div>
    <div class="body">
      <p>«Standart Servis» MChJ rahbari bir xodimni tezda ishdan boʻshatmoqchi boʻldi. HR mutaxassisi shaxsiy ish yigʻmajildini tekshirib, quyidagilarni aniqladi:</p>
      <ul><li>xodimga oldin rasmiy ogohlantirish berilmagan;</li><li>lavozim yoʻriqnomasida vazifalar aniq belgilanmagan;</li><li>topshiriqlar faqat ogʻzaki berilgan va qayd etilmagan;</li><li>ishdan boʻshatish uchun hujjatlashtirilgan qonuniy asos yoʻq.</li></ul>
      <div class="files">
        <div class="fl"><span class="fileic pdf">PDF</span><div><b>Mehnat_shartnomasi.pdf</b><span>240 KB</span></div>{ic("eye")}</div>
        <div class="fl"><span class="fileic doc">DOC</span><div><b>Lavozim_yoriqnomasi.docx</b><span>86 KB</span></div>{ic("eye")}</div>
      </div>
    </div>
  </section>

  <section class="card">
    <div class="qh"><span class="cap">1-savol</span><span class="st green ml"><i></i>Javob yuborildi</span></div>
    <div class="qt">Bu vaziyatda huquqiy asoslar nima uchun muhim?</div>
    <div class="cmp">
      <div class="mine"><span class="cap">{ic("user")}Sizning javobingiz</span>Hujjatlashtirilgan asos boʻlmasa, xodim ishdan boʻshatishni sudda nizolashishi mumkin. Tashkilot ishga tiklash va majburiy progul uchun haq toʻlashga majbur boʻladi.</div>
      <div class="exp"><span class="cap">{ic("shield")}Ekspert javobi</span>HR — eng katta huquqiy xavf bilan ishlaydigan yoʻnalishlardan biri. Hujjatlashtirilmagan jarayon tashkilotni moliyaviy va obroʻ xavfi ostida qoldiradi.</div>
    </div>
    <div class="qf">{ic("clock")}Oʻqituvchi bahosi kutilmoqda · Yuborilgan: 15.10.2026, 18:20</div>
  </section>

  <section class="card">
    <div class="qh"><span class="cap" style="color:var(--blue)">2-savol</span><span class="st blue ml"><i></i>Jarayonda</span></div>
    <div class="qt">HR mutaxassisi rahbarga qanday tavsiyalar berishi kerak? Harakatlar ketma-ketligini yozing.</div>
    <div class="editor">
      <div class="tb"><span>{ic("bold")}</span><span>{ic("list")}</span><span class="sep"></span><span>{ic("paperclip")}</span></div>
      <div class="txt">Birinchidan, xodimning lavozim yoʻriqnomasini qayta koʻrib chiqish va tanishtirish varaqasiga imzo olish kerak. Ikkinchidan, topshiriqlarni yozma shaklda berishni yoʻlga qoʻyish<u></u></div>
      <div class="ef">Qoralama avtomatik saqlanadi<span class="ml">214 / 1500</span></div>
    </div>
    <div class="qa"><a class="btn b-ghost">{ic("save")}Qoralamani saqlash</a><a class="btn b-pri ml">{ic("send")}Javobni yuborish</a></div>
    <div class="locked"><span class="lk">{ic("lock")}</span><div><b>Ekspert javobi yopiq</b>Javobingizni yuborganingizdan soʻng ochiladi va oʻz javobingiz bilan solishtirishingiz mumkin boʻladi.</div></div>
  </section>

  <section class="card">
    <div class="qrow"><span class="n">3</span><b>Xodim bilan suhbatni qanday tashkil etish kerak?</b><span class="st gray"><i></i>Javob berilmagan</span></div>
    <div class="qrow"><span class="n">4</span><b>Kelgusida bunday holatning oldini olish uchun qanday tartib joriy qilinadi?</b><span class="st gray"><i></i>Javob berilmagan</span></div>
  </section>
</div>

<aside class="col">
  <section class="card">
    <div class="ch"><h3>Topshiriq maʼlumotlari</h3></div>
    <div class="info">
      <dl class="kvrow">
        <dt>{ic("target")}Holat</dt><dd><span class="st amber"><i></i>Muddati yaqin</span></dd>
        <dt>{ic("book")}Kurs</dt><dd>Zamonaviy HR</dd>
        <dt>{ic("layers")}Modul</dt><dd>2-modul, 3-dars</dd>
        <dt>{ic("cal")}Muddat</dt><dd class="num">21.10.2026 <span class="mut" style="font-weight:400">· 5 kun qoldi</span></dd>
        <dt>{ic("award")}Maksimal ball</dt><dd class="num">20 ball</dd>
        <dt>{ic("user")}Baholovchi</dt><dd>Atabayev S.</dd>
      </dl>
      <div class="desc"><span class="cap">Tavsif</span>Vaziyatni tahlil qiling va har bir savolga asoslangan javob yozing. Javoblar alohida yuboriladi; har biridan soʻng ekspert javobi ochiladi.</div>
    </div>
  </section>
  <section class="card">
    <div class="ch"><h3>Baholash mezonlari</h3><span class="cl ml">{ic("list")}4</span></div>
    <div class="crit">
      <div class="cr"><span class="bx"></span>Huquqiy asoslarni toʻgʻri koʻrsatish<b>5</b></div>
      <div class="cr"><span class="bx"></span>Xavflarni aniqlash<b>5</b></div>
      <div class="cr"><span class="bx"></span>Amaliy, bosqichma-bosqich yechim<b>7</b></div>
      <div class="cr"><span class="bx"></span>Yozma bayon sifati<b>3</b></div>
    </div>
    <div class="tot"><span>Jami</span><span class="num">20 ball</span></div>
  </section>
  <div class="alert a-blue">{ic("info")}<span>Javob yuborilgach uni oʻzgartirib boʻlmaydi. Yuborishdan oldin qoralamani tekshiring.</span></div>
</aside>
</main>"""

case_hd = (f'<span class="bk">{ic("back")}</span><span class="crumb">Zamonaviy HR{ic("chevr")}2-modul{ic("chevr")}<b>Case study: «Standart Servis»</b></span>'
           f'<span class="st green ml"><i></i>Qoralama saqlandi · 14:32</span><span class="ib">{ic("help")}</span>')

# ---------------------------------------------------------------- 5. Test (fokus rejimi)
css_test = """
.tw{max-width:1180px;margin:0 auto;width:100%;display:grid;grid-template-columns:1fr 340px;gap:16px;padding:24px;align-items:start}
.hd .mark{width:30px;height:30px;font-size:14px}
.hd .vr{width:1px;height:24px;background:var(--line)}
.timer{display:inline-flex;align-items:center;gap:8px;height:38px;padding:0 14px;border-radius:10px;background:var(--amber-50);box-shadow:inset 0 0 0 1px var(--amber-100);color:#6B4610;font-size:13px;font-weight:500}
.timer b{font-size:15px;font-weight:700;color:#5A3A0C;font-variant-numeric:tabular-nums}
.timer .ic{width:16px;height:16px;color:var(--amber)}
.q{padding:24px 28px}
.qtop{display:flex;align-items:center;gap:10px}
.qtop .cap{color:var(--blue)}
.qtop .flag{margin-left:auto}
.qq{font-size:19px;line-height:1.45;font-weight:600;color:var(--ink);letter-spacing:-.01em;margin:12px 0 22px;max-width:760px}
.opts{display:grid;gap:10px}
.opt{display:flex;align-items:center;gap:14px;padding:14px 16px;border-radius:12px;background:#fff;box-shadow:inset 0 0 0 1px var(--line);font-size:14.5px;color:var(--text)}
.opt .k{width:28px;height:28px;border-radius:8px;display:grid;place-items:center;font-size:13px;font-weight:700;color:var(--muted);background:var(--bg);box-shadow:inset 0 0 0 1px var(--line);flex:none}
.opt .rd{margin-left:auto;width:20px;height:20px;border-radius:50%;box-shadow:inset 0 0 0 1.5px var(--line);flex:none}
.opt.sel{background:var(--blue-50);box-shadow:inset 0 0 0 1.5px var(--blue);color:var(--ink);font-weight:500}
.opt.sel .k{background:var(--blue);color:#fff;box-shadow:none}
.opt.sel .rd{box-shadow:inset 0 0 0 6px var(--blue);background:#fff}
.qnav{display:flex;align-items:center;gap:8px;margin-top:24px;padding-top:20px;border-top:1px solid var(--line-2)}
.keys{margin-top:12px;font-size:12px;color:var(--subtle);display:flex;gap:14px}
.keys kbd{font:600 11px Inter;color:var(--muted);background:#fff;box-shadow:inset 0 0 0 1px var(--line);border-radius:5px;padding:2px 6px;margin-right:4px}
.grid{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;padding:0 20px}
.grid span{position:relative;height:40px;border-radius:9px;display:grid;place-items:center;font-size:13px;font-weight:600;color:var(--muted);background:#fff;box-shadow:inset 0 0 0 1px var(--line);font-variant-numeric:tabular-nums}
.grid span.a{background:var(--blue-50);color:var(--blue);box-shadow:inset 0 0 0 1px var(--blue-100)}
.grid span.c{background:#fff;color:var(--blue);box-shadow:inset 0 0 0 2px var(--blue),0 0 0 3px var(--blue-50)}
.grid span.f:after{content:"";position:absolute;top:5px;right:5px;width:7px;height:7px;border-radius:50%;background:var(--amber)}
.legend{display:flex;flex-wrap:wrap;gap:8px 12px;padding:14px 20px;font-size:12px;color:var(--muted)}
.legend span{display:inline-flex;align-items:center;gap:6px}
.legend i{width:12px;height:12px;border-radius:4px;box-shadow:inset 0 0 0 1px var(--line);background:#fff}
.legend i.a{background:var(--blue-50);box-shadow:inset 0 0 0 1px var(--blue-100)}
.legend i.c{box-shadow:inset 0 0 0 2px var(--blue)}
.legend i.f{border-radius:50%;width:8px;height:8px;background:var(--amber);box-shadow:none}
.sumr{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line)}
.sumr div{padding:12px 16px;text-align:center}
.sumr div+div{border-left:1px solid var(--line)}
.sumr b{display:block;font-size:18px;font-weight:700;color:var(--ink);font-variant-numeric:tabular-nums}
.sumr span{font-size:11.5px;color:var(--muted)}
.tm{padding:0 20px 18px}
.tm .row2{display:flex;justify-content:space-between;font-size:12.5px;color:var(--muted);margin-bottom:8px;font-variant-numeric:tabular-nums}
.tm .bar i{background:var(--amber)}
"""

qcells = []
for i in range(1, 26):
    cls = "c" if i == 21 else ("a" if i <= 20 else "")
    if i in (7, 15):
        cls += " f"
    qcells.append(f'<span class="{cls.strip()}">{i}</span>')

test_body = f"""
<main class="tw">
<div class="col">
  <section class="card q">
    <div class="qtop"><span class="cap">21-savol · 25 tadan</span><span class="tag t-gray">Mehnat huquqi</span><a class="btn b-sm b-white flag">{ic("flag")}Keyinroq qaytish</a></div>
    <div class="qq">HR mutaxassisi nomzodning ijtimoiy tarmoqdagi faoliyatini koʻrib chiqishda qaysi maʼlumotlar qaroriga taʼsir qilmasligi kerak?</div>
    <div class="opts" role="radiogroup">
      <div class="opt"><span class="k">A</span>Professional portfolio va ekspertlik faoliyati<span class="rd"></span></div>
      <div class="opt sel" aria-checked="true"><span class="k">B</span>Nomzodning dini, millati, oilaviy holati va siyosiy qarashlari<span class="rd"></span></div>
      <div class="opt"><span class="k">C</span>Ish tajribasiga oid maʼlumotlar<span class="rd"></span></div>
      <div class="opt"><span class="k">D</span>Amaliy maqolalar va hamjamiyatdagi ishtirok<span class="rd"></span></div>
    </div>
    <div class="qnav"><a class="btn b-white">{ic("chevl")}Oldingi</a><a class="btn b-ghost">Javobni tozalash</a><a class="btn b-pri ml">Keyingi savol{ic("arrow")}</a></div>
  </section>
  <div class="keys"><span><kbd>A</kbd>–<kbd>D</kbd>javob tanlash</span><span><kbd>←</kbd><kbd>→</kbd>savollar</span><span><kbd>F</kbd>belgilash</span></div>
</div>

<aside class="col">
  <section class="card">
    <div class="ch"><h3>Savollar</h3><span class="cap ml">20 / 25</span></div>
    <div class="grid">{"".join(qcells)}</div>
    <div class="legend"><span><i class="a"></i>Javob berilgan</span><span><i class="c"></i>Joriy</span><span><i></i>Javobsiz</span><span><i class="f"></i>Belgilangan</span></div>
    <div class="sumr"><div><b>20</b><span>Javob berilgan</span></div><div><b>5</b><span>Qolgan</span></div><div><b>2</b><span>Belgilangan</span></div></div>
  </section>
  <section class="card">
    <div class="ch"><h3>Vaqt</h3><span class="cap ml">20 daqiqa</span></div>
    <div class="tm"><div class="row2"><span>Sarflandi: 07:19</span><span>Qoldi: 12:41</span></div><div class="bar"><i style="width:37%"></i></div></div>
  </section>
  <div class="alert a-blue">{ic("info")}<span>Natija test yakunlangach koʻrsatiladi. <b>Oʻtish bali — 60.</b> Vaqt tugasa, javoblar avtomatik yuboriladi.</span></div>
</aside>
</main>"""

test_hd = (f'<span class="mark">R</span><span class="vr"></span><h1>Oraliq test (1-modul)</h1><span class="tag t-gray">Zamonaviy HR</span>'
           f'<span class="ml"></span><span class="timer">{ic("clock")}Qoldi <b>12:41</b></span>'
           f'<a class="btn b-white">{ic("exit")}Saqlab chiqish</a><a class="btn b-pri">Testni yakunlash</a>')

if __name__ == "__main__":
    write("2-kurs-ichi.html", page("Kurs ichi", course_hd, course_body, css_course, active="courses"))
    write("3-dars.html", page("Dars", lesson_hd, lesson_body, css_lesson, active="courses"))
    write("4-case-study.html", page("Case study", case_hd, case_body, css_case, active="courses"))
    write("5-test.html", page("Test", test_hd, test_body, css_test, focus=True))
    print("ok")
