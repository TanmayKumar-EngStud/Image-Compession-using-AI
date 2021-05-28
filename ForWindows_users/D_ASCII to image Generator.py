from PIL import ImageDraw, Image, ImageFilter
import math

chars = "qwertyuiopasdfghjklzxcvbnm1234567890"[::-1]
charArray= list(chars)
interval = 70/256
oneCharWidth = 1
oneCharHeight = 2


path = "C:\\Users\\dsnma\\Desktop\\tanmay temporary folder\\AI Project\\Image-Compession-using-AI-main\\Image-Compession-using-AI-main\\B Text Folder\\Result.txt"
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
width , height = outputImage.size
outputImage = outputImage.resize((int(width*0.7), int(height*0.7)), Image.BICUBIC)

outputImage = outputImage.filter(ImageFilter.GaussianBlur(radius = 0.2))

outputImage.save('C:\\Users\\dsnma\\Desktop\\tanmay temporary folder\\AI Project\\Image-Compession-using-AI-main\\Image-Compession-using-AI-main\\LR\\Generated.png')
