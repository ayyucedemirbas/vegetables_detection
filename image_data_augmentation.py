from os import listdir
from os.path import isfile, join
from PIL import Image, ImageOps, ImageChops, ImageFilter
import random
import glob
mypath = "./vegetables_data/"
#imagefiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
imagefiles = glob.glob(mypath + '*.png')
cnt=0

for my_image in imagefiles:
    img = Image.open(my_image)
    mirror_img = ImageOps.mirror(img)
    mirror_img.save(mypath+ str(cnt)+"_mirror.png")

    img_to_shift = Image.open(my_image)
    img_shifted =ImageChops.offset(img_to_shift, -800, -400)
    img_shifted.save(mypath + str(cnt) +'_shifted.png')

    im = Image.open(my_image)
    im2 = im.filter(ImageFilter.GaussianBlur(5))
    im2.save(mypath+str(cnt) +'_GaussianBlur.png')


    """"pepper_salt=add_noise(my_image)
    pepper_salt.save(str(cnt) +'_pepperSalt.png')"""



    """image_file = Image.open(my_image) # open colour image
    image_file = image_file.convert('1') # convert image to black and white
    image_file.save(mypath + str(cnt) +'_black_white.png')"""
    

    HSV= img.convert('HSV')

    # Split into separate channels
    H, S, V = HSV.split()
    S = S.point(lambda p: p//2)
    H = H.point(lambda p: p//3)

    HSVr = Image.merge('HSV', (H,S,V))

    RGBr = HSVr.convert('RGB')

    RGBr.save(mypath+str(cnt)+'_hsv.png')
    

    S = S.point(lambda p: p//1)
    H = H.point(lambda p: p//4)

    HSVr = Image.merge('HSV', (H,S,V))

    RGBr = HSVr.convert('RGB')

    RGBr.save(mypath+str(cnt)+'_hsv_1.png')
    
    with Image.open(my_image) as im:
        im.rotate(120).save(mypath+str(cnt) +"_rotated.png")


    with Image.open(my_image) as im:
        

        width, height = im.size
        
        # Setting the points for cropped image
        left = 50
        top =  height / 4
        right = 1640
        bottom =  3 * height / 4
        
        # Cropped image of above dimension
        # (It will not change original image)
        im1 = im.crop((left, top, right, bottom))
        
        
        im1.save(mypath+str(cnt)+"_cropped.png")
    with Image.open(my_image) as im:
        

        width, height = im.size
        
        # Setting the points for cropped image
        left = 500
        top =  height / 4
        right = 1197
        bottom =  3 * height / 4
        
        # Cropped image of above dimension
        # (It will not change original image)
        im1 = im.crop((left, top, right, bottom))
        
        
        im1.save(mypath+str(cnt)+"_cropped_1.png")
        
    cnt=cnt+1
