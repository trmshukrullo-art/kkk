/* N harfi sayohati — 1-sinf, Alifbe, 9-dars: [n] tovushi. N n harfi */
(function () {
  'use strict';

  const A = window.ART;
  const app = document.getElementById('app');
  const stage = document.getElementById('stage');
  const fx = document.getElementById('fx');
  const titleEl = document.getElementById('title');
  const starsEl = document.getElementById('stars');
  const homeBtn = document.getElementById('homeBtn');
  const soundBtn = document.getElementById('soundBtn');

  const state = { stars: [false, false, false, false, false], muted: false };

  const PRAISE = ['Barakalla!', 'Ofarin!', 'Zo‘r!', 'Qoyil!', 'Juda yaxshi!', 'Ajoyib!', 'To‘g‘ri!'];
  const TRY = ['Yana urinib ko‘r!', 'Shoshilma, yaxshilab qara!', 'Deyarli! Yana bir bor!'];
  const COLORS = ['#FF6B6B', '#FFB020', '#4CC9F0', '#7B61FF', '#2DBE6C', '#FF7EB6', '#3A86FF'];

  /* ================= Yordamchi funksiyalar ================= */
  const el = (tag, cls, html) => {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  };
  const pick = (a) => a[(Math.random() * a.length) | 0];
  const shuffle = (src) => {
    const a = [...src];
    for (let i = a.length - 1; i > 0; i--) {
      const j = (Math.random() * (i + 1)) | 0;
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  };
  const remPx = () => parseFloat(getComputedStyle(document.documentElement).fontSize) || 16;
  const hlN = (w) => w.replace(/n/gi, (m) => `<b class="hl">${m}</b>`);
  const plain = (html) => html.replace(/<[^>]+>/g, '');

  /* Har bir ekran o‘z taymer va tinglovchilarini "scope"da saqlaydi — ekran almashganda hammasi tozalanadi. */
  const mkScope = () => ({ alive: true, timers: [], ac: new AbortController() });
  let S = mkScope();
  function resetScope() {
    S.alive = false;
    S.timers.forEach(clearTimeout);
    S.ac.abort();
    S = mkScope();
  }
  function later(fn, ms) {
    const s = S;
    const t = setTimeout(() => { if (s.alive) fn(); }, ms);
    s.timers.push(t);
    return t;
  }
  function on(target, type, fn, opts) {
    target.addEventListener(type, fn, Object.assign({}, opts, { signal: S.ac.signal }));
  }
  function restartClass(node, cls, ms = 700) {
    node.classList.remove(cls);
    void node.offsetWidth;
    node.classList.add(cls);
    later(() => node.classList.remove(cls), ms);
  }
  const shake = (node) => restartClass(node, 'shake', 600);

  /* ================= Ovoz effektlari (WebAudio) ================= */
  const Sfx = (() => {
    let ctx = null;
    function ac() {
      if (!ctx) {
        const C = window.AudioContext || window.webkitAudioContext;
        if (!C) return null;
        try { ctx = new C(); } catch (e) { return null; }
      }
      if (ctx.state === 'suspended') ctx.resume();
      return ctx;
    }
    function tone(freq, at, dur, type = 'sine', vol = 0.16, to) {
      if (state.muted) return;
      const c = ac();
      if (!c) return;
      const o = c.createOscillator();
      const g = c.createGain();
      const t = c.currentTime + at;
      o.type = type;
      o.frequency.setValueAtTime(freq, t);
      if (to) o.frequency.exponentialRampToValueAtTime(to, t + dur);
      g.gain.setValueAtTime(0.0001, t);
      g.gain.exponentialRampToValueAtTime(vol, t + 0.02);
      g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
      o.connect(g);
      g.connect(c.destination);
      o.start(t);
      o.stop(t + dur + 0.05);
    }
    return {
      unlock: ac,
      tap: () => tone(660, 0, 0.08, 'sine', 0.08),
      pop: () => { tone(900, 0, 0.14, 'triangle', 0.2, 260); tone(1500, 0.02, 0.07, 'sine', 0.07); },
      correct: () => [523, 659, 784].forEach((fq, i) => tone(fq, i * 0.09, 0.24, 'triangle', 0.15)),
      wrong: () => { tone(320, 0, 0.16, 'sine', 0.11, 240); tone(260, 0.15, 0.22, 'sine', 0.09, 200); },
      ding: () => { tone(1047, 0, 0.32, 'sine', 0.13); tone(1568, 0.05, 0.3, 'sine', 0.05); },
      win: () => [523, 659, 784, 1047, 784, 1047].forEach((fq, i) => tone(fq, i * 0.12, 0.32, 'triangle', 0.15)),
      whoosh: () => tone(380, 0, 0.25, 'sine', 0.06, 900)
    };
  })();

  /* ================= O‘zbekcha nutq (agar brauzerda bo‘lsa) ================= */
  const TTS = (() => {
    const synth = window.speechSynthesis;
    let voice = null;
    function find() {
      if (!synth) return;
      voice = synth.getVoices().find((v) => /^uz/i.test(v.lang)) || null;
      document.body.classList.toggle('has-voice', !!voice);
    }
    if (synth) {
      find();
      synth.addEventListener && synth.addEventListener('voiceschanged', find);
    }
    return {
      ok: () => !!voice,
      say(text) {
        if (!voice || state.muted || !text) return;
        synth.cancel();
        const u = new SpeechSynthesisUtterance(plain(text));
        u.voice = voice;
        u.lang = voice.lang;
        u.rate = 0.85;
        synth.speak(u);
      },
      stop() { if (synth) synth.cancel(); }
    };
  })();

  /* ================= Vizual effektlar ================= */
  function toast(html, kind = 'good') {
    const t = el('div', 'toast ' + kind, html);
    fx.append(t);
    setTimeout(() => t.remove(), 1600);
  }
  /* Maqtov va maslahatni Nunu o‘z gap pufagida aytadi — o‘yin maydonini to‘sib qo‘ymaydi. */
  let curGuide = null;
  const praise = () => (curGuide ? curGuide.flash(pick(PRAISE), 'good') : toast(pick(PRAISE), 'good'));
  const tryAgain = (html) => (curGuide ? curGuide.flash(html || pick(TRY), 'try', 3200) : toast(html || pick(TRY), 'try'));

  function burst(x, y, color, n = 12) {
    const r = remPx();
    for (let i = 0; i < n; i++) {
      const p = el('i', 'particle');
      p.style.left = x + 'px';
      p.style.top = y + 'px';
      p.style.background = i % 3 === 0 ? '#fff' : color;
      fx.append(p);
      const a = Math.random() * Math.PI * 2;
      const d = r * (2.5 + Math.random() * 4);
      p.animate(
        [{ transform: 'translate(0,0) scale(1)', opacity: 1 },
          { transform: `translate(${Math.cos(a) * d}px,${Math.sin(a) * d}px) scale(.2)`, opacity: 0 }],
        { duration: 550 + Math.random() * 300, easing: 'cubic-bezier(.2,.8,.3,1)' }
      ).onfinish = () => p.remove();
    }
  }
  function burstAt(node, color) {
    const b = node.getBoundingClientRect();
    burst(b.left + b.width / 2, b.top + b.height / 2, color || pick(COLORS));
  }

  function confetti(n = 70) {
    const W = innerWidth, H = innerHeight;
    for (let i = 0; i < n; i++) {
      const c = el('i', 'confetti');
      c.style.left = Math.random() * W + 'px';
      c.style.background = pick(COLORS);
      if (i % 3 === 0) c.style.borderRadius = '50%';
      fx.append(c);
      c.animate(
        [{ transform: 'translate(0,0) rotate(0deg)' },
          { transform: `translate(${(Math.random() - 0.5) * 240}px, ${H + 60}px) rotate(${Math.random() * 900}deg)` }],
        { duration: 2000 + Math.random() * 1800, delay: Math.random() * 600, easing: 'cubic-bezier(.3,.5,.6,1)', fill: 'backwards' }
      ).onfinish = () => c.remove();
    }
  }

  /* Elementning nusxasini bir joydan ikkinchisiga "uchirib" olib borish. */
  function flyClone(from, to, dur = 420) {
    const a = from.getBoundingClientRect();
    const b = to.getBoundingClientRect();
    const c = from.cloneNode(true);
    c.classList.add('fly');
    c.classList.remove('dragging', 'hint', 'shake');
    Object.assign(c.style, {
      position: 'fixed', left: a.left + 'px', top: a.top + 'px',
      width: a.width + 'px', height: a.height + 'px', margin: '0', transform: 'none'
    });
    fx.append(c);
    const dx = b.left + b.width / 2 - (a.left + a.width / 2);
    const dy = b.top + b.height / 2 - (a.top + a.height / 2);
    const sc = Math.min(b.width / a.width, b.height / a.height, 1.15);
    return new Promise((res) => {
      c.animate(
        [{ transform: 'translate(0,0) scale(1)', opacity: 1 },
          { transform: `translate(${dx}px,${dy}px) scale(${sc})`, opacity: 0.9 }],
        { duration: dur, easing: 'cubic-bezier(.5,0,.3,1)', fill: 'forwards' }
      ).onfinish = () => { c.remove(); res(); };
    });
  }

  /* Sudrab olib borish (barmoq/sichqoncha). Kichik harakat — bosish deb hisoblanadi. */
  function draggable(node, opt) {
    let id = null, sx = 0, sy = 0, drag = false;
    const hit = (e) => opt.targets().find((t) => {
      const r = t.getBoundingClientRect();
      return e.clientX >= r.left && e.clientX <= r.right && e.clientY >= r.top && e.clientY <= r.bottom;
    });
    on(node, 'pointerdown', (e) => {
      if (id !== null || node.classList.contains('used')) return;
      e.preventDefault();
      id = e.pointerId; sx = e.clientX; sy = e.clientY; drag = false;
      try { node.setPointerCapture(id); } catch (err) { /* e’tiborsiz */ }
    });
    on(node, 'pointermove', (e) => {
      if (e.pointerId !== id) return;
      const dx = e.clientX - sx, dy = e.clientY - sy;
      if (!drag && Math.hypot(dx, dy) > 12) { drag = true; node.classList.add('dragging'); }
      if (drag) {
        node.style.transform = `translate(${dx}px,${dy}px) scale(1.08)`;
        const t = hit(e);
        opt.targets().forEach((x) => x.classList.toggle('over', x === t));
      }
    });
    const end = (e) => {
      if (e.pointerId !== id) return;
      id = null;
      opt.targets().forEach((x) => x.classList.remove('over'));
      if (!drag) { opt.onTap && opt.onTap(node); return; }
      node.classList.remove('dragging');
      const t = e.type === 'pointerup' ? hit(e) : null;
      const kept = t ? opt.onDrop(t, node) : false;
      if (!kept) snapBack(node);
    };
    on(node, 'pointerup', end);
    on(node, 'pointercancel', end);
  }
  function snapBack(node) {
    const cur = node.style.transform;
    node.style.transform = '';
    if (cur) node.animate([{ transform: cur }, { transform: 'translate(0,0) scale(1)' }], { duration: 300, easing: 'cubic-bezier(.3,1.5,.5,1)' });
  }

  /* Bola uzoq vaqt hech narsa qilmasa — to‘g‘ri javobga ishora beriladi. */
  function idleHint(root, fn, ms = 8000) {
    const s = S;
    let t;
    const reset = () => {
      clearTimeout(t);
      t = setTimeout(() => { if (s.alive) { fn(); reset(); } }, ms);
      s.timers.push(t);
    };
    on(root, 'pointerdown', reset);
    reset();
    return reset;
  }
  const hint = (node) => node && restartClass(node, 'hint', 3200);

  /* ================= Umumiy interfeys qismlari ================= */
  function guide(html, speech) {
    const g = el('div', 'guide');
    g.innerHTML = `<div class="guide-mascot mascot">${A.mascot()}</div>
      <div class="bubble"><p></p><button class="say" type="button" aria-label="Qayta tinglash">${A.icon.speaker}</button></div>`;
    const p = g.querySelector('p');
    const bubble = g.querySelector('.bubble');
    let base = html, flashT = null;
    g.set = (h, sp) => {
      base = h;
      clearTimeout(flashT);
      bubble.classList.remove('good', 'try');
      p.innerHTML = h;
      restartClass(bubble, 'pop-in', 500);
      g.speech = sp || plain(h);
      later(() => TTS.say(g.speech), 250);
    };
    g.flash = (h, kind, ms = 2000) => {
      clearTimeout(flashT);
      bubble.classList.remove('good', 'try');
      bubble.classList.add(kind);
      p.innerHTML = h;
      restartClass(bubble, 'pop-in', 500);
      TTS.say(h);
      flashT = later(() => {
        bubble.classList.remove('good', 'try');
        p.innerHTML = base;
      }, ms);
    };
    on(g.querySelector('.say'), 'click', () => TTS.say(g.speech));
    g.set(html, speech);
    curGuide = g;
    return g;
  }
  function react(kind) {
    stage.querySelectorAll('.guide .mascot, .map-mascot').forEach((m) => restartClass(m, kind, 900));
  }
  function progress(n) {
    const p = el('div', 'prog');
    for (let i = 0; i < n; i++) p.append(el('i', '', A.icon.star));
    return {
      el: p,
      set(k) {
        [...p.children].forEach((c, i) => {
          const was = c.classList.contains('on');
          c.classList.toggle('on', i < k);
          if (!was && i < k) restartClass(c, 'pop', 500);
        });
      }
    };
  }
  function levelHead(root, g, prog) {
    const h = el('div', 'lvl-head');
    h.append(g);
    if (prog) h.append(prog.el);
    root.append(h);
  }

  function renderStars() {
    starsEl.innerHTML = state.stars.map((s) => `<i class="${s ? 'on' : ''}">${A.icon.star}</i>`).join('');
  }
  function renderSound() {
    soundBtn.innerHTML = state.muted ? A.icon.soundOff : A.icon.soundOn;
    soundBtn.classList.toggle('off', state.muted);
  }

  function show(name, title, build) {
    resetScope();
    TTS.stop();
    curGuide = null;
    stage.innerHTML = '';
    app.dataset.screen = name;
    titleEl.textContent = title;
    build();
  }

  /* ================= Ekranlar ================= */
  const LEVELS = [
    { key: 'shar', name: 'Harfli sharlar', color: '#FF6B6B', run: lvlBalloons },
    { key: 'yoz', name: 'Harfni yoz', color: '#FFB020', run: lvlTrace },
    { key: 'savat', name: 'Tovush savati', color: '#2DBE6C', run: lvlBasket },
    { key: 'qoy', name: 'Harfni qo‘y', color: '#4C8DFF', run: lvlMissing },
    { key: 'soz', name: 'So‘z yasa', color: '#9B6BFF', run: lvlSyllable }
  ];

  function startScreen() {
    show('start', '', () => {
      const w = el('div', 'start');
      const letters = 'NnNnNnNnNn'.split('').map((c, i) => `<span style="--i:${i}">${c}</span>`).join('');
      w.innerHTML = `<div class="float-letters" aria-hidden="true">${letters}</div>
        <div class="start-card">
          <div class="lesson-tag">Alifbe · 9-dars</div>
          <h1>N harfi <span>sayohati</span></h1>
          <p class="sub"><b class="hl">[n]</b> tovushi. <b class="hl">N n</b> harfi</p>
          <div class="start-hero">
            <div class="start-mascot mascot">${A.mascot()}</div>
            <div class="start-bubble">Salom! Men <b class="hl">Nunu</b>.<br>Keling, <b class="hl">N</b> harfi bilan do‘stlashamiz!</div>
          </div>
          <button class="btn btn-play" type="button">${A.icon.play}<span>Boshlash</span></button>
        </div>`;
      stage.append(w);
      on(w.querySelector('.btn-play'), 'click', () => {
        Sfx.unlock();
        Sfx.tap();
        mapScreen();
      });
    });
  }

  function smoothPath(p) {
    let d = `M${p[0][0]} ${p[0][1]}`;
    for (let i = 0; i < p.length - 1; i++) {
      const p0 = p[i - 1] || p[i], p1 = p[i], p2 = p[i + 1], p3 = p[i + 2] || p2;
      const c1 = [p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6];
      const c2 = [p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6];
      d += ` C${c1[0]} ${c1[1]} ${c2[0]} ${c2[1]} ${p2[0]} ${p2[1]}`;
    }
    return d;
  }

  function mapScreen() {
    show('map', 'Sayohat xaritasi', () => {
      const next = state.stars.findIndex((s) => !s);
      const allDone = next === -1;
      const m = el('div', 'map');
      const board = el('div', 'map-board');
      m.append(board);
      stage.append(m);

      const portrait = board.clientHeight > board.clientWidth * 1.05;
      const pts = portrait
        ? [[26, 88], [72, 71], [30, 53], [70, 35], [34, 16]]
        : [[9, 72], [29, 34], [50, 68], [70, 32], [90, 64]];
      const d = smoothPath(pts);
      board.innerHTML = `<svg class="map-path" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
        <path d="${d}" class="road"/><path d="${d}" class="road-dash"/></svg>`;

      LEVELS.forEach((L, i) => {
        const done = state.stars[i];
        const locked = !done && !allDone && i !== next;
        const b = el('button', 'station' + (done ? ' done' : '') + (i === next ? ' current' : '') + (locked ? ' locked' : ''));
        b.type = 'button';
        b.style.left = pts[i][0] + '%';
        b.style.top = pts[i][1] + '%';
        b.style.setProperty('--c', L.color);
        b.setAttribute('aria-label', `${i + 1}-bekat: ${L.name}`);
        b.innerHTML = `<span class="st-ico">${A.station[i]}</span><span class="st-num">${i + 1}</span>
          ${done ? `<span class="st-star">${A.icon.star}</span>` : ''}
          ${locked ? `<span class="st-lock">${A.icon.lock}</span>` : ''}
          <span class="st-label">${L.name}</span>`;
        on(b, 'click', () => {
          if (locked) {
            Sfx.wrong();
            shake(b);
            hint(board.querySelector('.station.current'));
            return;
          }
          Sfx.tap();
          startLevel(i);
        });
        board.append(b);
      });

      const mi = allDone ? 4 : next;
      const mm = el('div', 'map-mascot mascot', A.mascot());
      mm.style.left = pts[mi][0] + '%';
      mm.style.top = pts[mi][1] + '%';
      if (pts[mi][0] < 20) mm.classList.add('right');
      board.append(mm);

      let tip;
      if (next === 0) tip = 'Salom! Men <b class="hl">Nunu</b>. <b>1</b>-bekatni bos — sayohat boshlanadi!';
      else if (allDone) tip = 'Hamma bekatlardan o‘tding! Mukofotingni ol!';
      else tip = `${pick(PRAISE)} Endi <b>${next + 1}</b>-bekatga o‘tamiz!`;
      const g = guide(tip);
      g.classList.add('map-guide');
      curGuide = null;
      if (allDone) {
        const btn = el('button', 'btn btn-prize', `${A.icon.star}<span>Mukofot</span>`);
        btn.type = 'button';
        on(btn, 'click', () => { Sfx.tap(); finishScreen(); });
        g.append(btn);
      }
      m.append(g);
    });
  }

  function startLevel(i) {
    const L = LEVELS[i];
    show('level', `${i + 1}. ${L.name}`, () => {
      const root = el('div', 'level lvl-' + L.key);
      stage.append(root);
      L.run(root, () => levelDone(i));
    });
  }

  function levelDone(i) {
    state.stars[i] = true;
    const all = state.stars.every(Boolean);
    Sfx.win();
    confetti(50);
    react('happy');
    const ov = el('div', 'overlay');
    ov.innerHTML = `<div class="win-card">
        <div class="win-mascot mascot dance">${A.mascot()}</div>
        <h2>${pick(['Barakalla!', 'Ofarin!', 'Qoyil!'])}</h2>
        <p>Sen yulduzcha yutding!</p>
        <div class="win-star">${A.icon.star}</div>
        <button class="btn btn-next" type="button">${all ? A.icon.star : A.icon.arrow}<span>${all ? 'Mukofot' : 'Davom etish'}</span></button>
      </div>`;
    stage.append(ov);
    TTS.say('Barakalla! Sen yulduzcha yutding!');
    later(() => {
      const target = starsEl.children[i];
      flyClone(ov.querySelector('.win-star'), target, 700).then(() => {
        renderStars();
        restartClass(starsEl.children[i], 'pop', 500);
        Sfx.ding();
      });
    }, 900);
    on(ov.querySelector('.btn-next'), 'click', () => {
      Sfx.tap();
      renderStars();
      if (all) finishScreen(); else mapScreen();
    });
  }

  function finishScreen() {
    show('finish', 'Mukofot', () => {
      const words = [['non', 'non'], ['ona', 'ona'], ['anor', 'anor'], ['ninachi', 'ninachi'], ['on', 'o‘n'], ['ana', 'ana']];
      const w = el('div', 'finish');
      w.innerHTML = `<div class="finish-card">
          <div class="medal">${A.medal}</div>
          <h1>Barakalla!</h1>
          <p class="sub">Sen <b class="hl">N n</b> harfi bilan do‘stlashding!</p>
          <div class="finish-stars">${state.stars.map((_, i) => `<i style="--i:${i}">${A.icon.star}</i>`).join('')}</div>
          <p class="learned-title">Bugun o‘rgangan so‘zlarimiz:</p>
          <div class="learned">${words.map(([k, t], i) => `<div class="lw" style="--i:${i}"><div class="pic">${A.pic(k)}</div><span>${hlN(t)}</span></div>`).join('')}</div>
          <div class="finish-btns">
            <button class="btn btn-alt" type="button" data-act="again">${A.icon.again}<span>Qaytadan o‘ynash</span></button>
            <button class="btn" type="button" data-act="map">${A.icon.map}<span>Xarita</span></button>
          </div>
        </div>
        <div class="finish-mascot mascot dance">${A.mascot()}</div>`;
      stage.append(w);
      Sfx.win();
      confetti(110);
      later(() => confetti(60), 2200);
      TTS.say('Barakalla! Sen N harfi bilan do‘stlashding!');
      w.querySelectorAll('.lw').forEach((lw, i) => on(lw, 'click', () => { Sfx.tap(); restartClass(lw, 'pop', 500); TTS.say(words[i][1]); }));
      on(w.querySelector('[data-act=again]'), 'click', () => {
        Sfx.tap();
        state.stars = state.stars.map(() => false);
        renderStars();
        mapScreen();
      });
      on(w.querySelector('[data-act=map]'), 'click', () => { Sfx.tap(); mapScreen(); });
    });
  }

  /* ================= 1-bosqich: Harfli sharlar ================= */
  function lvlBalloons(root, done) {
    const NEED = 8;
    const OTHERS = ['O', 'o', 'A', 'a', 'T', 't'];
    let got = 0, finished = false, lastLanes = [];
    const g = guide('<b class="hl">N</b> va <b class="hl">n</b> harfi yozilgan sharlarni bos!', 'N va n harfi yozilgan sharlarni bos!');
    const prog = progress(NEED);
    levelHead(root, g, prog);
    const field = el('div', 'field');
    root.append(field);

    function spawn() {
      if (finished) return;
      const live = [...field.querySelectorAll('.balloon:not(.popped)')];
      const targets = live.filter((b) => b.dataset.t === '1').length;
      const maxLive = field.clientWidth > field.clientHeight ? 7 : 5;
      if (live.length < maxLive) {
        const isT = targets === 0 || Math.random() < 0.5;
        make(isT ? pick(['N', 'n']) : pick(OTHERS), isT);
      }
      later(spawn, 1000 + Math.random() * 600);
    }

    function make(ch, isT, startAt = 0) {
      const b = el('button', 'balloon');
      b.type = 'button';
      b.dataset.t = isT ? '1' : '0';
      b.dataset.ch = ch;
      const color = pick(COLORS);
      b.style.setProperty('--c', color);
      b.style.setProperty('--sway', (2.4 + Math.random() * 1.4).toFixed(2) + 's');
      b.innerHTML = `<span class="sway"><span class="b"><span class="ch">${ch}</span></span>
        <svg class="str" viewBox="0 0 20 60" aria-hidden="true"><path d="M10 0 Q2 15 10 30 T10 60"/></svg></span>`;
      field.append(b);
      const fw = field.clientWidth, fh = field.clientHeight;
      const bw = b.offsetWidth, bh = b.offsetHeight;
      const lanes = Math.max(3, Math.floor(fw / (bw * 1.2)));
      let lane, tries = 0;
      do { lane = (Math.random() * lanes) | 0; } while (lastLanes.includes(lane) && ++tries < 10);
      lastLanes = [lane, ...lastLanes].slice(0, Math.min(2, lanes - 1));
      const laneW = fw / lanes;
      b.style.left = lane * laneW + (laneW - bw) / 2 + 'px';
      const speed = fh / (8.5 + Math.random() * 3); // px/s — sekin, bolalarga qulay
      const anim = b.animate(
        [{ transform: `translateY(${fh + 10}px)` }, { transform: `translateY(${-bh - 20}px)` }],
        { duration: ((fh + bh + 30) / speed) * 1000, easing: 'linear' }
      );
      anim.currentTime = anim.effect.getTiming().duration * startAt;
      anim.onfinish = () => b.remove();
      on(b, 'pointerdown', (e) => { e.preventDefault(); hit(b, anim, color); });
    }

    function hit(b, anim, color) {
      if (b.classList.contains('popped') || finished) return;
      if (b.dataset.t === '1') {
        b.classList.add('popped');
        anim.pause();
        Sfx.pop();
        burstAt(b.querySelector('.b'), color);
        b.querySelector('.b').animate(
          [{ transform: 'scale(1)', opacity: 1 }, { transform: 'scale(1.6)', opacity: 0 }],
          { duration: 220, fill: 'forwards' }
        ).onfinish = () => b.remove();
        b.querySelector('.str').style.opacity = '0';
        got++;
        prog.set(got);
        react('happy');
        if (got % 3 === 0 && got < NEED) praise();
        if (got >= NEED) {
          finished = true;
          praise();
          later(() => field.querySelectorAll('.balloon').forEach((x) => x.classList.add('away')), 300);
          later(done, 1100);
        }
      } else {
        Sfx.wrong();
        restartClass(b, 'wobble', 700);
        react('think');
        tryAgain(`Bu — <b>${b.dataset.ch}</b> harfi. <b class="hl">N</b> ni qidir!`);
      }
    }

    idleHint(root, () => field.querySelectorAll('.balloon[data-t="1"]:not(.popped)').forEach(hint), 7000);
    // Birinchi sharlar darhol osmonda bo‘lsin
    make(pick(['N', 'n']), true, 0.45);
    make(pick(OTHERS), false, 0.3);
    make(pick(['N', 'n']), true, 0.15);
    later(spawn, 700);
  }

  /* ================= 2-bosqich: Harfni yoz (barmoq bilan chizish) ================= */
  function lvlTrace(root, done) {
    const LETTERS = [
      {
        ch: 'N',
        strokes: ['M30 18 L30 84', 'M70 18 L70 84', 'M30 18 L70 84'],
        text: 'Barmog‘ing bilan katta <b class="hl">N</b> ni yoz. Yashil nuqtadan boshla!',
        speech: 'Barmog‘ing bilan katta N harfini yoz. Yashil nuqtadan boshla!'
      },
      {
        ch: 'n',
        strokes: ['M36 42 L36 84', 'M36 58 C36 46 43 41 51 41 C60 41 66 46 66 57 L66 84'],
        text: 'Endi kichik <b class="hl">n</b> ni yoz: avval tayoqcha, keyin ko‘prikcha!',
        speech: 'Endi kichik n harfini yoz. Avval tayoqcha, keyin ko‘prikcha!'
      }
    ];
    const g = guide(LETTERS[0].text, LETTERS[0].speech);
    const prog = progress(LETTERS.length);
    levelHead(root, g, prog);

    const wrap = el('div', 'trace-wrap');
    wrap.innerHTML = `<div class="letter-tabs">${LETTERS.map((L, i) => `<div class="ltab" data-i="${i}">${L.ch}</div>`).join('')}</div>
      <div class="board"><svg class="trace-svg" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid meet"></svg></div>
      <div class="poem"><div class="poem-pic">${A.station[1]}</div><p>“<b class="hl">N</b>”ni yasamoq oson,<br>Diqqat bilan qaragin.<br>Ikki ustun oralab,<br>Qiya ustun tiragin.</p></div>`;
    root.append(wrap);
    const svgEl = wrap.querySelector('svg');
    const NS = 'http://www.w3.org/2000/svg';
    const mk = (tag, attrs) => {
      const n = document.createElementNS(NS, tag);
      for (const k in attrs) n.setAttribute(k, attrs[k]);
      return n;
    };

    let li = 0, si = 0, cps = [], idx = 0, len = 0, tracking = false, pid = null, ink = null, inkPts = [];
    let gFill, gActive, startDot, startNum;
    const TOL = 9;

    function setTabs() {
      wrap.querySelectorAll('.ltab').forEach((t, i) => {
        t.classList.toggle('active', i === li);
        t.classList.toggle('done', i < li);
      });
    }

    function drawLetter() {
      const L = LETTERS[li];
      svgEl.innerHTML = '';
      const lines = mk('g', { class: 'lines' });
      [[18, 'solid'], [41, 'dash'], [84, 'solid']].forEach(([y, t]) => lines.append(mk('line', { x1: 4, x2: 96, y1: y, y2: y, class: 'ln ' + t })));
      svgEl.append(lines);
      const base = mk('g', { class: 'g-base' });
      L.strokes.forEach((d) => base.append(mk('path', { d })));
      svgEl.append(base);
      svgEl.append(mk('g', { class: 'g-done' }));
      gActive = mk('g', { class: 'g-active' });
      svgEl.append(gActive);
      ink = mk('polyline', { class: 'ink', points: '' });
      svgEl.append(ink);
      si = 0;
      setTabs();
      setStroke();
    }

    function setStroke() {
      const d = LETTERS[li].strokes[si];
      gActive.innerHTML = '';
      gActive.append(mk('path', { d, class: 'g-dash' }));
      gFill = mk('path', { d, class: 'g-fill' });
      gActive.append(gFill);
      len = gFill.getTotalLength();
      gFill.style.strokeDasharray = `${len} ${len}`;
      gFill.style.strokeDashoffset = len;
      cps = [];
      for (let s = 0; s < len; s += 2.5) cps.push(gFill.getPointAtLength(s));
      cps.push(gFill.getPointAtLength(len));
      idx = 0;
      const mover = mk('circle', { r: 2.6, class: 'mover' });
      const am = mk('animateMotion', { dur: Math.max(1.4, len / 40) + 's', repeatCount: 'indefinite', path: d });
      mover.append(am);
      gActive.append(mover);
      const p0 = cps[0];
      startDot = mk('circle', { cx: p0.x, cy: p0.y, r: 5.2, class: 'start-dot' });
      startNum = mk('text', { x: p0.x, y: p0.y + 2.2, class: 'start-num' });
      startNum.textContent = si + 1;
      gActive.append(startDot, startNum);
    }

    function moveStart() {
      const p = cps[Math.min(idx, cps.length - 1)];
      startDot.setAttribute('cx', p.x); startDot.setAttribute('cy', p.y);
      startNum.setAttribute('x', p.x); startNum.setAttribute('y', p.y + 2.2);
    }

    const toSvg = (e) => {
      const pt = svgEl.createSVGPoint();
      pt.x = e.clientX; pt.y = e.clientY;
      return pt.matrixTransform(svgEl.getScreenCTM().inverse());
    };
    const dist = (a, b) => Math.hypot(a.x - b.x, a.y - b.y);

    function advance(p) {
      let hitAny = false;
      const end = Math.min(idx + 6, cps.length - 1);
      for (let k = idx; k <= end; k++) {
        if (dist(p, cps[k]) < TOL) { idx = k + 1; hitAny = true; }
      }
      if (!hitAny && idx > 0 && dist(p, cps[idx - 1]) > TOL * 2.4) tracking = false;
      gFill.style.strokeDashoffset = Math.max(0, len - (idx / (cps.length - 1)) * len);
      if (idx >= cps.length) strokeDone();
    }

    function strokeDone() {
      tracking = false;
      const L = LETTERS[li];
      const doneG = svgEl.querySelector('.g-done');
      doneG.append(mk('path', { d: L.strokes[si], class: 'g-solid' }));
      fadeInk();
      Sfx.ding();
      si++;
      if (si < L.strokes.length) {
        setStroke();
        return;
      }
      // Harf tayyor
      gActive.innerHTML = '';
      Sfx.correct();
      praise();
      react('happy');
      restartClass(doneG, 'letter-done', 900);
      prog.set(li + 1);
      li++;
      if (li < LETTERS.length) {
        later(() => { g.set(LETTERS[li].text, LETTERS[li].speech); drawLetter(); }, 1400);
      } else {
        setTabs();
        later(done, 1200);
      }
    }

    function fadeInk() {
      const old = ink;
      old.classList.add('fade');
      setTimeout(() => old.remove(), 500);
      ink = mk('polyline', { class: 'ink', points: '' });
      svgEl.append(ink);
      inkPts = [];
    }

    on(svgEl, 'pointerdown', (e) => {
      if (pid !== null || li >= LETTERS.length || !gFill) return;
      e.preventDefault();
      pid = e.pointerId;
      try { svgEl.setPointerCapture(pid); } catch (err) { /* e’tiborsiz */ }
      const p = toSvg(e);
      const from = cps[Math.max(0, idx - 1)];
      tracking = dist(p, from) < TOL * 1.6 || dist(p, cps[Math.min(idx, cps.length - 1)]) < TOL * 1.6;
      if (!tracking) restartClass(startDot, 'blink', 1200);
      inkPts = [`${p.x.toFixed(1)},${p.y.toFixed(1)}`];
      ink.setAttribute('points', inkPts.join(' '));
      if (tracking) advance(p);
    });
    on(svgEl, 'pointermove', (e) => {
      if (e.pointerId !== pid) return;
      const p = toSvg(e);
      inkPts.push(`${p.x.toFixed(1)},${p.y.toFixed(1)}`);
      ink.setAttribute('points', inkPts.join(' '));
      if (tracking) advance(p);
    });
    const up = (e) => {
      if (e.pointerId !== pid) return;
      pid = null;
      tracking = false;
      if (inkPts.length) fadeInk();
      if (gFill && idx > 0 && idx < cps.length) moveStart();
    };
    on(svgEl, 'pointerup', up);
    on(svgEl, 'pointercancel', up);

    idleHint(root, () => startDot && restartClass(startDot, 'blink', 1600), 6000);
    drawLetter();
  }

  /* ================= 3-bosqich: Tovush savati ================= */
  function lvlBasket(root, done) {
    const WITH_N = ['non', 'nok', 'banan', 'limon', 'anor', 'ninachi'];
    const WITHOUT_N = ['olma', 'baliq', 'quyosh', 'tarvuz', 'mushuk', 'qush'];
    const items = shuffle([
      ...shuffle(WITH_N).slice(0, 4).map((w) => ({ w, has: true })),
      ...shuffle(WITHOUT_N).slice(0, 4).map((w) => ({ w, has: false }))
    ]);
    const g = guide('Rasm nomini ayt. <b class="hl">[n]</b> tovushi bormi? Savatga sol!',
      'Rasm nomini ovoz chiqarib ayt. Unda n tovushi bormi? Rasmni savatga sol!');
    const prog = progress(items.length);
    levelHead(root, g, prog);

    const area = el('div', 'basket-area');
    area.innerHTML = `
      <div class="bask yes" role="button" aria-label="n tovushi bor">
        <div class="bask-in"></div>${A.basket}
        <div class="bask-tag"><span class="bt-letter">n</span><span class="bt-mark ok">${A.icon.check}</span></div>
        <div class="bask-label">bor</div>
      </div>
      <div class="card-slot"></div>
      <div class="bask no" role="button" aria-label="n tovushi yo‘q">
        <div class="bask-in"></div>${A.basket}
        <div class="bask-tag"><span class="bt-letter crossed">n</span></div>
        <div class="bask-label">yo‘q</div>
      </div>`;
    root.append(area);
    const yes = area.querySelector('.bask.yes');
    const no = area.querySelector('.bask.no');
    const slot = area.querySelector('.card-slot');
    let i = 0, errs = 0, busy = false, card = null;

    function showItem() {
      errs = 0;
      busy = false;
      const it = items[i];
      card = el('div', 'pic-card enter');
      card.innerHTML = `<div class="pic">${A.pic(it.w)}</div><div class="word">${hlN(it.w)}</div>`;
      slot.innerHTML = '';
      slot.append(card);
      later(() => card.classList.remove('enter'), 500);
      later(() => TTS.say(it.w), 500);
      draggable(card, {
        targets: () => [yes, no],
        onDrop: (t) => answer(t === yes),
        onTap: () => TTS.say(it.w)
      });
    }

    function answer(saidYes) {
      if (busy) return true;
      const it = items[i];
      const word = card.querySelector('.word');
      if (saidYes === it.has) {
        busy = true;
        snapBack(card);
        word.classList.add('show');
        Sfx.correct();
        react('happy');
        praise();
        TTS.say(it.w);
        const b = saidYes ? yes : no;
        b.classList.remove('hint');
        later(() => {
          const pic = card.querySelector('.pic');
          const inn = b.querySelector('.bask-in');
          flyClone(pic, inn, 450).then(() => {
            const mini = el('div', 'mini', A.pic(it.w));
            const n = inn.children.length;
            mini.style.setProperty('--x', ((n % 4) - 1.5) * 22 + '%');
            mini.style.setProperty('--r', ((n % 2 ? 1 : -1) * (6 + n * 3)) + 'deg');
            inn.append(mini);
            restartClass(b, 'bump', 500);
            Sfx.whoosh();
          });
          card.classList.add('gone');
          i++;
          prog.set(i);
          if (i < items.length) later(showItem, 650);
          else later(done, 900);
        }, 900);
        return true;
      }
      errs++;
      Sfx.wrong();
      react('think');
      word.classList.add('show');
      shake(card);
      tryAgain(it.has
        ? `Yaxshilab tingla: <b>${hlN(it.w)}</b> — <b class="hl">n</b> bor!`
        : `Yaxshilab tingla: <b>${it.w}</b> — <b class="hl">n</b> yo‘q!`);
      TTS.say(it.w);
      if (errs >= 1) hint(it.has ? yes : no);
      return false;
    }

    on(yes, 'click', () => answer(true));
    on(no, 'click', () => answer(false));
    idleHint(root, () => card && restartClass(card, 'wiggle', 1000), 9000);
    showItem();
  }

  /* ================= 4-bosqich: Tushib qolgan harfni qo‘y ================= */
  function lvlMissing(root, done) {
    const ITEMS = [
      { w: 'non', pic: 'non', i: 0 },
      { w: 'ona', pic: 'ona', i: 1 },
      { w: 'ota', pic: 'ota', i: 1 },
      { w: 'anor', pic: 'anor', i: 1 },
      { w: 'ninachi', pic: 'ninachi', i: 0 },
      { w: 'o‘n', pic: 'on', i: 2 },
      { w: 'ana', pic: 'ana', i: 1 }
    ];
    const KNOWN = ['ona', 'ota', 'ana', 'non', 'anor', 'nota', 'ot', 'on'];
    const g = guide('Rasmga qara. Tushib qolgan harfni topib, joyiga qo‘y!', 'Rasmga qara. Tushib qolgan harfni topib, joyiga qo‘y!');
    const prog = progress(ITEMS.length);
    levelHead(root, g, prog);

    const area = el('div', 'miss-area');
    area.innerHTML = `<div class="word-card"></div><div class="tiles">${['n', 'o', 'a', 't'].map((c, k) => `<button class="tile" type="button" data-ch="${c}" style="--c:${COLORS[[4, 2, 1, 3][k]]}">${c}</button>`).join('')}</div>`;
    root.append(area);
    const card = area.querySelector('.word-card');
    const tiles = [...area.querySelectorAll('.tile')];
    let k = 0, busy = false, errs = 0, slot = null;

    function showItem() {
      busy = false;
      errs = 0;
      const it = ITEMS[k];
      const chars = Array.from(it.w);
      card.innerHTML = `<div class="pic">${A.pic(it.pic)}</div>
        <div class="spell">${chars.map((ch, j) => (j === it.i ? `<span class="slot" data-ans="${ch}"></span>` : `<span class="ch">${ch}</span>`)).join('')}</div>`;
      slot = card.querySelector('.slot');
      restartClass(card, 'enter', 500);
    }

    async function tryTile(tile, dropped) {
      if (busy) return true;
      const it = ITEMS[k];
      const ch = tile.dataset.ch;
      if (ch === slot.dataset.ans) {
        busy = true;
        if (dropped) tile.style.transform = '';
        else await flyClone(tile, slot, 380);
        slot.textContent = ch;
        slot.classList.add('filled');
        card.querySelector('.spell').classList.add('solved');
        burstAt(slot, '#FFC93C');
        Sfx.correct();
        react('happy');
        praise();
        later(() => {
          card.querySelector('.spell').innerHTML = hlN(it.w);
          TTS.say(it.w);
        }, 450);
        k++;
        prog.set(k);
        if (k < ITEMS.length) later(showItem, 1700);
        else later(done, 1500);
        return true;
      }
      errs++;
      Sfx.wrong();
      react('think');
      shake(tile);
      const chars = Array.from(it.w);
      chars[it.i] = ch;
      const made = chars.join('');
      if (KNOWN.includes(made)) tryAgain(`Unda “<b>${made}</b>” bo‘lib qoladi. Rasmga qara!`);
      else tryAgain();
      if (errs >= 2) hint(tiles.find((t) => t.dataset.ch === slot.dataset.ans));
      return false;
    }

    tiles.forEach((t) => draggable(t, {
      targets: () => [card],
      onDrop: (_, node) => { tryTile(node, true); return busy; },
      onTap: (node) => { Sfx.tap(); tryTile(node, false); }
    }));
    idleHint(root, () => slot && restartClass(slot, 'hint', 3000), 8000);
    showItem();
  }

  /* ================= 5-bosqich: Bo‘g‘inlardan so‘z yasa ================= */
  function lvlSyllable(root, done) {
    const WORDS = [
      { w: 'ona', s: ['o', 'na'], x: ['a', 'ta'] },
      { w: 'ota', s: ['o', 'ta'], x: ['a', 'na'] },
      { w: 'ana', s: ['a', 'na'], x: ['o', 'no'] },
      { w: 'anor', s: ['a', 'nor'], x: ['o', 'no'] }
    ];
    const g = guide('Rasmga qara. Bo‘g‘inlarni tartib bilan qo‘yib, so‘z yasa!', 'Rasmga qara. Bo‘g‘inlarni tartib bilan qo‘yib, so‘z yasa!');
    const prog = progress(WORDS.length);
    levelHead(root, g, prog);

    const area = el('div', 'syl-area');
    area.innerHTML = `<div class="word-card syl-card"></div><div class="tiles syl-tiles"></div>`;
    root.append(area);
    const card = area.querySelector('.word-card');
    const tilesBox = area.querySelector('.syl-tiles');
    let k = 0, filled = 0, busy = false, errs = 0;

    function showItem() {
      busy = false;
      filled = 0;
      errs = 0;
      const it = WORDS[k];
      card.innerHTML = `<div class="pic">${A.pic(it.w)}</div>
        <div class="syl-build">
          <div class="syl-slots">${it.s.map((_, j) => `<span class="sslot" data-j="${j}"></span>`).join('')}</div>
          <svg class="syl-arc" viewBox="0 0 100 20" preserveAspectRatio="none" aria-hidden="true"><path d="M8 4 Q50 22 92 4"/></svg>
          <div class="syl-word"></div>
        </div>`;
      restartClass(card, 'enter', 500);
      tilesBox.innerHTML = '';
      shuffle([...it.s, ...it.x]).forEach((s, n) => {
        const t = el('button', 'tile syl', s);
        t.type = 'button';
        t.dataset.s = s;
        t.style.setProperty('--c', COLORS[(n + k) % COLORS.length]);
        tilesBox.append(t);
        draggable(t, {
          targets: () => [card],
          onDrop: (_, node) => { tryTile(node, true); return node.classList.contains('used'); },
          onTap: (node) => { Sfx.tap(); tryTile(node, false); }
        });
      });
    }

    async function tryTile(tile, dropped) {
      if (busy || tile.classList.contains('used')) return;
      const it = WORDS[k];
      const s = tile.dataset.s;
      const slot = card.querySelector(`.sslot[data-j="${filled}"]`);
      if (s === it.s[filled]) {
        busy = true;
        tile.classList.add('used');
        if (dropped) tile.style.transform = '';
        else await flyClone(tile, slot, 360);
        slot.textContent = s;
        slot.classList.add('filled');
        Sfx.ding();
        filled++;
        errs = 0;
        busy = false;
        if (filled === it.s.length) {
          busy = true;
          card.querySelector('.syl-build').classList.add('solved');
          card.querySelector('.syl-word').innerHTML = hlN(it.w);
          Sfx.correct();
          react('happy');
          praise();
          TTS.say(it.s.join('-') + '. ' + it.w);
          k++;
          prog.set(k);
          if (k < WORDS.length) later(showItem, 2000);
          else later(done, 1700);
        }
        return;
      }
      errs++;
      Sfx.wrong();
      react('think');
      shake(tile);
      if (filled === 0 && s === it.s[1]) {
        tryAgain('Bu ikkinchi bo‘g‘in. Avval birinchisini qo‘y!');
        hint(slot);
      } else {
        tryAgain();
      }
      if (errs >= 2) hint([...tilesBox.children].find((t) => t.dataset.s === it.s[filled] && !t.classList.contains('used')));
    }

    idleHint(root, () => {
      const it = WORDS[k];
      if (it) hint([...tilesBox.children].find((t) => t.dataset.s === it.s[filled] && !t.classList.contains('used')));
    }, 9000);
    showItem();
  }

  /* ================= Ishga tushirish ================= */
  homeBtn.innerHTML = A.icon.map;
  homeBtn.addEventListener('click', () => { Sfx.tap(); mapScreen(); });
  soundBtn.addEventListener('click', () => {
    state.muted = !state.muted;
    if (state.muted) TTS.stop();
    renderSound();
    Sfx.tap();
  });
  // Kontekst menyu va tasodifiy belgilashning oldini olish (planshet/doska uchun)
  document.addEventListener('contextmenu', (e) => e.preventDefault());
  document.addEventListener('pointerdown', () => Sfx.unlock(), { once: true });

  let rz;
  window.addEventListener('resize', () => {
    clearTimeout(rz);
    rz = setTimeout(() => { if (app.dataset.screen === 'map') mapScreen(); }, 250);
  });

  renderStars();
  renderSound();
  startScreen();
})();
