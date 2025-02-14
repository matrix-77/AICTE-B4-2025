import cv2
import os
import string
# Read the image
img = cv2.imread("Sample_Image.png")  # Ensure this path is correct
# Check if the image is read correctly
if img is None:
    print("Image not found or path is incorrect")
    exit()
# Input secret message and passcode
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")
# Dictionaries for encoding and decoding
d = {}
c = {}
for i in range(256):  # Use 256 for all possible ASCII characters
    d[chr(i)] = i
    c[i] = chr(i)
# Initialize positions
n = 0
m = 0
z = 0
# Encode message into image
for i in range(len(msg)):
    if n >= img.shape[0] or m >= img.shape[1]:
        print("Message is too long for this image")
        break
    img[n, m, z] = d[msg[i]]
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m == img.shape[1]:
            m = 0
            n += 1
# Write the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
print("Image written successfully")
# Open the image (change command based on OS)
if os.name == 'nt':  # For Windows
    os.system("start encryptedImage.jpg")
elif os.name == 'posix':  # For Linux/Unix
    os.system("xdg-open encryptedImage.jpg")
else:
    print("Unsupported OS")
# Decryption process
message = ""
n = 0
m = 0
z = 0
pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        if n >= img.shape[0] or m >= img.shape[1]:
            break
        message += c[img[n, m, z]]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == img.shape[1]:
                m = 0
                n += 1
    print("Decryption message:", message)
else:
    print("YOU ARE NOT authorized")
