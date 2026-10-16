"""3-partiya: Forum, Chat, Videokonferensiyalar, Kutubxona, Arizalar."""
import os
from shell import page, ic, tools

OUT = os.path.join(os.path.dirname(__file__), "..")


def write(name, html):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(html)


COMMON = """
.split{display:grid;grid-template-columns:minmax(0,1fr) 440px;gap:16px;padding:24px;align-items:start}
.drw{background:#fff;border-radius:14px;box-shadow:var(--sh-lg);overflow:hidden;display:flex;flex-direction:column}
.drw-h{display:flex;gap:12px;align-items:flex-start;padding:20px 20px 16px}
.drw-h h2{font-size:18px;line-height:1.3;letter-spacing:-.01em;color:var(--ink)}
.drw-h p{font-size:12.5px;color:var(--muted);margin-top:4px}
.x{margin-left:auto;width:30px;height:30px;border-radius:8px;display:grid;place-items:center;color:var(--muted);box-shadow:var(--sh);flex:none}
.x .ic{width:15px;height:15px}
.drw .kvrow{padding:0 20px 16px;border-bottom:1px dashed var(--line);margin:0}
.drw-b{padding:16px 20px}
.drw-f{display:flex;align-items:center;gap:8px;padding:14px 20px;border-top:1px solid var(--line);background:var(--soft)}
table{width:100%;border-collapse:collapse}
th{text-align:left;font-size:12.5px;font-weight:500;color:var(--muted);padding:10px 20px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:#FAFBFD;white-space:nowrap}
td{padding:0 20px;height:56px;border-bottom:1px solid var(--line-2);font-size:13.5px;color:var(--ink)}
tr:last-child td{border-bottom:0}
tr.on td{background:var(--blue-50)}
tr.on td:first-child{box-shadow:inset 3px 0 0 var(--blue)}
td small{display:block;font-size:12px;color:var(--muted);margin-top:1px}
.icb{width:32px;height:32px;border-radius:8px;display:inline-grid;place-items:center;color:var(--muted);box-shadow:var(--sh);background:#fff}
.icb .ic{width:15px;height:15px}
.fsearch{height:36px;border-radius:9px;background:#fff;box-shadow:var(--sh);display:flex;align-items:center;gap:8px;padding:0 12px;font-size:13px;color:var(--subtle)}
.fsearch .ic{width:15px;height:15px}
.sel{height:36px;padding:0 12px;border-radius:9px;background:#fff;box-shadow:var(--sh);display:inline-flex;align-items:center;gap:8px;font-size:13px;color:var(--muted);white-space:nowrap}
.sel b{color:var(--ink);font-weight:600}
.sel .ic{width:15px;height:15px}
"""

# ---------------------------------------------------------------- 10. Forum
css_forum = COMMON + """
.th{display:flex;gap:12px;padding:14px 20px;border-top:1px solid var(--line-2);align-items:flex-start}
.th.on{background:var(--blue-50);box-shadow:inset 3px 0 0 var(--blue)}
.th b{display:block;font-size:14px;font-weight:600;color:var(--ink);line-height:1.4}
.th .m{display:flex;align-items:center;flex-wrap:wrap;gap:6px 10px;margin-top:6px;font-size:12.5px;color:var(--muted)}
.th .r{margin-left:auto;display:flex;flex-direction:column;align-items:flex-end;gap:8px;flex:none}
.cnt2{display:inline-flex;align-items:center;gap:5px;font-size:12.5px;color:var(--muted);font-variant-numeric:tabular-nums}
.cnt2 .ic{width:14px;height:14px}
.q{font-size:14px;line-height:1.6;color:var(--text)}
.ans{margin-top:14px;border-radius:12px;padding:14px;box-shadow:inset 0 0 0 1px var(--line)}
.ans.best{background:var(--green-50);box-shadow:inset 0 0 0 1px var(--green-100)}
.ans-h{display:flex;align-items:center;gap:10px;margin-bottom:8px}
.ans-h b{font-size:13.5px;font-weight:600;color:var(--ink)}
.ans-h span{font-size:12px;color:var(--muted)}
.ans p{font-size:13.5px;line-height:1.6;color:var(--text)}
.ans .f{display:flex;align-items:center;gap:14px;margin-top:10px;font-size:12.5px;color:var(--muted)}
.ans .f span{display:inline-flex;align-items:center;gap:5px}
.ans .f .ic{width:14px;height:14px}
.reply{flex:1;height:38px;border-radius:10px;background:#fff;box-shadow:var(--sh);display:flex;align-items:center;padding:0 12px;font-size:13px;color:var(--subtle)}
"""


def thread(av, avc, title, author, when, course, n, status, on=False):
    return (f'<div class="th{" on" if on else ""}"><span class="av {avc}">{av}</span><div><b>{title}</b>'
            f'<div class="m"><span>{author} · {when}</span><span class="tag t-gray">{course}</span></div></div>'
            f'<div class="r">{status}<span class="cnt2">{ic("chat")}{n} javob</span></div></div>')


