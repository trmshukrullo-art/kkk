"""Raqamli Malaka — umumiy qobiq: dizayn tokenlari, sidebar, header, komponentlar."""

ICONS = dict(
    home='<rect x="3" y="3" width="7" height="9" rx="1.5"/><rect x="14" y="3" width="7" height="5" rx="1.5"/><rect x="14" y="12" width="7" height="9" rx="1.5"/><rect x="3" y="16" width="7" height="5" rx="1.5"/>',
    book='<path d="M2 4h6a4 4 0 0 1 4 4v13a3 3 0 0 0-3-3H2zM22 4h-6a4 4 0 0 0-4 4v13a3 3 0 0 1 3-3h7z"/>',
    chart='<path d="M3 3v18h18M8 17V11M13 17V7M18 17v-4"/>',
    video='<path d="m22 8-6 4 6 4V8z"/><rect x="2" y="6" width="14" height="12" rx="2"/>',
    chat='<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    forum='<path d="M17 9V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v10l4-4h2"/><path d="M21 21l-4-4h-6a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2z"/>',
    lib='<path d="M4 19V5M8 19V5M12 19l-2-14M16 5h4v14h-4z"/>',
    file='<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13h6M9 17h6"/>',
    help='<circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3M12 17h.01"/>',
    panel='<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M9 3v18"/>',
    updown='<path d="m8 9 4-4 4 4M16 15l-4 4-4-4"/>',
    search='<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    globe='<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20"/>',
    bell='<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.9 1.9 0 0 0 3.4 0"/>',
    back='<path d="M19 12H5M11 18l-6-6 6-6"/>',
    arrow='<path d="M5 12h14M13 6l6 6-6 6"/>',
    chevr='<path d="m9 6 6 6-6 6"/>', chevd='<path d="m6 9 6 6 6-6"/>', chevl='<path d="m15 6-6 6 6 6"/>',
    check='<path d="M20 6 9 17l-5-5"/>',
    lock='<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    layers='<path d="m12 2 10 5-10 5L2 7l10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>',
    clock='<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    task='<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>',
    play='<path d="M6 4v16l14-8z" fill="currentColor" stroke="none"/>',
    pause='<path d="M7 4h3v16H7zM14 4h3v16h-3z" fill="currentColor" stroke="none"/>',
    slides='<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/>',
    text='<path d="M4 6h16M4 12h16M4 18h10"/>',
    quiz='<circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3M12 17h.01"/>',
    dl='<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/>',
    user='<circle cx="12" cy="8" r="4"/><path d="M4 21v-1a6 6 0 0 1 6-6h4a6 6 0 0 1 6 6v1"/>',
    users='<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    cal='<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    flag='<path d="M4 22V4M4 4h12l-2 4 2 4H4"/>',
    info='<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
    alert='<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0zM12 9v4M12 17h.01"/>',
    list='<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
    note='<path d="M12 20h9M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>',
    bookmark='<path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>',
    volume='<path d="M11 5 6 9H2v6h4l5 4zM15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14"/>',
    full='<path d="M8 3H5a2 2 0 0 0-2 2v3M21 8V5a2 2 0 0 0-2-2h-3M3 16v3a2 2 0 0 0 2 2h3M16 21h3a2 2 0 0 0 2-2v-3"/>',
    cc='<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M10 10.5a2 2 0 1 0 0 3M17 10.5a2 2 0 1 0 0 3"/>',
    paperclip='<path d="m21.4 11-9.2 9.2a6 6 0 0 1-8.5-8.5l9.2-9.2a4 4 0 0 1 5.7 5.7L9.4 17.4a2 2 0 0 1-2.8-2.8l8.5-8.5"/>',
    send='<path d="M22 2 11 13M22 2l-7 20-4-9-9-4z"/>',
    eye='<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    target='<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    award='<circle cx="12" cy="9" r="6"/><path d="M8.2 13.9 7 22l5-3 5 3-1.2-8.1"/>',
    shield='<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    bold='<path d="M6 4h8a4 4 0 0 1 0 8H6zM6 12h9a4 4 0 0 1 0 8H6z"/>',
    dots='<circle cx="5" cy="12" r="1.2"/><circle cx="12" cy="12" r="1.2"/><circle cx="19" cy="12" r="1.2"/>',
    save='<path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/><path d="M17 21v-8H7v8M7 3v5h8"/>',
    exit='<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"/>',
)


def ic(name, cls="ic", style=""):
    st = f' style="{style}"' if style else ""
    return f'<svg class="{cls}" viewBox="0 0 24 24"{st}>{ICONS[name]}</svg>'


