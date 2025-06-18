from PIL import Image as img
import os, sys

Valid = False
print("Welcome to image cropper!")

while not Valid:
    imag = input("Choose an image!: ") #Choose your image's path
    if os.path.exists(imag):
            Valid = True
    elif KeyboardInterrupt or not os.path.exists(imag):
            print(f"Sorry, but we didn't found your image ({imag}), try again!")

im = img.open(imag)
Valid = False

while not Valid:
        heightLeft = float(input("Type a value for the left height: "))
        heightRight = float(input("Type a value for the right height: "))
        widthUp = float(input("Type a value for the upper width: "))
        widthLow = float(input("Type a value for the lower width: "))
        if heightLeft >= heightRight or widthUp>=widthLow or heightLeft > im.height or widthUp>im.width or heightLeft > im.height or widthUp>=im.width:
               print("Sorry but your values aren't valid")
        else:
               Valid = True

#PIL crop thinks in that way:
#right > left and low > up

im = im.crop((heightLeft, widthUp, heightRight, widthLow))

file_name = input("choose your file name: ")
file = input("Choose the folder where you want to save your file: ")

file = f"{file}/{file_name}"

im.save(file, format = "JPG", quality = 90)

im.show()

print("Here's your image! (Saved in the where you bringed the original)")
print("Thank you for using my program, bye... :)")