forum_body = f"""
<main class="split">
  <section class="card">
    <div class="ch"><div class="seg"><span class="on">Barchasi <em>128</em></span><span>Mening savollarim <em>3</em></span><span>Javobsiz <em>12</em></span></div>
      <span class="sel ml">Kurs: <b>Barchasi</b>{ic("chevd")}</span><span class="sel">Saralash: <b>Yangi</b>{ic("chevd")}</span></div>
    {thread("BS", "", "Kirish testini qayta topshirish mumkinmi?", "Baxtiyorov Sarvar", "5 soat oldin", "Zamonaviy HR", 12, '<span class="st green"><i></i>Hal qilingan</span>', True)}
    {thread("AS", "navy", "Case study javobini qachongacha yuborish kerak?", "Atabayev Sirojiddin", "2 soat oldin", "Zamonaviy HR", 5, '<span class="st green"><i></i>Hal qilingan</span>')}
    {thread("KM", "amber", "Sertifikat qanday olinadi va qayerda tekshiriladi?", "Karimova Malika", "1 kun oldin", "Umumiy", 8, '<span class="st amber"><i></i>Javob kutilmoqda</span>')}
    {thread("DT", "blue", "Sinov muddati davomida xodimni ishdan boʻshatish tartibi", "Doniyorov Temur", "1 kun oldin", "Mehnat huquqi", 17, '<span class="st blue"><i></i>Muhokamada</span>')}
    {thread("NY", "", "Xavflarni baholash matritsasi uchun namuna bormi?", "Nazarova Yulduz", "2 kun oldin", "Mehnat muhofazasi", 4, '<span class="st green"><i></i>Hal qilingan</span>')}
    {thread("OR", "navy", "Videokonferensiya yozuvlari qancha vaqt saqlanadi?", "Olimov Rustam", "3 kun oldin", "Umumiy", 0, '<span class="st amber"><i></i>Javob kutilmoqda</span>')}
  </section>

  <aside class="drw">
    <div class="drw-h"><span class="av">BS</span><div><h2>Kirish testini qayta topshirish mumkinmi?</h2><p>Baxtiyorov Sarvar · 16.10.2026, 09:14</p></div><span class="x">{ic("x")}</span></div>
    <dl class="kvrow"><dt>{ic("target")}Holat</dt><dd><span class="st green"><i></i>Hal qilingan</span></dd><dt>{ic("book")}Kurs</dt><dd>Zamonaviy HR</dd><dt>{ic("list")}Boʻlim</dt><dd>Testlar</dd><dt>{ic("eye")}Koʻrishlar</dt><dd class="num">142</dd></dl>
    <div class="drw-b">
      <p class="q">Kirish testidan 64 ball oldim. Natijani yaxshilash uchun testni qayta topshirish imkoniyati bormi va qaysi ball hisobga olinadi?</p>
      <div class="ans best"><div class="ans-h"><span class="av sm navy">AS</span><b>Atabayev Sirojiddin</b><span class="tag t-green">Oʻqituvchi · eng yaxshi javob</span></div>
        <p>Ha, har bir test uchun 2 ta urinish bor. Ikkinchi urinish birinchisidan kamida 24 soat keyin ochiladi va <b>eng yuqori ball</b> hisobga olinadi.</p>
        <div class="f"><span>{ic("check")}Foydali · 24</span><span>4 soat oldin</span></div></div>
      <div class="ans"><div class="ans-h"><span class="av sm amber">KM</span><b>Karimova Malika</b><span>3 soat oldin</span></div>
        <p>Men ham qayta topshirganman — natija sahifasidagi «Qayta topshirish» tugmasi orqali boshlanadi.</p>
        <div class="f"><span>{ic("check")}Foydali · 7</span></div></div>
    </div>
    <div class="drw-f"><div class="reply">Javob yozing…</div><a class="btn b-pri">{ic("send")}Yuborish</a></div>
  </aside>
</main>"""

forum_hd = (f'<h1>Forum</h1><div class="search" role="search">{ic("search")}Forumdan qidirish<kbd>Ctrl K</kbd></div>'
            f'<a class="btn b-pri">{ic("chat")}Savol berish</a><span class="ib">{ic("bell")}<span class="dot"></span></span>')

