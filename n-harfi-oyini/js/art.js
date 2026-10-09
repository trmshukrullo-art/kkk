/* Barcha rasmlar SVG ko‘rinishida — tashqi fayllar kerak emas. */
(function () {
  'use strict';

  const svg = (inner, vb = '0 0 120 120') =>
    `<svg viewBox="${vb}" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">${inner}</svg>`;
  const shadow = (y = 110, rx = 38) => `<ellipse cx="60" cy="${y}" rx="${rx}" ry="5" fill="#000" opacity=".1"/>`;
  const f = (n) => n.toFixed(1);

  /* ---------- So‘z rasmlari ---------- */
  const PIC = {
    non() {
      let dots = '';
      for (const [r, n] of [[0, 1], [7, 6], [13.5, 11], [19.5, 15]]) {
        for (let i = 0; i < n; i++) {
          const a = (i / n) * Math.PI * 2;
          dots += `<circle cx="${f(60 + r * Math.cos(a))}" cy="${f(58 + r * Math.sin(a))}" r="1.7"/>`;
        }
      }
      let seeds = '';
      for (let i = 0; i < 18; i++) {
        const a = (i / 18) * Math.PI * 2;
        const x = 60 + 36 * Math.cos(a), y = 58 + 36 * Math.sin(a);
        seeds += `<ellipse cx="${f(x)}" cy="${f(y)}" rx="1.5" ry="2.7" transform="rotate(${Math.round((a * 180) / Math.PI + 90)} ${f(x)} ${f(y)})"/>`;
      }
      return svg(`${shadow(110, 42)}
        <circle cx="60" cy="61" r="48" fill="#A85A1C"/>
        <circle cx="60" cy="58" r="48" fill="#D98A35"/>
        <circle cx="60" cy="57" r="44" fill="#E9A44E"/>
        <circle cx="60" cy="58" r="28" fill="#BF7230"/>
        <circle cx="60" cy="58" r="25.5" fill="#F4CD8A"/>
        <g fill="#C27A30">${dots}</g>
        <g fill="#FFF3D8">${seeds}</g>
        <path d="M25 40 A40 40 0 0 1 50 17" stroke="#fff" stroke-width="5" stroke-linecap="round" fill="none" opacity=".35"/>`);
    },

    ninachi() {
      return svg(`${shadow(112, 40)}
        <g fill="#DDF3FF" stroke="#7CC4F2" stroke-width="1.6" opacity=".95">
          <ellipse cx="40" cy="33" rx="9" ry="25" transform="rotate(-18 40 33)"/>
          <ellipse cx="40" cy="87" rx="9" ry="25" transform="rotate(18 40 87)"/>
          <ellipse cx="55" cy="35" rx="8" ry="23" transform="rotate(22 55 35)"/>
          <ellipse cx="55" cy="85" rx="8" ry="23" transform="rotate(-22 55 85)"/>
        </g>
        <g stroke="#A9DBF7" stroke-width="1" fill="none">
          <path d="M42 56 L34 12"/><path d="M42 64 L34 108"/><path d="M52 56 L62 14"/><path d="M52 64 L62 106"/>
        </g>
        <rect x="50" y="56" width="60" height="8" rx="4" fill="#2FB57A"/>
        <g stroke="#1E8A5A" stroke-width="1.6"><path d="M62 56v8M72 56v8M82 56v8M92 56v8M101 57v6"/></g>
        <ellipse cx="44" cy="60" rx="11" ry="9" fill="#2A9D68"/>
        <circle cx="28" cy="60" r="10" fill="#2A9D68"/>
        <circle cx="24" cy="53" r="6.5" fill="#1D3B66"/><circle cx="24" cy="67" r="6.5" fill="#1D3B66"/>
        <circle cx="22" cy="51" r="2" fill="#fff"/><circle cx="22" cy="65" r="2" fill="#fff"/>`);
    },

    anor() {
      return svg(`${shadow(112, 36)}
        <path d="M47 28 L43 12 L53 19 L60 8 L67 19 L77 12 L73 28Z" fill="#A3122A"/>
        <circle cx="60" cy="66" r="42" fill="#B81E37"/>
        <circle cx="56" cy="62" r="38" fill="#E03149"/>
        <ellipse cx="42" cy="46" rx="10" ry="6" fill="#fff" opacity=".4" transform="rotate(-35 42 46)"/>
        <path d="M74 27 Q96 10 108 22 Q92 38 74 27Z" fill="#43A047"/>
        <path d="M77 27 Q93 20 104 22" stroke="#2E7D32" stroke-width="1.6" fill="none"/>`);
    },

    on() {
      return svg(`${shadow(108, 40)}
        <text x="60" y="94" text-anchor="middle" font-family="Nunito, 'Arial Rounded MT Bold', Arial, sans-serif"
          font-weight="900" font-size="88" letter-spacing="-4" fill="#FF8C1A" stroke="#D96A00" stroke-width="5"
          paint-order="stroke" stroke-linejoin="round">10</text>`);
    },

    ona() {
      return svg(`
        <path d="M16 120 Q20 92 60 92 Q100 92 104 120Z" fill="#E4588E"/>
        <path d="M60 14 C26 14 20 44 22 66 C24 86 30 98 38 104 L82 104 C90 98 96 86 98 66 C100 44 94 14 60 14Z" fill="#4A2A1A"/>
        <rect x="52" y="80" width="16" height="16" rx="6" fill="#EDB78F"/>
        <path d="M44 96 Q60 108 76 96" stroke="#fff" stroke-width="3" fill="none" opacity=".6"/>
        <ellipse cx="60" cy="58" rx="27" ry="30" fill="#F6C9A2"/>
        <path d="M33 58 C32 32 46 24 60 24 C76 24 88 34 87 58 C82 44 72 37 62 36 C54 40 42 45 33 58Z" fill="#4A2A1A"/>
        <path d="M44 52 Q49 49 54 52M66 52 Q71 49 76 52" stroke="#4A2A1A" stroke-width="2.2" fill="none" stroke-linecap="round"/>
        <ellipse cx="49" cy="60" rx="3.3" ry="4.2" fill="#2B1B12"/><ellipse cx="71" cy="60" rx="3.3" ry="4.2" fill="#2B1B12"/>
        <circle cx="50.2" cy="58.4" r="1.2" fill="#fff"/><circle cx="72.2" cy="58.4" r="1.2" fill="#fff"/>
        <circle cx="42" cy="70" r="5" fill="#FF9AA8" opacity=".6"/><circle cx="78" cy="70" r="5" fill="#FF9AA8" opacity=".6"/>
        <path d="M51 71 Q60 82 69 71 Q60 75 51 71Z" fill="#C9504A"/>
        <circle cx="33" cy="67" r="3" fill="#FFC93C"/><circle cx="87" cy="67" r="3" fill="#FFC93C"/>
        <path d="M100 30 C100 25 107 24 108 29 C109 24 116 25 116 30 C116 36 108 40 108 42 C108 40 100 36 100 30Z" fill="#F0505A"/>`);
    },

    ota() {
      const pep = (x, y, r) =>
        `<path transform="translate(${x} ${y}) rotate(${r})" d="M0 0 C3 -6 10 -7 9 1 C8 6 2 5 0 0Z"/>`;
      return svg(`
        <path d="M12 120 Q16 92 60 92 Q104 92 108 120Z" fill="#2F6DB5"/>
        <g stroke="#5B93D6" stroke-width="2.4"><path d="M28 100 L24 120M40 95 L38 120M80 95 L82 120M92 100 L96 120"/></g>
        <path d="M48 92 L60 110 L72 92Z" fill="#fff"/>
        <rect x="52" y="80" width="16" height="14" rx="6" fill="#DCA77A"/>
        <circle cx="33" cy="62" r="6" fill="#E3A878"/><circle cx="87" cy="62" r="6" fill="#E3A878"/>
        <ellipse cx="60" cy="60" rx="27" ry="29" fill="#EDB98A"/>
        <path d="M30 46 C30 28 42 18 60 18 C78 18 90 28 90 46 Z" fill="#1F2230"/>
        <rect x="29" y="41" width="62" height="7" rx="3" fill="#2B2F42"/>
        <g fill="#fff">${pep(38, 36, -20)}${pep(52, 28, -8)}${pep(65, 28, 8)}${pep(78, 34, 22)}</g>
        <path d="M44 53 L54 52M66 52 L76 53" stroke="#3B2618" stroke-width="3.2" stroke-linecap="round"/>
        <ellipse cx="49" cy="60" rx="3" ry="3.8" fill="#2B1B12"/><ellipse cx="71" cy="60" rx="3" ry="3.8" fill="#2B1B12"/>
        <circle cx="50" cy="58.6" r="1.1" fill="#fff"/><circle cx="72" cy="58.6" r="1.1" fill="#fff"/>
        <path d="M60 61 Q64 68 58 70" stroke="#C98A5E" stroke-width="2.2" fill="none" stroke-linecap="round"/>
        <path d="M45 77 Q53 70 60 74 Q67 70 75 77 Q67 81 60 78 Q53 81 45 77Z" fill="#3B2618"/>
        <path d="M53 82 Q60 87 67 82" stroke="#9B4A3A" stroke-width="2.4" fill="none" stroke-linecap="round"/>`);
    },

    ana() {
      return svg(`
        <rect x="2" y="52" width="30" height="38" rx="7" fill="#2F6DB5"/>
        <rect x="26" y="54" width="9" height="34" rx="3" fill="#24589A"/>
        <path d="M34 62 Q34 54 44 54 L100 54 Q108 54 108 61 Q108 68 100 68 L72 68 L72 88 Q72 98 60 98 L46 98 Q34 98 34 88Z" fill="#F4C49C"/>
        <g fill="#F4C49C" stroke="#D9A07A" stroke-width="1.6">
          <rect x="54" y="66" width="22" height="11" rx="5.5"/><rect x="54" y="76" width="21" height="11" rx="5.5"/><rect x="52" y="86" width="19" height="11" rx="5.5"/>
        </g>
        <ellipse cx="52" cy="58" rx="13" ry="6.5" fill="#EDB58A" stroke="#D9A07A" stroke-width="1.4"/>
        <ellipse cx="102" cy="61" rx="4" ry="3.2" fill="#FFE3D0"/>
        <g stroke="#F04D4D" stroke-width="4" stroke-linecap="round"><path d="M110 42 L116 32"/><path d="M114 52 L121 50"/><path d="M102 38 L102 28"/></g>`, '0 0 124 120');
    },

    nok() {
      return svg(`${shadow(113, 30)}
        <path d="M60 24 C52 24 50 38 46 48 C34 58 28 74 32 88 C36 104 52 110 60 110 C68 110 84 104 88 88 C92 74 86 58 74 48 C70 38 68 24 60 24Z" fill="#C5DC4A"/>
        <path d="M88 88 C84 104 68 110 60 110 C74 104 82 92 80 76 C79 66 76 58 74 48 C86 58 92 74 88 88Z" fill="#A9C33A"/>
        <ellipse cx="47" cy="78" rx="5" ry="11" fill="#fff" opacity=".4" transform="rotate(10 47 78)"/>
        <path d="M60 27 Q60 16 64 9" stroke="#7A4A22" stroke-width="4.5" fill="none" stroke-linecap="round"/>
        <path d="M63 16 Q78 5 88 13 Q75 25 63 16Z" fill="#4CAF50"/>`);
    },

    banan() {
      return svg(`${shadow(110, 40)}
        <path d="M22 30 Q18 78 58 94 Q90 104 108 86 Q104 81 98 83 Q76 90 56 76 Q36 62 34 30Z" fill="#FFD43B" stroke="#E0A800" stroke-width="2.6" stroke-linejoin="round"/>
        <path d="M28 38 Q31 74 64 88" stroke="#E8B800" stroke-width="2.2" fill="none"/>
        <path d="M22 31 L23 20 Q28 17 33 20 L34 31Z" fill="#7A5A2A"/>
        <circle cx="106" cy="86" r="3.2" fill="#5A4020"/>`);
    },

    limon() {
      let dots = '';
      for (const [x, y] of [[40, 70], [52, 80], [70, 82], [84, 70], [62, 62], [76, 56], [46, 58]]) dots += `<circle cx="${x}" cy="${y}" r="1.4"/>`;
      return svg(`${shadow(106, 40)}
        <ellipse cx="17" cy="66" rx="7" ry="5" fill="#F7D532"/><ellipse cx="103" cy="66" rx="7" ry="5" fill="#F7D532"/>
        <ellipse cx="60" cy="66" rx="42" ry="32" fill="#FFE04A"/>
        <path d="M100 70 Q90 96 60 98 Q36 98 22 80 Q44 90 64 88 Q88 86 100 70Z" fill="#F2C823"/>
        <ellipse cx="46" cy="52" rx="13" ry="5" fill="#fff" opacity=".5" transform="rotate(-15 46 52)"/>
        <g fill="#EBC21A">${dots}</g>
        <path d="M62 35 Q76 18 94 24 Q80 41 62 35Z" fill="#4CAF50"/>`);
    },

    olma() {
      return svg(`${shadow(112, 36)}
        <path d="M60 36 C48 26 20 28 20 60 C20 92 42 112 60 104 C78 112 100 92 100 60 C100 28 72 26 60 36Z" fill="#E53935"/>
        <path d="M100 60 C100 92 78 112 60 104 C80 100 94 84 94 60 C94 44 86 34 76 32 C92 32 100 44 100 60Z" fill="#C62828"/>
        <ellipse cx="38" cy="58" rx="6" ry="13" fill="#fff" opacity=".4" transform="rotate(18 38 58)"/>
        <path d="M60 37 Q58 22 64 13" stroke="#6D4C2A" stroke-width="4.5" fill="none" stroke-linecap="round"/>
        <path d="M62 24 Q78 9 93 17 Q79 32 62 24Z" fill="#43A047"/>`);
    },

    baliq() {
      return svg(`${shadow(104, 40)}
        <path d="M86 60 L114 36 Q106 60 114 84Z" fill="#F57C00"/>
        <path d="M40 38 Q56 18 74 38Z" fill="#F57C00"/>
        <ellipse cx="54" cy="60" rx="40" ry="26" fill="#FFA726"/>
        <g stroke="#F57C00" stroke-width="2.2" fill="none" stroke-linecap="round">
          <path d="M56 46 q7 6 0 12M68 46 q7 6 0 12M56 62 q7 6 0 12M68 62 q7 6 0 12M80 54 q6 6 0 12"/>
          <path d="M40 44 Q47 60 40 76"/>
        </g>
        <path d="M50 74 Q58 88 66 78Z" fill="#F57C00"/>
        <circle cx="29" cy="54" r="7.5" fill="#fff"/><circle cx="30" cy="54" r="4.2" fill="#1B2A4A"/><circle cx="31.5" cy="52.5" r="1.4" fill="#fff"/>
        <path d="M15 64 Q19 67 24 64" stroke="#B85A00" stroke-width="2.2" fill="none" stroke-linecap="round"/>`);
    },

    quyosh() {
      let rays = '';
      for (let i = 0; i < 12; i++) {
        const a = (i / 12) * Math.PI * 2;
        rays += `<path d="M${f(60 + 37 * Math.cos(a))} ${f(60 + 37 * Math.sin(a))} L${f(60 + 51 * Math.cos(a))} ${f(60 + 51 * Math.sin(a))}"/>`;
      }
      return svg(`<g stroke="#FFB300" stroke-width="7" stroke-linecap="round">${rays}</g>
        <circle cx="60" cy="60" r="31" fill="#FFD54F" stroke="#FFC107" stroke-width="3"/>
        <path d="M46 56 Q50 51 54 56M66 56 Q70 51 74 56" stroke="#7A4A00" stroke-width="3" fill="none" stroke-linecap="round"/>
        <circle cx="44" cy="66" r="4.5" fill="#FF8A65" opacity=".6"/><circle cx="76" cy="66" r="4.5" fill="#FF8A65" opacity=".6"/>
        <path d="M50 68 Q60 78 70 68" stroke="#7A4A00" stroke-width="3" fill="none" stroke-linecap="round"/>`);
    },

    tarvuz() {
      let seeds = '';
      for (const [x, y, r] of [[40, 58, -30], [60, 66, 0], [80, 58, 30], [50, 76, -15], [70, 76, 15], [60, 52, 0], [30, 50, -45], [90, 50, 45]]) {
        seeds += `<ellipse cx="${x}" cy="${y}" rx="2.2" ry="3.6" transform="rotate(${r} ${x} ${y})"/>`;
      }
      return svg(`${shadow(104, 44)}<g transform="translate(0 10)">
        <path d="M8 40 A52 52 0 0 0 112 40Z" fill="#2E9D3F"/>
        <path d="M14 40 A46 46 0 0 0 106 40Z" fill="#D7F2A8"/>
        <path d="M19 40 A41 41 0 0 0 101 40Z" fill="#F2475B"/>
        <g fill="#2B1B1B">${seeds}</g>
        <path d="M26 46 Q30 60 40 70" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" opacity=".35"/></g>`);
    },

    mushuk() {
      return svg(`${shadow(108, 34)}
        <path d="M26 50 L30 14 L56 34Z" fill="#F29E4C"/><path d="M94 50 L90 14 L64 34Z" fill="#F29E4C"/>
        <path d="M32 42 L34 24 L48 35Z" fill="#FFB6C1"/><path d="M88 42 L86 24 L72 35Z" fill="#FFB6C1"/>
        <ellipse cx="60" cy="64" rx="38" ry="34" fill="#F6AE5A"/>
        <g stroke="#E08A2E" stroke-width="4" stroke-linecap="round"><path d="M60 32v11M50 34l2 9M70 34l-2 9"/></g>
        <ellipse cx="60" cy="80" rx="15" ry="10" fill="#FFF1E0"/>
        <ellipse cx="46" cy="62" rx="5" ry="7" fill="#2E4A1E"/><ellipse cx="74" cy="62" rx="5" ry="7" fill="#2E4A1E"/>
        <circle cx="47.5" cy="59.5" r="1.8" fill="#fff"/><circle cx="75.5" cy="59.5" r="1.8" fill="#fff"/>
        <path d="M55 74 L65 74 L60 80Z" fill="#F06A8A"/>
        <path d="M60 80 Q56 86 51 83M60 80 Q64 86 69 83" stroke="#8A4A2A" stroke-width="2" fill="none" stroke-linecap="round"/>
        <g stroke="#8A5A3A" stroke-width="1.6" stroke-linecap="round"><path d="M42 78 L14 72M42 83 L14 86M78 78 L106 72M78 83 L106 86"/></g>`);
    },

    qush() {
      return svg(`${shadow(110, 32)}
        <path d="M86 70 L113 56 L109 82Z" fill="#2F7FD8"/>
        <ellipse cx="58" cy="66" rx="36" ry="30" fill="#4FA3F7"/>
        <ellipse cx="54" cy="79" rx="22" ry="15" fill="#CFE8FF"/>
        <path d="M58 58 Q84 50 93 72 Q74 82 58 58Z" fill="#2F7FD8"/>
        <path d="M24 59 L9 66 L24 71Z" fill="#FFA726"/>
        <circle cx="38" cy="54" r="7" fill="#fff"/><circle cx="37" cy="54" r="4" fill="#1B2A4A"/><circle cx="38.4" cy="52.5" r="1.4" fill="#fff"/>
        <circle cx="34" cy="68" r="4" fill="#FF9AA8" opacity=".6"/>
        <g stroke="#FFA726" stroke-width="3.4" stroke-linecap="round"><path d="M50 95 L48 106M64 95 L64 106"/></g>`);
    }
  };

  /* ---------- Nunu — o‘yin qahramoni ---------- */
  function mascot() {
    return svg(`
      <ellipse cx="60" cy="126" rx="34" ry="5" fill="#000" opacity=".13"/>
      <g class="m-body">
        <ellipse cx="44" cy="117" rx="13" ry="7" fill="#1452B8"/><ellipse cx="76" cy="117" rx="13" ry="7" fill="#1452B8"/>
        <g class="m-arm-l"><path d="M22 76 Q9 74 6 62" stroke="#2F80F5" stroke-width="9" fill="none" stroke-linecap="round"/><circle cx="6" cy="60" r="6.5" fill="#2F80F5"/></g>
        <g class="m-arm-r"><path d="M98 76 Q111 74 114 62" stroke="#2F80F5" stroke-width="9" fill="none" stroke-linecap="round"/><circle cx="114" cy="60" r="6.5" fill="#2F80F5"/></g>
        <path d="M56 15 Q57 2 67 6 Q62 9 63 15Z" fill="#2F80F5"/>
        <path d="M60 12 C92 12 104 40 104 72 C104 102 86 118 60 118 C34 118 16 102 16 72 C16 40 28 12 60 12Z" fill="#2F80F5"/>
        <path d="M104 72 C104 102 86 118 60 118 C34 118 16 102 16 72 C22 96 40 108 60 108 C80 108 98 96 104 72Z" fill="#1F6AE0"/>
        <ellipse cx="44" cy="30" rx="10" ry="5" fill="#fff" opacity=".25" transform="rotate(-25 44 30)"/>
        <ellipse cx="60" cy="90" rx="25" ry="19" fill="#fff"/>
        <text x="60" y="99" text-anchor="middle" font-family="Nunito, 'Arial Rounded MT Bold', Arial, sans-serif" font-weight="900" font-size="26" fill="#1E6FE8">Nn</text>
        <g class="m-eyes">
          <circle cx="46" cy="46" r="11.5" fill="#fff"/><circle cx="74" cy="46" r="11.5" fill="#fff"/>
          <circle cx="48" cy="48" r="5.8" fill="#10213F"/><circle cx="76" cy="48" r="5.8" fill="#10213F"/>
          <circle cx="50" cy="45.5" r="2.1" fill="#fff"/><circle cx="78" cy="45.5" r="2.1" fill="#fff"/>
        </g>
        <circle cx="34" cy="60" r="5" fill="#FF8FB1" opacity=".75"/><circle cx="86" cy="60" r="5" fill="#FF8FB1" opacity=".75"/>
        <path class="m-mouth" d="M52 60 Q60 70 68 60Z" fill="#0E2A66"/>
      </g>`, '-4 0 128 132');
  }

  /* ---------- Interfeys belgilari ---------- */
  const icon = {
    map: svg(`<path d="M14 26 L40 16 L80 28 L106 18 L106 94 L80 104 L40 92 L14 102Z" fill="#fff" stroke="currentColor" stroke-width="8" stroke-linejoin="round"/><path d="M40 16 V92 M80 28 V104" stroke="currentColor" stroke-width="7"/>`),
    soundOn: svg(`<path d="M18 46 H38 L62 24 V96 L38 74 H18Z" fill="currentColor" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/><path d="M76 42 Q88 60 76 78 M88 30 Q108 60 88 90" stroke="currentColor" stroke-width="8" fill="none" stroke-linecap="round"/>`),
    soundOff: svg(`<path d="M18 46 H38 L62 24 V96 L38 74 H18Z" fill="currentColor" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/><path d="M78 46 L104 74 M104 46 L78 74" stroke="currentColor" stroke-width="8" stroke-linecap="round"/>`),
    speaker: svg(`<path d="M18 46 H38 L62 24 V96 L38 74 H18Z" fill="currentColor"/><path d="M76 42 Q88 60 76 78 M88 30 Q108 60 88 90" stroke="currentColor" stroke-width="9" fill="none" stroke-linecap="round"/>`),
    star: svg(`<path d="M60 8 L75 41 L111 45 L84 69 L92 105 L60 87 L28 105 L36 69 L9 45 L45 41Z" fill="currentColor" stroke-linejoin="round" stroke="currentColor" stroke-width="6"/>`),
    lock: svg(`<rect x="24" y="52" width="72" height="56" rx="12" fill="currentColor"/><path d="M38 54 V38 Q38 16 60 16 Q82 16 82 38 V54" stroke="currentColor" stroke-width="11" fill="none"/><circle cx="60" cy="78" r="8" fill="#fff"/>`),
    play: svg(`<path d="M38 22 Q30 18 30 28 V92 Q30 102 38 98 L96 66 Q104 60 96 54Z" fill="currentColor"/>`),
    arrow: svg(`<path d="M22 60 H92 M64 30 L94 60 L64 90" stroke="currentColor" stroke-width="14" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`),
    again: svg(`<path d="M92 60 A32 32 0 1 1 82 37" stroke="currentColor" stroke-width="13" fill="none" stroke-linecap="round"/><path d="M68 22 L96 24 L90 52Z" fill="currentColor"/>`),
    check: svg(`<path d="M24 62 L50 88 L98 32" stroke="currentColor" stroke-width="16" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`)
  };

  /* ---------- Xarita bekatlari belgilari ---------- */
  const station = [
    svg(`<path d="M60 92 Q54 102 62 110" stroke="#8C9BB5" stroke-width="3" fill="none"/>
      <ellipse cx="60" cy="52" rx="32" ry="38" fill="#FF6B6B"/><path d="M54 88 L66 88 L60 96Z" fill="#E04B4B"/>
      <ellipse cx="47" cy="36" rx="7" ry="11" fill="#fff" opacity=".45" transform="rotate(20 47 36)"/>
      <text x="60" y="68" text-anchor="middle" font-family="Nunito, Arial, sans-serif" font-weight="900" font-size="44" fill="#fff">N</text>`),
    svg(`<g transform="rotate(40 60 60)"><rect x="48" y="8" width="24" height="76" rx="4" fill="#FFB020"/><rect x="48" y="8" width="24" height="14" rx="4" fill="#FF7EB6"/><rect x="48" y="20" width="24" height="6" fill="#C9D3E3"/><path d="M48 84 L60 110 L72 84Z" fill="#F5D7A8"/><path d="M55 99 L60 110 L65 99Z" fill="#1B2A4A"/><rect x="56" y="26" width="4" height="58" fill="#fff" opacity=".35"/></g>`),
    svg(`<path d="M28 52 Q60 6 92 52" stroke="#A86E33" stroke-width="7" fill="none"/>
      <circle cx="46" cy="46" r="13" fill="#E53935"/><circle cx="70" cy="44" r="14" fill="#E9A44E"/><circle cx="70" cy="44" r="7" fill="#F4CD8A"/>
      <path d="M14 56 L106 56 L96 100 Q95 104 90 104 L30 104 Q25 104 24 100Z" fill="#C98B4A"/>
      <rect x="10" y="50" width="100" height="12" rx="6" fill="#B07438"/>
      <g stroke="#A86E33" stroke-width="3"><path d="M22 74 H98 M26 88 H94"/><path d="M40 62 V104 M60 62 V104 M80 62 V104"/></g>`),
    svg(`<rect x="10" y="24" width="100" height="62" rx="12" fill="#fff" stroke="#4C8DFF" stroke-width="5"/>
      <text x="30" y="68" font-family="Nunito, Arial, sans-serif" font-weight="900" font-size="34" fill="#1B2A4A">o</text>
      <rect x="52" y="38" width="22" height="34" rx="5" fill="none" stroke="#4C8DFF" stroke-width="4" stroke-dasharray="6 5"/>
      <text x="80" y="68" font-family="Nunito, Arial, sans-serif" font-weight="900" font-size="34" fill="#1B2A4A">a</text>
      <rect x="62" y="76" width="34" height="36" rx="8" fill="#4C8DFF"/>
      <text x="79" y="103" text-anchor="middle" font-family="Nunito, Arial, sans-serif" font-weight="900" font-size="30" fill="#fff">n</text>`),
    svg(`<rect x="8" y="40" width="44" height="44" rx="10" fill="#9B6BFF"/><rect x="58" y="40" width="54" height="44" rx="10" fill="#FFB020"/>
      <text x="30" y="74" text-anchor="middle" font-family="Nunito, Arial, sans-serif" font-weight="900" font-size="32" fill="#fff">o</text>
      <text x="85" y="74" text-anchor="middle" font-family="Nunito, Arial, sans-serif" font-weight="900" font-size="32" fill="#fff">na</text>
      <path d="M26 96 Q56 112 86 96" stroke="#1B2A4A" stroke-width="4" fill="none" stroke-linecap="round"/>`)
  ];

  const basket = svg(`
    <path d="M8 22 L112 22 L100 80 Q99 86 93 86 L27 86 Q21 86 20 80Z" fill="#C98B4A"/>
    <g stroke="#A86E33" stroke-width="3.2"><path d="M14 42 H106 M18 62 H102"/><path d="M34 22 L38 86 M60 22 V86 M86 22 L82 86"/></g>
    <rect x="3" y="14" width="114" height="14" rx="7" fill="#B07438"/>`, '0 0 120 90');

  const medal = svg(`
    <path d="M38 6 L52 46 L68 46 L54 6Z" fill="#E04B4B"/><path d="M82 6 L68 46 L52 46 L66 6Z" fill="#2F80F5"/>
    <circle cx="60" cy="76" r="38" fill="#FFC93C" stroke="#E5A500" stroke-width="6"/>
    <circle cx="60" cy="76" r="27" fill="#FFD966"/>
    <text x="60" y="92" text-anchor="middle" font-family="Nunito, Arial, sans-serif" font-weight="900" font-size="40" fill="#B87800">Nn</text>`, '0 0 120 120');

  window.ART = {
    pic: (k) => (PIC[k] ? PIC[k]() : ''),
    mascot,
    icon,
    station,
    basket,
    medal
  };
})();
