# Kartochka viktorina (prototip)

O‘quvchilarda telefon bo‘lmagan sinf uchun jonli viktorina.
Hamma ish sinf kompyuterida (yoki interaktiv doskada) bajariladi: sinf ro‘yxati, kartochkalar, savollar, o‘yin ekrani.
O‘quvchilar kartochkani javob harfi (A, B, C, D) tepada turadigan qilib ko‘taradi. Skanerlashning ikki yo‘li bor:

- **Telefon (asosiy).** O‘yin ekranida QR kod chiqadi. Istalgan telefon kamerasi bilan skanerlanadi va brauzerda skaner ochiladi — ilova o‘rnatish shart emas. Javoblar kompyuter ekraniga o‘zi tushadi, telefondan «Natijani ko‘rsatish» / «Keyingi savol»ni ham bosish mumkin. QR ishlamasa, havolani ochib 4 xonali kod kiritiladi.
- **Doska kamerasi.** Kompyuter yoki interaktiv doskaning o‘z kamerasi sinfga qaratiladi — telefon umuman kerak emas.

## Qanday ishlaydi

- Har bir kartochkada ArUco markeri (7×7 katakli oq-qora kvadrat) bor. Marker ichida o‘quvchining raqami kodlangan.
- Kamera markerni topadi, raqamdan o‘quvchini aniqlaydi, marker qanchaga burilganidan javob harfini oladi.
- Ha/Yo‘q savolda A = Ha, B = Yo‘q.
- Har bir to‘g‘ri javob 100 ball. Oxirida reyting chiqadi.

## Plickers'dan olingan funksiyalar

1. **Kompyuter va telefon-skaner sinxroni.** Ikkalasi o‘yin kodi nomli kanalga ulanadi. Kompyuter o‘yin holatini to‘liq yuboradi, telefon esa topgan javoblarini (o‘quvchi raqami → harf) va buyruqlarni yuboradi; holat egasi — kompyuter.
   - claude.ai ichida: artifact'ning jonli «room» kanali.
   - Fayl sifatida ochilganda: bitta brauzerning boshqa oynalari (BroadcastChannel).
   - Platformaga joylashda shu joyga o‘z WebSocket serverimiz qo‘yiladi (`joinChannel` / `send` funksiyalari).
2. **Natija jadvali.** «Natijalar» bo‘limida o‘quvchilar × savollar rangli jadvali va CSV eksport (Excel ochadi).
3. **Oflayn ishlash.** O‘yin holati telefonda saqlanadi: internet uzilsa ham skanerlash davom etadi, sahifa yangilansa ham javoblar yo‘qolmaydi. Aloqa tiklanganda ekran avtomatik yangilanadi.
4. **Live View.** Ekranda ikki ko‘rinish: «Kim javob berdi» (ismlar, javobsiz) va «Grafik» (har variantga nechta javob).

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
- `src/qrcode-lib.js` — [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) kutubxonasi (MIT litsenziyasi, `src/LICENSE-qrcode-generator.txt`).

## Prototip cheklovlari

- Sinxron hozircha claude.ai «room» kanali yoki bitta brauzer oynalari orqali; platformada o‘z serverimiz kerak.
- Sinovda 24 ta burilgan kartochkaning hammasi to‘g‘ri o‘qildi; xira (fokussiz) suratda ayrimlari o‘tkazib yuboriladi, lekin noto‘g‘ri o‘qilmaydi.
- Haqiqiy sinfda yorug‘lik va masofa bo‘yicha sinab ko‘rish kerak.