# ---------------------------------------------------------------- 11. Chat
css_chat = """
.chat{margin:24px;display:grid;grid-template-columns:300px minmax(0,1fr) 280px;height:calc(900px - 64px - 48px - 16px);background:#fff;border-radius:14px;box-shadow:var(--sh);overflow:hidden}
.cl1{border-right:1px solid var(--line);display:flex;flex-direction:column}
.cl1 .top{padding:16px;display:grid;gap:10px;border-bottom:1px solid var(--line)}
.cs{height:36px;border-radius:9px;background:var(--bg);box-shadow:inset 0 0 0 1px var(--line);display:flex;align-items:center;gap:8px;padding:0 12px;font-size:13px;color:var(--subtle)}
.cs .ic{width:15px;height:15px}
.cv{display:flex;gap:12px;padding:12px 16px;align-items:center;border-bottom:1px solid var(--line-2)}
.cv.on{background:var(--blue-50);box-shadow:inset 3px 0 0 var(--blue)}
.avw{position:relative;flex:none}
.avw .on{position:absolute;right:0;bottom:0;width:10px;height:10px;border-radius:50%;background:#1BAA74;box-shadow:0 0 0 2px #fff}
.cv .t{min-width:0;flex:1}
.cv b{display:flex;justify-content:space-between;font-size:13.5px;font-weight:600;color:var(--ink)}
.cv b em{font-style:normal;font-weight:500;font-size:11.5px;color:var(--subtle);font-variant-numeric:tabular-nums}
.cv span.p{display:flex;justify-content:space-between;gap:8px;font-size:12.5px;color:var(--muted);margin-top:2px}
.cv span.p i{font-style:normal;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cv .cnt{margin-left:0}
.mid{display:flex;flex-direction:column;min-width:0}
.mh{display:flex;align-items:center;gap:12px;padding:12px 20px;border-bottom:1px solid var(--line)}
.mh b{display:block;font-size:14.5px;font-weight:600;color:var(--ink)}
.mh span.s{font-size:12.5px;color:var(--green)}
.mh .acts{margin-left:auto;display:flex;gap:6px}
.icb{width:34px;height:34px;border-radius:9px;display:grid;place-items:center;color:var(--muted);box-shadow:var(--sh);background:#fff}
.icb .ic{width:16px;height:16px}
.msgs{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:10px;background:var(--soft);overflow:hidden}
.day{align-self:center;font-size:11.5px;font-weight:600;color:var(--muted);background:#fff;box-shadow:var(--sh);padding:4px 10px;border-radius:99px;margin:4px 0}
.m{max-width:68%;padding:10px 14px;border-radius:14px;font-size:13.5px;line-height:1.55}
.m small{display:block;font-size:11px;margin-top:4px;text-align:right;font-variant-numeric:tabular-nums}
.m.in{align-self:flex-start;background:#fff;box-shadow:var(--sh);color:var(--text);border-bottom-left-radius:4px}
.m.in small{color:var(--subtle)}
.m.out{align-self:flex-end;background:var(--blue);color:#fff;border-bottom-right-radius:4px}
.m.out small{color:rgba(255,255,255,.7)}
.fm{display:flex;gap:10px;align-items:center;min-width:240px}
.fm b{display:block;font-size:13px;font-weight:600;color:var(--ink)}
.fm span{font-size:12px;color:var(--muted)}
.fm .ic{margin-left:auto;width:16px;height:16px;color:var(--muted)}
.typing{align-self:flex-start;display:flex;gap:4px;padding:10px 14px;border-radius:14px;background:#fff;box-shadow:var(--sh)}
.typing i{width:6px;height:6px;border-radius:50%;background:var(--subtle)}
.comp{display:flex;align-items:center;gap:8px;padding:12px 16px;border-top:1px solid var(--line)}
.comp .in{flex:1;height:40px;border-radius:10px;background:var(--bg);box-shadow:inset 0 0 0 1px var(--line);display:flex;align-items:center;padding:0 14px;font-size:13.5px;color:var(--subtle)}
.side{border-left:1px solid var(--line);padding:24px 20px;display:flex;flex-direction:column;gap:18px}
.prof{text-align:center}
.prof .av{width:64px;height:64px;font-size:20px;margin:0 auto}
.prof b{display:block;font-size:15px;font-weight:600;color:var(--ink);margin-top:12px}
.prof span{font-size:12.5px;color:var(--muted)}
.side .kvrow{grid-template-columns:118px 1fr;padding-top:16px;border-top:1px solid var(--line)}
.sf{display:flex;gap:10px;align-items:center}
.sf b{display:block;font-size:13px;font-weight:600;color:var(--ink)}
.sf span{font-size:12px;color:var(--muted)}
"""


def conv(av, avc, name, when, last, unread=0, online=False, on=False):
    o = '<span class="on"></span>' if online else ''
    u = f'<span class="cnt">{unread}</span>' if unread else ''
    return (f'<div class="cv{" on" if on else ""}"><span class="avw"><span class="av {avc}">{av}</span>{o}</span>'
            f'<div class="t"><b>{name}<em>{when}</em></b><span class="p"><i>{last}</i>{u}</span></div></div>')


