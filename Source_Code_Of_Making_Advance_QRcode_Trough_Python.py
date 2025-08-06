import qrcode
from PIL import Image
qr=qrcode.QRCode(version=6,
                  box_size=10, border=10)
qr.add_data("https://github.com/RabbanAli1122")
qr.make(fit=True)
img=qr.make_image(fill_color="white",back_color="black")
img.save("python_20_projects.png")
