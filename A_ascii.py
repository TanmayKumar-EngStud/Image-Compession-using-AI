from PIL import Image, ImageDraw, ImageFont
import os
import math
#QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()-+_={}[]\\/?.,<>;:
chars = "qwertyuiopasdfghjklzxcvbnm1234567890"[::-1]

charArray = list(chars)
charLength = len(charArray)
interval = charLength/256
# Finding current working directory
cwd = os.getcwd()

oneCharWidth = 11
oneCharHeight = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

text_file = open(cwd+"/B Text Folder/Output.txt", "w")
path = input("Enter image name: \n")
path = cwd+"/Test Photos/"+path
im = Image.open(path)
# H --> 570
# W --> 570*W/H
fnt = ImageFont.truetype('ArialCE.ttf', 15)

scaleFactor = .6

width, height = im.size
im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.BICUBIC)
width, height = im.size
pix = im.load()

outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (30, 30, 30))
d = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))
        d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))

    text_file.write('\n')

outputImage.save('output.jpg')