chat_body = f"""
<div class="chat">
  <div class="cl1">
    <div class="top"><div class="cs">{ic("search")}Suhbatlardan qidirish</div><div class="seg"><span class="on">Barchasi</span><span>Oʻqituvchilar</span><span>Guruh</span></div></div>
    {conv("AS", "navy", "Atabayev Sirojiddin", "10:24", "Baholash mezonlarini ham yubordim", 2, True, True)}
    {conv("17", "blue", "17-26-guruh", "09:40", "Doniyorov T.: Ertangi suhbat soat nechada?", 5)}
    {conv("KM", "amber", "Karimova Malika", "Kecha", "Mehnat muhofazasi kursi 8-noyabrdan", 0, True)}
    {conv("QX", "", "Qoʻllab-quvvatlash", "14.10", "Arizangiz qabul qilindi. Raqami A-2026-0412")}
    {conv("RA", "navy", "Rasulov Akmal", "28.09", "Sertifikatingiz tayyor, tabriklayman!")}
  </div>
  <div class="mid">
    <div class="mh"><span class="avw"><span class="av navy">AS</span><span class="on"></span></span><div><b>Atabayev Sirojiddin</b><span class="s">Oʻqituvchi · onlayn</span></div>
      <div class="acts"><span class="icb">{ic("video")}</span><span class="icb">{ic("search")}</span><span class="icb">{ic("info")}</span></div></div>
    <div class="msgs">
      <span class="day">Bugun, 16-oktabr</span>
      <div class="m out">Assalomu alaykum! 2-modul case study topshirigʻi boʻyicha savolim bor edi.<small>10:12 ✓✓</small></div>
      <div class="m in">Va alaykum assalom, Sarvar. Albatta, soʻrang.<small>10:15</small></div>
      <div class="m out">Case study javobini qachongacha yuborish kerak? Savollarga birdaniga javob berish shartmi?<small>10:16 ✓✓</small></div>
      <div class="m in">21-oktabrgacha. Har bir savolga alohida javob yuboring — yuborganingizdan keyin ekspert javobi ochiladi va solishtirishingiz mumkin.<small>10:20</small></div>
      <div class="m in"><div class="fm"><span class="fileic pdf">PDF</span><div><b>Baholash_mezonlari.pdf</b><span>180 KB</span></div>{ic("dl")}</div><small>10:24</small></div>
      <div class="typing"><i></i><i></i><i></i></div>
    </div>
    <div class="comp"><span class="icb">{ic("paperclip")}</span><div class="in">Xabar yozing…</div><a class="btn b-pri">{ic("send")}Yuborish</a></div>
  </div>
  <div class="side">
    <div class="prof"><span class="av navy">AS</span><b>Atabayev Sirojiddin</b><span>HR boʻyicha ekspert</span></div>
    <dl class="kvrow"><dt>{ic("book")}Kurs</dt><dd>Zamonaviy HR</dd><dt>{ic("cal")}Konsultatsiya</dt><dd>Pa, 15:00–16:00</dd><dt>{ic("clock")}Javob vaqti</dt><dd>~4 soat</dd></dl>
    <div><span class="cap">Ulashilgan fayllar · 2</span>
      <div class="sf" style="margin-top:12px"><span class="fileic pdf">PDF</span><div><b>Baholash_mezonlari.pdf</b><span>Bugun · 180 KB</span></div></div>
      <div class="sf" style="margin-top:10px"><span class="fileic doc">DOC</span><div><b>Case_namuna.docx</b><span>12.10 · 64 KB</span></div></div></div>
    <a class="btn b-white" style="margin-top:auto">{ic("video")}Videoqoʻngʻiroq</a>
  </div>
</div>"""

chat_hd = '<h1>Chat</h1>' + tools()

