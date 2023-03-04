#QR Code Scanner
import pyqrcode
from pyqrcode import QRCode
s=input("")
url=pyqrcode.create(s)
url.svg("MYQRcode.svg",scale=10)