#code to automate the resizing of images locked by the aspect ratio

#for now we will do this via the width, which will be locked to 400 pixels and then the height will be changed to match that ratio

#this will also reduce the amount of images that need to be cropped for this, which likely can be automated as well

from PIL import Image
from os import listdir, makedirs
from os.path import isfile, join, isdir
import time

def make_square(im, min_size=400, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

image_dir='/Users/zb3663/Desktop/clearvale_stimuli_set/stimuli_clearvale' #root image directory 

sub_folders = [name for name in listdir(image_dir) if isdir(join(image_dir, name))]

basewidth = 400 #set pixel width 

for w in sub_folders:
    resized_folder=isdir(join(image_dir,('resized_'+w)))
    if not resized_folder:
        makedirs(join(image_dir,('resized_'+w)))
        print("created resized folder for: ", w)
    else:
        print("resized folder already exists")

    time.sleep(2)

    onlyfiles = [f for f in listdir(join(image_dir,w)) if isfile(join(image_dir, w,f))] # get all the files in a folder but not the directories 

    for i in onlyfiles: #loop across the list of images 
        img = Image.open(join(image_dir,w,i)) #load in your image
        
        x,y=img.size

        if y>x:

            hpercent = (basewidth / float(img.size[1])) #get the ratio of the current height to the new height, giving us a scaling factor
            wsize = int((float(img.size[0]) * float(hpercent))) #scaled width
            img = img.resize((wsize, basewidth), Image.ANTIALIAS) # resize the image based on the new width and height

            #now we need to add transparent box to the x axis, so it fits as a square
            # we are going to use that make_square code above, which adds transparent sections to which ever axis is too small
            img= make_square(img)

            img.save(join(image_dir,('resized_'+w),i), format='png') #save the image 
            print(i, " has been resized and saved")

        elif x>y:

            wpercent = (basewidth / float(img.size[0])) #get the ratio of the current width to the new width, giving us a scaling factor
            hsize = int((float(img.size[1]) * float(wpercent))) #scaled height
            img = img.resize((basewidth, hsize), Image.ANTIALIAS) # resize the image based on the new width and height

            #now we need to add transparent box to the y axis, so it fits as a square
            # we are going to use that make_square code above, which adds transparent sections to which ever axis is too small
            img= make_square(img)

            img.save(join(image_dir,('resized_'+w),i), format='png') #save the image 
            print(i, " has been resized and saved")
        

        else:
            img=img.resize((basewidth,basewidth), Image.ANTIALIAS)
            img.save(join(image_dir,('resized_'+w),i),  format='png') #save the image 
            print(i, " has been resized and saved")