# ---------------------------------------------------------------- 12. Videokonferensiyalar
css_video = """
.live{position:relative;overflow:hidden;padding:22px 24px;display:flex;gap:24px;align-items:center;box-shadow:0 0 0 1px var(--green-100),0 8px 24px -12px rgba(14,122,82,.35)}
.live:before{content:"";position:absolute;right:-120px;top:-120px;width:360px;height:360px;background:radial-gradient(closest-side,rgba(14,122,82,.12),transparent);pointer-events:none}
.live>*{position:relative}
.lv-ic{width:56px;height:56px;border-radius:14px;display:grid;place-items:center;background:var(--green-50);color:var(--green);box-shadow:inset 0 0 0 1px var(--green-100);flex:none}
.lv-ic .ic{width:26px;height:26px}
.live h2{font-size:19px;letter-spacing:-.01em;color:var(--ink);margin:8px 0 6px}
.live .m{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:13px;color:var(--muted)}
.live .m span{display:inline-flex;align-items:center;gap:6px}
.live .m .ic{width:15px;height:15px;color:var(--subtle)}
.st.lv i{color:var(--green);background:var(--green);box-shadow:0 0 0 3px rgba(14,122,82,.2)}
.stack{display:flex;align-items:center;margin-left:auto}
.stack .av{width:30px;height:30px;font-size:11px;box-shadow:0 0 0 2px #fff;margin-left:-6px}
.stack .av:first-child{margin-left:0}
.stack em{font-style:normal;font-size:12.5px;color:var(--muted);margin-left:10px;white-space:nowrap}
.dg{padding:10px 20px;background:#FAFBFD;border-top:1px solid var(--line);border-bottom:1px solid var(--line-2);font-size:12px;font-weight:600;letter-spacing:.06em;color:var(--muted);text-transform:uppercase}
.ev{display:flex;align-items:center;gap:16px;padding:14px 20px}
.ev+.ev{border-top:1px solid var(--line-2)}
.ev .tm{width:96px;flex:none;font-size:13.5px;font-weight:600;color:var(--ink);font-variant-numeric:tabular-nums}
.ev .tm small{display:block;font-size:12px;font-weight:500;color:var(--muted)}
.ev .bdr{width:3px;align-self:stretch;border-radius:3px;background:var(--blue-100)}
.ev b{display:block;font-size:14px;font-weight:600;color:var(--ink)}
.ev .m{display:flex;gap:10px;align-items:center;margin-top:4px;font-size:12.5px;color:var(--muted)}
.ev .r{margin-left:auto;display:flex;align-items:center;gap:8px}
.hint{display:flex;align-items:center;gap:8px;padding:12px 20px;border-top:1px solid var(--line);font-size:12.5px;color:var(--muted)}
.hint .ic{width:15px;height:15px}
.calh{display:flex;align-items:center;gap:8px;padding:16px 20px 8px}
.calh b{font-size:14.5px;font-weight:600;color:var(--ink)}
.calh .icb{width:28px;height:28px;border-radius:7px;display:grid;place-items:center;box-shadow:var(--sh);color:var(--muted)}
.calh .icb .ic{width:14px;height:14px}
.cal{display:grid;grid-template-columns:repeat(7,1fr);gap:2px;padding:4px 16px 18px;text-align:center}
.cal .dn{font-size:11px;font-weight:600;color:var(--subtle);padding:6px 0}
.cal span{position:relative;height:38px;display:grid;place-items:center;font-size:13px;color:var(--text);border-radius:9px;font-variant-numeric:tabular-nums}
.cal span.o{color:#C3C9D6}
.cal span.e:after{content:"";position:absolute;bottom:5px;left:50%;width:4px;height:4px;margin-left:-2px;border-radius:50%;background:var(--blue)}
.cal span.t{background:var(--blue);color:#fff;font-weight:700}
.cal span.t:after{background:#fff}
.rec{display:flex;gap:12px;align-items:center;padding:12px 20px;border-top:1px solid var(--line-2)}
.rec .th{width:64px;height:40px;border-radius:7px;background:linear-gradient(135deg,#0B1A3F,#1E3F9A);display:grid;place-items:center;color:#fff;flex:none;position:relative}
.rec .th .ic{width:14px;height:14px}
.rec .th em{position:absolute;right:3px;bottom:2px;font-style:normal;font-size:9.5px;font-weight:600;background:rgba(0,0,0,.4);padding:0 3px;border-radius:3px}
.rec b{display:block;font-size:13px;font-weight:600;color:var(--ink)}
.rec span{font-size:12px;color:var(--muted)}
"""


def ev(t1, t2, title, who, course, status, action):
    return (f'<div class="ev"><div class="tm">{t1}<small>{t2}</small></div><span class="bdr"></span>'
            f'<div><b>{title}</b><div class="m"><span>{who}</span><span class="tag t-gray">{course}</span></div></div>'
            f'<div class="r">{status}{action}</div></div>')


def cal():
    out = [f'<span class="dn">{d}</span>' for d in ["Du", "Se", "Ch", "Pa", "Ju", "Sh", "Ya"]]
    for d in (28, 29, 30):
        out.append(f'<span class="o">{d}</span>')
    events = {2, 9, 14, 16, 17, 20, 23, 28}
    for d in range(1, 32):
        cls = "t e" if d == 16 else ("e" if d in events else "")
        out.append(f'<span class="{cls}">{d}</span>')
    for d in (1,):
        out.append(f'<span class="o">{d}</span>')
    return "".join(out)


