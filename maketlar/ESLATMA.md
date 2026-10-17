# Masterium Market — ish holati (2026-10-17)

Keyingi sessiyada shu fayldan davom etiladi.

## Manba
- Figma: https://www.figma.com/design/WHlfUq89xLo2wcbcNKAXm0 (Production → «In Progress», node 3:5)
- Xaridor bo‘limlari: Ro‘yhat yaratish, Bozor, Tanlanganlar, Profil, Bildirishnomalar
- Sotuvchi bo‘limlari: Ro‘yhatdan o‘tish, Asosiy (tovarlar), Qidiruv, Izohlar, Statistika, Sozlamalar, Bildirishnomalar
- Figma’da Sotuvchi mind-map’i bor (Group 1, node 2285:7904)
- Dizayn tokenlari: primary #015594, soft #E6EEF4, field #F1F2F3, line #E4E4E7, shrift Inter, ekran kengligi 375px

## Tayyor maketlar (`maketlar/`, HTML + PNG)
- `4-tovar-chegirma` — hamma narxlarga bitta chegirma (foiz yoki summa), birinchi variant
- `5-chegirma-har-narxga` — Dona, Ulgurji va Partiya uchun alohida chegirma (tavsiya etilgan variant)
- `6-sotuvchi-tariflar` — tariflar: Sozlamalar kartasi, solishtirish, paywall, to‘lov, muvaffaqiyat, tugayapti, tugadi, Ko‘tarish
- `7-rasmsiz-tovar-va-tahlil` — rasmsiz tovar: yagona katalog, bozor narxi, xaridor kartasi, narx tahlili, talab tahlili, ommaviy narx, Excel import, narxlarni tasdiqlash

## Muhim cheklov
- Ilovada tovar rasmi, videosi va Stories YO‘Q. Tovar katalog, kategoriya ikonkasi, xususiyat chiplari va «narx yangilangan» belgisi orqali ko‘rsatiladi

## Tarif bo‘yicha qarorlar
- To‘lov ilova ichida emas, tashqi ilovada (Click, Payme, Uzum). MChJ’lar uchun bank o‘tkazmasi
- Narx barcha sotuvchi turlari (Bozor, Do‘kon, Sklad) uchun bir xil
- Start: bepul, 20 tovar · Standart: 99 000/oy (yiliga 990 000), 200 tovar · Biznes: 249 000/oy (yiliga 2 490 000), cheksiz
- Hammaga bepul: katalog, Excel import, narx tasdiqlash · Standart: chegirma, ommaviy narx, 90 kunlik statistika, Telegram, 2 ta ko‘tarish · Biznes: narx va talab tahlili, yillik statistika, ko‘p filial, 3 ta xodim, 10 ta ko‘tarish
- Ko‘tarish: 3 kun 9 000 so‘m, 7 kun 19 000 so‘m
- Ishga tushirish: birinchi 3 oy hammaga Biznes bepul; birinchi 50 ta sotuvchiga umrbod −30%

## Ochiq savollar
- «100–200» — sotuvchilar sonimi yoki bitta sotuvchidagi tovarlar sonimi? Ikkinchisi bo‘lsa, limitlar 30 / 300 ga o‘zgaradi
- App Store va Google Play: tashqi to‘lov havolasi qoidalarga to‘g‘ri keladimi, tekshirish kerak (muqobil: veb-sayt yoki Telegram-bot)
- Figma’dagi izohlar (comment) hali ko‘rib chiqilmagan, MCP ularni o‘qiy olmaydi, foydalanuvchi matn ko‘rinishida beradi
- Mind-map’da bor, lekin dizaynda yo‘q: Telegram ulash, do‘kon Active on/off

## Keyingi qadamlar (taklif)
- Maketlarni Figma’ga ko‘chirish
- Telegram ulash ekrani
- Katalog tuzilmasi (kategoriyalar, xususiyatlar, moderatsiya)
- Branch’ni `main`ga qo‘shish uchun PR ochish
