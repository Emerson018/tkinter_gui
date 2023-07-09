import qrcode

imagem_qrcode = qrcode.make("https://www.speedtest.net/pt")
imagem_qrcode.save("qrcode_python.png")