video_body = f"""
<main class="ct two">
<div class="col">
  <section class="card live">
    <span class="lv-ic">{ic("video")}</span>
    <div><span class="st lv"><i></i>Jonli efirda · 24 daqiqadan beri</span>
      <h2>HR asoslari: ochiq maʼruza</h2>
      <div class="m"><span>{ic("user")}Atabayev Sirojiddin</span><span>{ic("clock")}10:00–11:30</span><span>{ic("book")}Zamonaviy HR</span></div></div>
    <div class="stack"><span class="av navy">AS</span><span class="av amber">KM</span><span class="av blue">DT</span><span class="av">NY</span><em>+38 ishtirokchi</em></div>
    <a class="btn b-pri">{ic("video")}Qoʻshilish</a>
  </section>

  <section class="card">
    <div class="ch"><h3>Kelgusi uchrashuvlar</h3><span class="cap ml">4 ta</span></div>
    <div class="dg">Bugun · 16-oktabr, juma</div>
    {ev("14:00", "60 daqiqa", "Case study tahlili", "Atabayev S.", "Zamonaviy HR", '<span class="st blue"><i></i>Rejalashtirilgan</span>', f'<a class="btn b-sm b-white">{ic("bell")}Eslatma</a>')}
    <div class="dg">Ertaga · 17-oktabr, shanba</div>
    {ev("11:00", "45 daqiqa", "Yakuniy suhbat", "Karimova M.", "Mustaqil taʼlim", '<span class="st green"><i></i>Eslatma oʻrnatilgan</span>', f'<a class="btn b-sm b-white">{ic("cal")}Kalendarga</a>')}
    <div class="dg">20-oktabr, seshanba</div>
    {ev("16:00", "90 daqiqa", "Mehnat qonunchiligi: savol-javob", "Rasulov A.", "Zamonaviy HR", '<span class="st blue"><i></i>Rejalashtirilgan</span>', f'<a class="btn b-sm b-white">{ic("bell")}Eslatma</a>')}
    {ev("18:00", "60 daqiqa", "Guruh bilan uchrashuv", "Atabayev S.", "17-26-guruh", '<span class="st blue"><i></i>Rejalashtirilgan</span>', f'<a class="btn b-sm b-white">{ic("bell")}Eslatma</a>')}
    <div class="hint">{ic("info")}«Qoʻshilish» tugmasi uchrashuv boshlanishidan 10 daqiqa oldin faollashadi.</div>
  </section>
</div>

<aside class="col">
  <section class="card">
    <div class="calh"><b>Oktabr 2026</b><span class="icb ml">{ic("chevl")}</span><span class="icb">{ic("chevr")}</span></div>
    <div class="cal">{cal()}</div>
  </section>
  <section class="card">
    <div class="ch"><h3>Yozuvlar</h3><a class="lnk">Barchasi</a></div>
    <div class="rec"><span class="th">{ic("play")}<em>58:12</em></span><div><b>Strategik HR: kirish maʼruzasi</b><span>14.10.2026 · Atabayev S.</span></div></div>
    <div class="rec"><span class="th">{ic("play")}<em>1:24:05</em></span><div><b>Mehnat shartnomasi amaliyoti</b><span>09.10.2026 · Rasulov A.</span></div></div>
    <div class="rec"><span class="th">{ic("play")}<em>45:30</em></span><div><b>Kirish testi tahlili</b><span>02.10.2026 · Atabayev S.</span></div></div>
  </section>
</aside>
</main>"""

video_hd = (f'<h1>Videokonferensiyalar</h1><span class="ml"></span><div class="seg"><span class="on">Kelgusi</span><span>Oʻtgan</span><span>Yozuvlar</span></div>'
            f'<span class="ib">{ic("globe")}UZ</span><span class="ib">{ic("bell")}<span class="dot"></span></span>')

# ---------------------------------------------------------------- 13. Kutubxona
css_lib = COMMON + """
.cats{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.cat{display:flex;gap:14px;align-items:center;padding:16px 18px}
.cat.on{box-shadow:0 0 0 1.5px var(--blue),0 0 0 4px var(--blue-50)}
.cat .ci{width:42px;height:42px;border-radius:11px;display:grid;place-items:center;flex:none}
.cat .ci .ic{width:20px;height:20px}
.cat b{display:block;font-size:14px;font-weight:600;color:var(--ink)}
.cat span{font-size:12.5px;color:var(--muted)}
.cat em{margin-left:auto;font-style:normal;font-size:20px;font-weight:700;color:var(--ink);font-variant-numeric:tabular-nums}
.ci.b{background:var(--blue-50);color:var(--blue)}.ci.g{background:var(--green-50);color:var(--green)}.ci.a{background:var(--amber-50);color:var(--amber)}.ci.n{background:#E8ECF5;color:var(--navy-800)}
.nm{display:flex;gap:12px;align-items:center}
.nm b{font-weight:600}
.acts{display:flex;gap:6px;justify-content:flex-end}
.pg{display:flex;align-items:center;gap:8px;padding:12px 20px;border-top:1px solid var(--line);font-size:13px;color:var(--muted)}
.pg .icb{width:30px;height:30px}
.pg .n{min-width:30px;height:30px;border-radius:8px;display:grid;place-items:center;font-weight:600;color:var(--muted)}
.pg .n.on{background:var(--blue);color:#fff}
"""

books = [
    ("pdf", "PDF", "Mehnat kodeksi (2023-yil tahriri)", "LexUZ rasmiy nashri", "Qonunchilik", "t-blue", "3,2 MB", "12.09.2026"),
    ("pdf", "PDF", "Davlat fuqarolik xizmati toʻgʻrisidagi qonun", "LexUZ rasmiy nashri", "Qonunchilik", "t-blue", "1,1 MB", "05.09.2026"),
    ("doc", "DOC", "Inson resurslarini boshqarish", "M. Karimova, 2021", "Qoʻllanma", "t-green", "4,6 MB", "28.08.2026"),
    ("pdf", "PDF", "Yangi Oʻzbekiston taraqqiyot strategiyasi", "Sh.M. Mirziyoyev, 2022", "Qoʻllanma", "t-green", "2,8 MB", "20.08.2026"),
    ("doc", "DOC", "Mehnat muhofazasi boʻyicha yoʻriqnoma namunasi", "Tahririyat", "Namunaviy hujjat", "t-amber", "96 KB", "14.08.2026"),
    ("doc", "DOC", "Ishga qabul qilish buyrugʻi namunasi", "Tahririyat", "Namunaviy hujjat", "t-amber", "48 KB", "14.08.2026"),
    ("ppt", "PPT", "Raqamli iqtisodiyot asoslari", "A. Rasulov, 2023", "Taqdimot", "t-gray", "7,9 MB", "02.08.2026"),
    ("", "XLS", "Xavflarni baholash matritsasi", "Tahririyat", "Namunaviy hujjat", "t-amber", "62 KB", "30.07.2026"),
]


