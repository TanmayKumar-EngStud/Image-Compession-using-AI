from PIL import ImageDraw, Image, ImageFilter
import math
import cv2
import glob
import os.path as osp
from os import path
cwd = path.dirname(path.abspath(__file__))
test_img_folder = cwd + "/pixelated image/*"
i =0
for path in glob.glob(test_img_folder):
    i = i+1
    im = Image.open(path)
    width , height = im.size
    im = im.resize((int(width), int(height+200)), Image.BICUBIC)
    im = im.filter(ImageFilter.SMOOTH_MORE)
    im.save(cwd+'/Final Image/Image generated {}.png'.format(i))