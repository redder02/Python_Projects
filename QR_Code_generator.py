import qrcode as qr
str = input('enter the text to be converted into QR Code')
image = qr.make(str)
image.save("D:\QR\QR.jpg")
