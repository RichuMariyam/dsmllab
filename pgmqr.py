import pyqrcode
import png
from pyqrcode import QRCode
s=input("Enter your url")
myqr=input("enter your filename")
url=pyqrcode.create(s)
url.svg(myqr+".svg",scale=8)