BASE_CSS = """
:root{
  --sb:#071230;--sb-text:#B4BED6;--sb-dim:#6F7C9C;--sb-line:#16244A;
  --bg:#F3F5F9;--card:#FFFFFF;--line:#E3E8F1;--line-2:#EDF0F5;--grid:#E6EAF2;--soft:#F8FAFC;
  --ink:#0B1324;--text:#1F2A44;--muted:#5B6782;--subtle:#8A94AB;
  --navy-900:#0B1A3F;--navy-800:#12275A;--blue-700:#1E3F9A;--blue:#2550C0;--blue-500:#3B6CE0;--blue-300:#9DB8F5;--blue-100:#DCE6FB;--blue-50:#EEF3FD;
  --green:#0E7A52;--green-100:#CBE8D9;--green-50:#E5F4EC;--amber:#B7791F;--amber-100:#F1D9B5;--amber-50:#FCF1E1;--red:#B4232F;--red-100:#F0C9CD;--red-50:#FBEDEE;
  --sh:0 0 0 1px var(--line),0 1px 2px rgba(11,26,63,.04);
  --sh-lg:0 0 0 1px var(--line),0 12px 32px -12px rgba(11,26,63,.18);
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,system-ui,sans-serif;font-feature-settings:"cv11";background:var(--sb);color:var(--text);font-size:14px;line-height:1.45;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
svg{display:block}
.ic{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;flex:none}
.num{font-variant-numeric:tabular-nums}
.app{display:grid;grid-template-columns:240px 1fr;width:1440px;min-height:100vh}
.app.focus{grid-template-columns:1fr}
/* sidebar */
.sb{display:flex;flex-direction:column;padding:18px 12px 16px;color:var(--sb-text)}
.brand{display:flex;align-items:center;gap:10px;padding:0 6px 22px}
.mark{width:32px;height:32px;border-radius:9px;background:linear-gradient(140deg,#3B6CE0,#1E3F9A);display:grid;place-items:center;color:#fff;font-weight:800;font-size:15px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.14);flex:none}
.brand .t{line-height:1.15}
.brand b{color:#fff;font-size:14.5px;font-weight:700}
.brand small{display:block;font-size:11.5px;color:var(--sb-dim);font-weight:500}
.brand>.ic{margin-left:auto;color:var(--sb-dim)}
.grp{font-size:11px;font-weight:600;letter-spacing:.08em;color:var(--sb-dim);padding:18px 10px 8px}
.nv{display:flex;align-items:center;gap:10px;height:36px;padding:0 10px;border-radius:9px;font-size:13.5px;font-weight:500;margin-bottom:2px}
.nv .ic{color:var(--sb-dim)}
.nv.on{color:#fff;background:rgba(59,108,224,.2);box-shadow:inset 0 0 0 1px rgba(157,184,245,.16)}
.nv.on .ic{color:var(--blue-300)}
.cnt{margin-left:auto;min-width:20px;height:20px;padding:0 6px;border-radius:99px;background:var(--blue);color:#fff;font-size:11px;font-weight:600;display:grid;place-items:center}
.sb-b{margin-top:auto}
.me{display:flex;align-items:center;gap:10px;padding:14px 8px 0;margin-top:12px;border-top:1px solid var(--sb-line)}
.me b{display:block;color:#fff;font-size:13.5px;font-weight:600;line-height:1.25}
.me span span{font-size:12px;color:var(--sb-dim)}
.me>.ic{margin-left:auto;color:var(--sb-dim)}
.av{width:32px;height:32px;border-radius:50%;background:var(--green);color:#fff;font-size:12px;font-weight:700;display:grid;place-items:center;flex:none}
.av.sm{width:26px;height:26px;font-size:10.5px}
.av.lg{width:44px;height:44px;font-size:15px}
.av.blue{background:var(--blue)}.av.navy{background:var(--navy-800)}.av.amber{background:var(--amber)}
/* panel + header */
.panel{background:var(--bg);margin:8px 8px 8px 0;border-radius:16px;overflow:hidden;min-width:0}
.focus .panel{margin:8px}
.hd{display:flex;align-items:center;gap:10px;height:64px;padding:0 24px;border-bottom:1px solid var(--line);background:#FAFBFD}
.hd h1{font-size:15px;font-weight:600;color:var(--ink);white-space:nowrap}
.crumb{display:flex;align-items:center;gap:6px;font-size:13.5px;color:var(--muted);white-space:nowrap}
.crumb .ic{width:14px;height:14px;color:var(--subtle)}
.crumb b{color:var(--ink);font-weight:600}
.bk{width:34px;height:34px;border-radius:9px;background:#fff;box-shadow:var(--sh);display:grid;place-items:center;color:var(--ink);flex:none}
.bk .ic{width:16px;height:16px}
.search{margin-left:auto;width:300px;height:38px;border-radius:10px;background:#fff;box-shadow:var(--sh);display:flex;align-items:center;gap:10px;padding:0 6px 0 12px;color:var(--subtle);font-size:13.5px}
.search .ic{width:16px;height:16px}
.search kbd{margin-left:auto;font:600 11px Inter;color:var(--muted);background:var(--bg);box-shadow:inset 0 0 0 1px var(--line);border-radius:6px;padding:3px 7px}
.ib{height:38px;min-width:38px;padding:0 10px;border-radius:10px;background:#fff;box-shadow:var(--sh);display:inline-flex;align-items:center;justify-content:center;gap:6px;font-size:13px;font-weight:600;color:var(--ink);position:relative}
.ib .ic{color:var(--muted)}
.ib .dot{position:absolute;top:8px;right:9px;width:7px;height:7px;border-radius:50%;background:var(--red);box-shadow:0 0 0 2px #fff}
.ml{margin-left:auto}
/* layout */
.ct{padding:24px;display:grid;gap:16px;align-items:start}
.two{grid-template-columns:1fr 348px}
.col{display:grid;gap:16px;min-width:0;align-content:start}
.card{background:var(--card);border-radius:14px;box-shadow:var(--sh)}
.ch{display:flex;align-items:center;gap:12px;padding:16px 20px}
.ch h3{font-size:14.5px;font-weight:600;color:var(--ink)}
.ch .lnk{margin-left:auto;font-size:13px;font-weight:600;color:var(--blue)}
.bt{border-top:1px solid var(--line)}
.cap{font-size:11px;font-weight:600;letter-spacing:.07em;color:var(--muted);text-transform:uppercase}
.mut{color:var(--muted)}
/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:38px;padding:0 16px;border-radius:10px;font-weight:600;font-size:13.5px;white-space:nowrap}
.btn .ic{width:16px;height:16px}
.b-pri{background:var(--blue);color:#fff;box-shadow:inset 0 1px 0 rgba(255,255,255,.14),0 4px 10px -4px rgba(37,80,192,.55)}
.b-white{background:#fff;color:var(--ink);box-shadow:var(--sh)}
.b-ghost{color:var(--muted)}
.b-sm{height:32px;padding:0 12px;font-size:13px;border-radius:8px}
.b-dis{background:#E9EDF4;color:var(--subtle);box-shadow:none}
/* status pills */
.st{display:inline-flex;align-items:center;gap:7px;height:24px;padding:0 9px;border-radius:7px;background:#fff;box-shadow:inset 0 0 0 1px var(--line),0 1px 1px rgba(11,26,63,.04);font-size:12px;font-weight:600;color:var(--ink);white-space:nowrap}
.st i{width:8px;height:8px;border-radius:50%;box-shadow:inset 0 0 0 2px currentColor;flex:none}
.st.blue i{color:var(--blue)}.st.green i{color:var(--green);background:var(--green)}.st.amber i{color:var(--amber)}.st.red i{color:var(--red)}.st.gray i{color:var(--subtle)}
.tag{display:inline-flex;align-items:center;height:22px;padding:0 8px;border-radius:6px;font-size:11.5px;font-weight:600;white-space:nowrap}
.t-blue{background:var(--blue-50);color:var(--blue)}.t-green{background:var(--green-50);color:var(--green)}.t-amber{background:var(--amber-50);color:var(--amber)}.t-gray{background:var(--bg);color:var(--muted);box-shadow:inset 0 0 0 1px var(--line)}.t-red{background:var(--red-50);color:var(--red)}
.cl{display:inline-flex;align-items:center;gap:4px;height:20px;padding:0 6px;border-radius:5px;background:var(--bg);font-size:11.5px;font-weight:600;color:var(--muted)}
.cl .ic{width:11px;height:11px}
.seg{display:inline-flex;padding:3px;border-radius:9px;background:var(--bg);box-shadow:inset 0 0 0 1px var(--line)}
.seg span{height:28px;padding:0 10px;border-radius:7px;font-size:12.5px;font-weight:500;color:var(--muted);display:inline-flex;align-items:center;gap:5px}
.seg span em{font-style:normal;color:var(--subtle)}
.seg .on{background:#fff;color:var(--ink);box-shadow:0 1px 2px rgba(11,26,63,.1),0 0 0 1px var(--line)}
.utabs{display:flex;gap:24px;padding:0 20px;border-bottom:1px solid var(--line)}
.utabs span{display:inline-flex;align-items:center;gap:7px;height:44px;font-size:13.5px;font-weight:500;color:var(--muted);border-bottom:2px solid transparent;margin-bottom:-1px}
.utabs span .ic{width:16px;height:16px}
.utabs span em{font-style:normal;color:var(--subtle)}
.utabs .on{color:var(--blue);border-color:var(--blue);font-weight:600}
.utabs .on em{color:var(--blue)}
.bar{height:6px;border-radius:99px;background:var(--line-2);overflow:hidden}
.bar i{display:block;height:100%;border-radius:99px;background:var(--blue)}
.bar.g i{background:var(--green)}
.alert{display:flex;gap:10px;padding:10px 12px;border-radius:10px;font-size:13px;line-height:1.45}
.alert .ic{width:16px;height:16px;margin-top:1px}
.a-red{background:var(--red-50);box-shadow:inset 0 0 0 1px var(--red-100);color:#7A1F27}.a-red .ic{color:var(--red)}
.a-blue{background:var(--blue-50);box-shadow:inset 0 0 0 1px var(--blue-100);color:#1B2F6B}.a-blue .ic{color:var(--blue)}
.a-amber{background:var(--amber-50);box-shadow:inset 0 0 0 1px var(--amber-100);color:#6B4610}.a-amber .ic{color:var(--amber)}
.alert b{font-weight:600}
.kvrow{display:grid;grid-template-columns:120px 1fr;gap:10px 12px;align-items:center;font-size:13px}
.kvrow dt{display:flex;align-items:center;gap:8px;color:var(--muted)}
.kvrow dt .ic{width:15px;height:15px;color:var(--subtle)}
.kvrow dd{color:var(--ink);font-weight:500}
.fileic{width:34px;height:40px;border-radius:5px;background:linear-gradient(180deg,#F3F5F9,#E6EAF2);box-shadow:inset 0 0 0 1px var(--line);display:flex;align-items:flex-end;justify-content:center;padding-bottom:5px;font-size:8.5px;font-weight:700;color:var(--muted);letter-spacing:.03em;flex:none}
.fileic.pdf{color:var(--red)}.fileic.doc{color:var(--blue)}.fileic.ppt{color:var(--amber)}
.dotc{width:28px;height:28px;border-radius:50%;display:grid;place-items:center;font-size:12px;font-weight:700;box-shadow:inset 0 0 0 1.5px var(--line);color:var(--muted);background:#fff;flex:none}
.dotc.done{box-shadow:inset 0 0 0 1.5px var(--green);color:var(--green);background:var(--green-50)}
.dotc.cur{background:var(--blue);color:#fff;box-shadow:none}
.dotc .ic{width:14px;height:14px;stroke-width:2.4}
"""