def brow(fc, ft, title, auth, typ, tc, size, date):
    return (f'<tr><td><div class="nm"><span class="fileic {fc}">{ft}</span><div><b>{title}</b><small>{auth}</small></div></div></td>'
            f'<td><span class="tag {tc}">{typ}</span></td><td class="num mut">{size}</td><td class="num mut">{date}</td>'
            f'<td><div class="acts"><span class="icb">{ic("eye")}</span><span class="icb">{ic("dl")}</span></div></td></tr>')


lib_body = f"""
<main class="ct">
  <div class="cats">
    <section class="card cat"><span class="ci b">{ic("shield")}</span><div><b>Qonunchilik</b><span>Kodeks, qonun, qaror</span></div><em>18</em></section>
    <section class="card cat"><span class="ci g">{ic("book")}</span><div><b>Qoʻllanmalar</b><span>Darslik va metodika</span></div><em>12</em></section>
    <section class="card cat"><span class="ci a">{ic("file")}</span><div><b>Namunaviy hujjatlar</b><span>Buyruq, yoʻriqnoma</span></div><em>9</em></section>
    <section class="card cat"><span class="ci n">{ic("slides")}</span><div><b>Taqdimotlar</b><span>Maʼruza slaydlari</span></div><em>3</em></section>
  </div>
  <section class="card">
    <div class="ch"><div class="seg"><span class="on">Barchasi <em>42</em></span><span>Saqlanganlar <em>5</em></span><span>Yangi <em>4</em></span></div>
      <div class="fsearch ml" style="width:300px">{ic("search")}Nomi yoki muallif boʻyicha qidirish</div>
      <span class="sel">Format: <b>Barchasi</b>{ic("chevd")}</span><span class="sel">Saralash: <b>Yangi</b>{ic("chevd")}</span></div>
    <table><thead><tr><th>Nomi</th><th style="width:170px">Turi</th><th style="width:110px">Hajmi</th><th style="width:130px">Qoʻshilgan</th><th style="width:100px"></th></tr></thead>
    <tbody>{"".join(brow(*b) for b in books)}</tbody></table>
    <div class="pg"><span>1–8 / 42 ta</span><span class="ml"></span><span class="icb">{ic("chevl")}</span><span class="n on">1</span><span class="n">2</span><span class="n">3</span><span class="n">…</span><span class="n">6</span><span class="icb">{ic("chevr")}</span></div>
  </section>
</main>"""

lib_hd = '<h1>Kutubxona</h1>' + tools()

# ---------------------------------------------------------------- 14. Arizalar
css_apps = COMMON + """
.tl{position:relative;display:grid;gap:14px;margin-top:4px}
.tl>div{display:flex;gap:12px;position:relative}
.tl>div:not(:last-child):after{content:"";position:absolute;left:13px;top:30px;bottom:-14px;width:2px;background:var(--line)}
.tl>div.d:not(:last-child):after{background:var(--green-100)}
.tl b{display:block;font-size:13.5px;font-weight:600;color:var(--ink)}
.tl span.s{font-size:12.5px;color:var(--muted);font-variant-numeric:tabular-nums}
.tl .p .dotc{background:#fff;box-shadow:inset 0 0 0 1.5px var(--amber);color:var(--amber)}
.sec{padding:16px 20px;border-top:1px solid var(--line)}
.sec .cap{display:block;margin-bottom:12px}
.doc{display:flex;gap:10px;align-items:center;padding:10px 0}
.doc+.doc{border-top:1px solid var(--line-2)}
.doc b{display:block;font-size:13px;font-weight:600;color:var(--ink)}
.doc span{font-size:12px;color:var(--muted)}
.ds{margin-left:auto;display:inline-flex;align-items:center;gap:6px;font-size:11px;font-weight:700;letter-spacing:.06em}
.ds i{width:8px;height:8px;border-radius:50%}
.ds.ok{color:var(--green)}.ds.ok i{background:var(--green)}
.ds.wt{color:var(--amber)}.ds.wt i{box-shadow:inset 0 0 0 2px var(--amber)}
.drop{display:flex;align-items:center;justify-content:center;gap:8px;height:52px;border-radius:10px;border:1.5px dashed var(--line);background:var(--soft);font-size:13px;color:var(--muted);margin-bottom:6px}
.drop .ic{width:16px;height:16px}
.drop u{color:var(--ink);font-weight:600}
.b-danger{color:var(--red)}
"""

