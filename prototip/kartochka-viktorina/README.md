# Kartochka viktorina (prototip)

O‘quvchilarda telefon bo‘lmagan sinf uchun jonli viktorina. Telefon faqat o‘qituvchida bo‘ladi.
O‘quvchi o‘z kartochkasini javob harfi (A, B, C, D) tepada turadigan qilib ko‘taradi,
o‘qituvchi telefon kamerasi bilan sinfni skanerlaydi.

## Qanday ishlaydi

- Har bir kartochkada ArUco markeri (7×7 katakli oq-qora kvadrat) bor. Marker ichida o‘quvchining raqami kodlangan.
- Kamera markerni topadi, raqamdan o‘quvchini aniqlaydi, marker qanchaga burilganidan javob harfini oladi.
- Ha/Yo‘q savolda A = Ha, B = Yo‘q.
- Har bir to‘g‘ri javob 100 ball. Oxirida reyting va savollar bo‘yicha hisobot chiqadi.

## Ishlatish

1. `index.html` faylini brauzerda oching (kompyuter yoki telefon).
2. «Sinf» bo‘limida o‘quvchilar ro‘yxatini kiriting.
3. «Kartochkalar» → «Chop etish». A4 varaqqa 2 tadan chiqadi.
4. «Savollar» bo‘limida savollarni tahrirlang.
5. «O‘yin» → «Skanerlash». Jonli kamera ishlamasa, «Surat orqali» tugmasi bilan sinfni suratga oling.

Jonli kamera faqat HTTPS orqali (yoki kompyuterda faylni to‘g‘ridan-to‘g‘ri ochganda) ishlaydi.
Ma’lumotlar (ro‘yxat, savollar) shu brauzerning o‘zida saqlanadi.

## Fayllar

- `index.html` — tayyor, bitta fayldan iborat ilova (`python3 build.py` bilan yig‘iladi).
- `src/app.html` — ilova kodi.
- `src/aruco-lib.js` — [js-aruco](https://github.com/jcmellado/js-aruco) kutubxonasi (MIT litsenziyasi, `src/LICENSE-js-aruco.txt`).

## Prototip cheklovlari

- Savol ekrani va skaner bitta qurilmada. Proyektor va telefonni sinxronlash uchun server kerak bo‘ladi.
- Sinovda 24 ta burilgan kartochkaning hammasi to‘g‘ri o‘qildi; xira (fokussiz) suratda ayrimlari o‘tkazib yuboriladi, lekin noto‘g‘ri o‘qilmaydi.
- Haqiqiy sinfda yorug‘lik va masofa bo‘yicha sinab ko‘rish kerak.
