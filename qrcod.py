import qrcode

# Website link
link = "https://alvora.ir/"

# Create QR Code
qr = qrcode.make(link)

# Save QR Code image
qr.save("my_qrcode.png")

print("QR Code created successfully!")
print("Website:", link)
print("Image saved as my_qrcode.png")