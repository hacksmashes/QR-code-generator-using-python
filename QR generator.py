import pyqrcode
import png
from pyqrcode import QRCode

# give something below within the string to generate QR
a="hello world"

url=pyqrcode.create(a)
url.svg("qr.svg",scale=8)
url.png("qr.png",scale=6)













