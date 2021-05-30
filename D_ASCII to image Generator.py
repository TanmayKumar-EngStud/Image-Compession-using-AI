from PIL import ImageDraw, Image
import math
#QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()-+_={}[]\\/?.,<>;:
chars = "qwertyuiopasdfghjklzxcvbnm1234567890"[::-1]
charArray= list(chars)
charLen = len(chars)
interval = charLen/256
oneCharWidth = 1
oneCharHeight = 2


path = "/home/tanmay/github/ASCII-program/B Text Folder/Result.txt"
with open(path, 'r') as value:
    fNew = value.readlines()

height= len(fNew)
width = len(fNew[0])


outputImage= Image.new('RGB', (oneCharWidth*width,oneCharHeight*height),(128,128,128))
d=ImageDraw.Draw(outputImage)
print(height, end=" ")
print(width, "\n")
for i in range(height-1):
    for j in range(width-1):

        v=chars.find(fNew[i][j])+1 #so that value of v doesn't get zero
        intensity=math.floor(v/interval)
        d.rectangle((j*oneCharWidth,i*oneCharHeight,(j+1)*oneCharWidth,(i+1)*oneCharHeight), fill=(intensity, intensity, intensity))
#ImageDraw.point(xy, fill=None)
outputImage= outputImage.resize((int(width*250/height),250), Image.BICUBIC)


outputImage.save('/home/tanmay/github/ASCII-program/pixelated image/Generated.png')
