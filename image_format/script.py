from PIL import Image, ImageDraw, ImageFont
import os
import pandas as pd

def create_certificate(name):
	# open original template
	im = Image.open('original.png')
	width, height = im.size

	# set font type and size
	font = ImageFont.truetype("/Library/Fonts/Georgia.ttf", 110)

	# get name width and height to center it
	text_w, text_h = font.getsize(name)

	# "draw" the name on the certificate
	draw = ImageDraw.Draw(im)
	draw.text(((width - text_w)/2, 1100), name, fill = "black", font = font)

	im.save(os.path.join('prints', name + ".png"), "PNG")

# read csv file
f = open('orig.csv', 'r')
students = pd.read_csv(f)

# get students eligible for attendance (total attendance (ta) >= 7)
students = students[students.ta >= 7][['first_name', 'last_name']]

ctr = 0

# go through each student and create certificate
for i in range(len(students)):
	row = list(students.iloc[i])
	first_name = row[0][0].upper() + row[0][1:] # ensuring first letter of first name is capital (wasn't already in the original data)
	last_name = row[1][0].upper() + row[1][1:] # ensuring first letter of last name is capital (wasn't already in the original data)

	name = first_name + ' ' + last_name # joining first name and last name

	create_certificate(name)

	ctr += 1
	print ctr, name