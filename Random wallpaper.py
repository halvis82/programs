#by Halvor, created: 20.02.2021, Picks random wallpaper in a folder
#Having trouble comparing jpg's, but not a big issue


#Importing libraries
import os
import random
from PIL import Image
import ctypes


#Check if wallpaper folder doesn't exist or is empty
wallpapers_path = "wallpapers\\"
if not os.path.exists(wallpapers_path):
    try:
        os.mkdir(wallpapers_path)
        print("'.\\{}' did not exist, but it has been created. Add images and run me again".format(wallpapers_path))
    except:
        print("'.\\{}' folder does not exist, and it could not be created".format(wallpapers_path))
    finally:
        exit()
elif len(os.listdir(wallpapers_path)) <= 1:
    print("'.\\{}' contains 1 image or is empty. Add images and run again".format(wallpapers_path))
    exit()


#Check if all images in wallpaper folder are identical
img1_path = "{}\\{}{}".format(os.getcwd(), wallpapers_path, os.listdir(wallpapers_path)[0])
img1 = Image.open(img1_path)
allImagesIdentical = True
for i in range(1, len(os.listdir(wallpapers_path))):
    current_img_path = "{}\\{}{}".format(os.getcwd(), wallpapers_path, os.listdir(wallpapers_path)[i])
    if list(img1.getdata()) != list(Image.open(current_img_path).getdata()):
        allImagesIdentical = False
        break
if allImagesIdentical:
    print("All images in '.\\{}' are identical. Add unique ones".format(wallpapers_path))
    quit()


#Get old/current wallpaper
old_wallpaper_path = "{}\\Microsoft\\Windows\\Themes\\TranscodedWallpaper".format(os.getenv('APPDATA'))
old_wallpaper = Image.open(old_wallpaper_path)


#Get new image until they're not identical
while True:
    new_wallpaper_path = "{}\\{}{}".format(os.getcwd(), wallpapers_path, random.choice(os.listdir(wallpapers_path)))
    new_wallpaper = Image.open(new_wallpaper_path)
    if list(old_wallpaper.getdata()) != list(new_wallpaper.getdata()):
        break


#Set new wallpaper
try:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, new_wallpaper_path, 0)
    print("Successfully set '{}' as wallpaper".format(new_wallpaper_path))
except:
    print("Could not set '{}' as wallpaper".format(new_wallpaper_path))