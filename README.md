# android_automatic_resize_images
Given all xxxhdpi images, this python script automatically generates all the other images with the following resolution: mdpi, hdpi, xhdpi and xxhdpi in respective folder

1. Just put this python script under the root folder of your android project
2. Type python resize_images.py under command line
3. The script will iterate all image files with .png and .jpg as suffix in app/src/main/res/mipmap-xxxhdpi folder, and generate images with different resolutions and save them in respective folder, i.e. mipmap-mdpi, mipmap-hdpi, mipmap-xhdpi and mipmap-xxhdpi.
