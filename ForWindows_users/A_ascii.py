from PIL import Image, ImageDraw, ImageFont

import math

chars = "qwertyuiopasdfghjklzxcvbnm1234567890"[::-1]

charArray = list(chars)
charLength = len(charArray)
interval = charLength/256




oneCharWidth = 11
oneCharHeight = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

text_file = open("C:\\Users\\dsnma\\Desktop\\tanmay temporary folder\\AI Project\\Image-Compession-using-AI-main\\Image-Compession-using-AI-main\\B Text Folder\\Output.txt", "w")
path = input("Enter image name: \n")
path = "C:\\Users\\dsnma\\Desktop\\tanmay temporary folder\\AI Project\\Image-Compession-using-AI-main\\Image-Compession-using-AI-main\\Test Photos\\"+path
im = Image.open(path)

fnt = ImageFont.truetype('C:\\Users\\dsnma\\Desktop\\tanmay temporary folder\\AI Project\\Image-Compession-using-AI-main\\Image-Compession-using-AI-main\\ArialCE.ttf', 15)

width, height = im.size

scaleFactor = 300/height
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

outputImage.save('C:\\Users\\dsnma\\Desktop\\tanmay temporary folder\\AI Project\\Image-Compession-using-AI-main\\Image-Compession-using-AI-main\\output.jpg')
