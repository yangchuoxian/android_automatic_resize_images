#!/bin/sh
import os, sys
import PIL
from PIL import Image

xxxhdpi_folder_path = './app/src/main/res/mipmap-xxxhdpi/'
xxhdpi = 0.75
xhdpi = 0.5
hdpi = 0.375
mdpi = 0.25

def round_to_int(x):
	return int(round(x, 0))

def resize_image_with_ratio(ratio, filename):
	image = Image.open('./' + filename)
	original_image_width = image.size[0]
	original_image_height = image.size[1]
	resized_image_width = round_to_int(original_image_width * ratio)
	resized_image_height = round_to_int(original_image_height * ratio)
	resized_image = image.resize((resized_image_width, resized_image_height), PIL.Image.ANTIALIAS)

	if ratio == mdpi:
		resized_image.save('../mipmap-mdpi/' + filename)
	elif ratio == hdpi:
		resized_image.save('../mipmap-hdpi/' + filename)
	elif ratio == xhdpi:
		resized_image.save('../mipmap-xhdpi/' + filename)
	elif ratio == xxhdpi:
		resized_image.save('../mipmap-xxhdpi/' + filename)

os.chdir(xxxhdpi_folder_path)
for filename in os.listdir(os.getcwd()):	
	if filename.endswith(".png") or filename.endswith(".jpg"):
		print 'resizing image: ' + filename
		resize_image_with_ratio(xxhdpi, filename)
		resize_image_with_ratio(xhdpi, filename)
		resize_image_with_ratio(hdpi, filename)
		resize_image_with_ratio(mdpi, filename)