apps = [
    ("Individual oʻqish arizasi", "A-2026-0412", "Yozilish", "14.10.2026", '<span class="st amber"><i></i>Koʻrib chiqilmoqda</span>', True),
    ("Sertifikat nusxasi", "A-2026-0388", "Hujjat", "05.10.2026", '<span class="st green"><i></i>Tasdiqlangan</span>', False),
    ("Guruhni oʻzgartirish", "A-2026-0351", "Guruh", "28.09.2026", '<span class="st red"><i></i>Rad etilgan</span>', False),
    ("Test natijasiga eʼtiroz", "A-2026-0297", "Baholash", "11.09.2026", '<span class="st green"><i></i>Tasdiqlangan</span>', False),
]


def arow(t, n, typ, d, st, on):
    return (f'<tr class="{"on" if on else ""}"><td><b style="font-weight:600">{t}</b><small>№ {n}</small></td>'
            f'<td class="mut">{typ}</td><td class="num mut">{d}</td><td>{st}</td><td style="width:40px;color:var(--subtle)">{ic("chevr")}</td></tr>')


apps_body = f"""
<main class="split">
  <div class="col">
    <section class="card">
      <div class="ch"><div class="seg"><span class="on">Barchasi <em>4</em></span><span>Koʻrib chiqilmoqda <em>1</em></span><span>Yakunlangan <em>3</em></span></div><span class="sel ml">Turi: <b>Barchasi</b>{ic("chevd")}</span></div>
      <table><thead><tr><th>Ariza</th><th style="width:132px">Turi</th><th style="width:108px">Yuborilgan</th><th style="width:164px">Holat</th><th style="width:36px"></th></tr></thead><tbody>{"".join(arow(*a) for a in apps)}</tbody></table>
    </section>
    <div class="alert a-blue">{ic("info")}<span>Arizalar <b>3 ish kuni</b> ichida koʻrib chiqiladi. Holat oʻzgarganda SMS va platforma orqali xabar beramiz.</span></div>
  </div>

  <aside class="drw">
    <div class="drw-h"><div><h2>Individual oʻqish uchun ariza</h2><p>Yuborilgan: 14.10.2026, 11:40</p></div><span class="x">{ic("x")}</span></div>
    <dl class="kvrow">
      <dt>{ic("target")}Holat</dt><dd><span class="st amber"><i></i>Koʻrib chiqilmoqda</span></dd>
      <dt>{ic("file")}Raqam</dt><dd>A-2026-0412</dd>
      <dt>{ic("book")}Kurs</dt><dd>Xodimlarni baholash va attestatsiya</dd>
      <dt>{ic("cal")}Javob muddati</dt><dd class="num">17.10.2026 <span class="mut" style="font-weight:400">· 1 kun qoldi</span></dd>
    </dl>
    <div class="drw-b"><span class="cap">Jarayon</span>
      <div class="tl" style="margin-top:12px">
        <div class="d"><span class="dotc done">{ic("check")}</span><div><b>Ariza yuborildi</b><span class="s">14.10.2026, 11:40</span></div></div>
        <div class="d"><span class="dotc done">{ic("check")}</span><div><b>Hujjatlar tekshirildi</b><span class="s">15.10.2026, 09:12 · Qoʻllab-quvvatlash</span></div></div>
        <div class="p"><span class="dotc">3</span><div><b>Komissiya koʻrib chiqmoqda</b><span class="s">Kutilmoqda</span></div></div>
        <div><span class="dotc">4</span><div><b>Qaror va guruhga biriktirish</b><span class="s">—</span></div></div>
      </div>
    </div>
    <div class="sec"><span class="cap">Hujjatlar · 2</span>
      <div class="drop">{ic("dl", style="transform:rotate(180deg)")}Fayllarni shu yerga tashlang yoki <u>yuklang</u></div>
      <div class="doc"><span class="fileic pdf">PDF</span><div><b>Pasport_nusxasi.pdf</b><span>Yuklangan: 14.10.2026</span></div><span class="ds ok">TASDIQLANDI<i></i></span></div>
      <div class="doc"><span class="fileic pdf">PDF</span><div><b>Ish_joyidan_malumotnoma.pdf</b><span>Yuklangan: 14.10.2026</span></div><span class="ds wt">KUTILMOQDA<i></i></span></div>
    </div>
    <div class="drw-f"><a class="btn b-ghost b-danger">Arizani bekor qilish</a><a class="btn b-white ml">{ic("chat")}Izoh qoʻshish</a></div>
  </aside>
</main>"""

apps_hd = (f'<h1>Arizalar</h1><span class="ml"></span><a class="btn b-pri">{ic("file")}Yangi ariza</a>'
           f'<span class="ib">{ic("globe")}UZ</span><span class="ib">{ic("bell")}<span class="dot"></span></span>')

if __name__ == "__main__":
    write("10-forum.html", page("Forum", forum_hd, forum_body, css_forum, active="forum"))
    write("11-chat.html", page("Chat", chat_hd, chat_body, css_chat, active="chat"))
    write("12-videokonferensiyalar.html", page("Videokonferensiyalar", video_hd, video_body, css_video, active="video"))
    write("13-kutubxona.html", page("Kutubxona", lib_hd, lib_body, css_lib, active="library"))
    write("14-arizalar.html", page("Arizalar", apps_hd, apps_body, css_apps, active="apps"))
    print("ok")
