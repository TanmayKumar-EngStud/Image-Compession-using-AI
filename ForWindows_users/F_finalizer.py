from PIL import ImageDraw, Image, ImageFilter
import math
import cv2
import glob
import os.path as osp


test_img_folder = "C:\\Users\\dsnma\\Desktop\\tanmay temporary folder\\AI Project\\Image-Compession-using-AI-main\\Image-Compession-using-AI-main\\results\\*"
i =0
for path in glob.glob(test_img_folder):
    i = i+1
    im = Image.open(path)
    width , height = im.size
    im = im.resize((int(width+200), int(height)), Image.BICUBIC)
    im = im.filter(ImageFilter.SMOOTH_MORE)
    im.save('C:\\Users\\dsnma\\Desktop\\tanmay temporary folder\\AI Project\\Image-Compession-using-AI-main\\Image-Compession-using-AI-main\\rFinal Result\\Final Image {}.png'.format(i))