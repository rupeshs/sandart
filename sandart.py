
"""
=====================================================
              SandArt 
Converts photos to sand artworks
Copyright 2017 Rupesh Sreeraman. All Rights Reserved
=====================================================
"""
#imports 
from PIL import Image,ImageFilter
from collections import defaultdict
import argparse
import time

print("")
print("***********************************************")
print("                 SandArt v1.0                  ")
print("Converts photos to sand artworks")
print("Copyright 2017 Rupesh Sreeraman")
print("***********************************************")
print("")

#options
parser = argparse.ArgumentParser(description='SandArt v1.0')
parser.add_argument('-i','--image',help='Source image path',required=True,)
parser.add_argument('-s','--strength',help='Sand art strength [1-20]',type=int,default=10)
parser.add_argument ('-c','--sandcolor', help='Sand art strength,RGB value eg: 255 30 50',nargs=3,type=int)
parser.add_argument ('-n','--invert', help='Invert style use 1 to enable 0 to disable | default 0',type=int,default=0)
parser.add_argument('-o' ,'--savepath',help='Sand art path',required=True)

args = parser.parse_args()

if args.sandcolor is not None :
    sandcolor=tuple(args.sandcolor)
else:
    sandcolor = (230, 208, 170)

start = time.time()    
try:
    im = Image.open(args.image)
except:
    print("ERROR:Unable to open image!")  
    exit()

width, height = im.size
print (im.format, im.size, im.mode)
print('Sand color ',str(sandcolor))

im_out = Image.new("RGB", (width, height), "white") #New RGB to hold the result
rgb_im = im.convert('RGB') #convert

rgb_im_out = im_out.convert('RGB')

color_dict = defaultdict(int)
for pixel in im.getdata():
    color_dict[pixel] += 1

for y in range(0,height):
    for x in range (0,width):
        r,g,b=rgb_im.getpixel((x, y))
        count=color_dict.get((r,g,b))
        if  args.invert==1:
            if count>=args.strength :
                rgb_im_out.putpixel((x,y),sandcolor)
        else:
            if count<=args.strength :
                rgb_im_out.putpixel((x,y),sandcolor)
try:
    rgb_im_out.save(args.savepath)
    print("Saved sandart successfully.")  
except:
    print("ERROR:Unable to save the sandart image!")  

print ('Elaspsed ',time.time() - start, 'sec') 