NAV = [
    (None, [("home", "Asosiy sahifa", "home")]),
    ("OʻQUV", [("book", "Mening kurslarim", "courses"), ("chart", "Natijalarim", "results")]),
    ("MULOQOT", [("video", "Videokonferensiyalar", "video"), ("chat", "Chat", "chat"), ("forum", "Forum", "forum")]),
    ("RESURSLAR", [("lib", "Kutubxona", "library"), ("file", "Arizalar", "apps")]),
]


def sidebar(active):
    out = ['<aside class="sb" aria-label="Yon panel">',
           f'<div class="brand"><span class="mark">R</span><span class="t"><b>Raqamli Malaka</b><small>Oshirish platformasi</small></span>{ic("panel")}</div>']
    for grp, items in NAV:
        if grp:
            out.append(f'<div class="grp">{grp}</div>')
        for icon, label, key in items:
            on = ' on" aria-current="page' if key == active else ''
            extra = '<span class="cnt">2</span>' if key == "chat" else ''
            out.append(f'<a class="nv{on}">{ic(icon)}{label}{extra}</a>')
    out.append(f'<div class="sb-b"><a class="nv">{ic("help")}Yordam markazi</a>'
               f'<div class="me"><span class="av">BS</span><span><b>Baxtiyorov Sarvar</b><span>Tinglovchi</span></span>{ic("updown")}</div></div></aside>')
    return "\n".join(out)


def tools(search=True):
    s = f'<div class="search" role="search">{ic("search")}Kurs, dars yoki kitob qidirish<kbd>Ctrl K</kbd></div>' if search else '<span class="ml"></span>'
    return (s + f'<span class="ib">{ic("globe")}UZ</span>'
            f'<span class="ib" aria-label="Bildirishnomalar">{ic("bell")}<span class="dot"></span></span>')


def page(title, header, body, css="", active=None, focus=False):
    sb = "" if focus else sidebar(active)
    return f"""<!doctype html>
<html lang="uz">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Raqamli Malaka</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{BASE_CSS}{css}</style>
</head>
<body>
<div class="app{' focus' if focus else ''}">
{sb}
<div class="panel">
<header class="hd">{header}</header>
{body}
</div>
</div>
</body>
</html>
"""
