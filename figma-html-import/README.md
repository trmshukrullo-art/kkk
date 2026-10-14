# HTML → Figma Import (Figma plagini)

`.html` fayllarni (masalan `maketlar/html/` dagi variantlarni) Figma'ga **tahrirlanadigan qatlamlar** sifatida import qiladi: frame'lar, matnlar, SVG ikonkalar, rasmlar, gradientlar, soyalar, border-radius.

## O'rnatish (bir marta)

1. **Figma Desktop** ilovasini oching (brauzer versiyasida lokal plagin qo'shib bo'lmaydi).
2. Istalgan dizayn faylda: **Menu → Plugins → Development → Import plugin from manifest…**
3. Shu papkadagi `manifest.json` ni tanlang.

## Ishlatish

1. **Plugins → Development → HTML → Figma Import**.
2. Bir yoki bir nechta `.html` faylni oynaga tashlang (yoki bosib tanlang). Kodni to'g'ridan-to'g'ri joylashtirish ham mumkin.
3. Kenglik: bo'sh qoldirsangiz `<meta name="viewport" content="width=1440">` dan olinadi, bo'lmasa 1440px.
4. **Figma'ga import qilish** — har bir fayl alohida frame bo'lib, yonma-yon joylashadi (variantlarni solishtirish uchun qulay).

## Qanday ishlaydi

- `ui.html` HTML'ni yashirin iframe ichida haqiqiy brauzer kabi render qiladi, shriftlar va rasmlar yuklanishini kutadi, so'ng har bir elementning o'lchami, joyi va hisoblangan CSS uslublarini o'qiydi.
- `code.js` shu ma'lumotdan Figma qatlamlarini yaratadi: element → Frame (nomi CSS klassidan), matn → Text (aralash uslublar bilan), `<svg>` → vektor, `<img>` → rasm to'ldirish.
- Shriftlar Figma'dagi mavjud shriftlarga moslanadi; topilmasa **Inter** ishlatiladi va bu haqida ogohlantiriladi. Eng aniq natija uchun HTML'dagi shriftlar (Geist, Inter, Instrument Sans) kompyuteringizda / Figma'da bo'lsin.

## Qo'llab-quvvatlanadi

fon rangi, `linear-/radial-gradient`, `background-image: url()`, `border` (har tomon alohida), `outline`, `border-radius`, `box-shadow` (shu jumladan `inset`), `opacity`, `overflow: hidden` (clip), `filter/backdrop-filter: blur`, `text-transform`, `letter-spacing`, `line-height`, `text-align`, `underline`, `z-index` tartibi, data-URI va tashqi rasmlar, input/textarea qiymatlari.

## Cheklovlar

- Natija absolyut joylashuvda (auto layout emas).
- `transform: rotate/scale` qo'llanilmaydi (faqat yakuniy chegaralar olinadi), `::before/::after` psevdo-elementlar import qilinmaydi.
- `:hover` kabi holatlar — faqat HTML'da ko'rinib turgan holat import qilinadi.
