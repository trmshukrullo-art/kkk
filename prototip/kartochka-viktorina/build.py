# Kutubxonalarni app.html ichiga joylab, bitta index.html faylini yig'adi.
import pathlib
d = pathlib.Path(__file__).parent
app = (d / 'src/app.html').read_text()
lib = (d / 'src/aruco-lib.js').read_text() + '\n' + (d / 'src/qrcode-lib.js').read_text()
(d / 'index.html').write_text(app.replace('/*LIB*/', lib))
print('index.html tayyor')
