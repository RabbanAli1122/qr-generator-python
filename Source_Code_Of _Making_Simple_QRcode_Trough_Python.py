import qrcode as qr
image= qr.make("https://www.youtube.com/watch?v=OKuiyX5k6zg")
image.save("python.png")