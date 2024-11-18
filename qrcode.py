import qrcode

# Create a QR code for the given URL
image = qrcode.make("https://127.0.0.1:8000")

# Save the QR code image to a file
image.save("qrcode.png")