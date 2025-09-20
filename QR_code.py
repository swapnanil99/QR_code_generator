import qrcode as qr # Importing the qrcode library and renaming it to qr using 'as' keyword

data = input("Enter the data for the QR code: ") # Taking input from the user for the data to be encoded in the QR code

img = qr.make(data) # Creating a QR code for the given URL

img.save('youtube_qr.png') # Saving the QR code image as 'youtube_qr.png'

print("QR code saved as youtube_qr.png")