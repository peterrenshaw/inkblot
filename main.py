#!/usr/bin/env python
# ~*~ coding: utf-8 ~*~


#
# name: main.py
# date: 2020JUL08
# prog: pr
# desc: A simple pihole mini-hack to display
#       the CRON update cycle onscreen.
# sorc: <https://github.com/pimoroni/inky/blob/master/examples/phat/weather-phat.py>
#


import os
from time import strftime
from time import localtime


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from inky import InkyPHAT
from font_untuitive import Intuitive


#
# setup
#
COLOR = "red"
SCALE_SIZE = 1.0
MMMDD = "%b%d"
DT = "{}".format( strftime(MMMDD, localtime()).upper()
ID = InkyPHAT(COLOR)


#
# create_mask
# < https://github.com/pimoroni/inky/blob/master/examples/phat/weather-phat.py>
# 
def create_mask(source,
                mask=(inky_display.WHITE, 
                      inky_display.BLACK,
                      inky_display.RED)):
    mask_image = Image.new("1", source.size)
    w, h = source.size
    for x in range(w):
        for y in range(h):
            p = source.getpixel((x, y))
            if p in mask:
                mask_image.putpixel((x, y), 255)

    return mask_image


:#
# dictionaries to store icons and masks in
#
icons = {}
mask = {}


# 
# maps icon to time phase
# 
icon_map = {
    "first":  ["wind"],
    "second": ["sun"],
    "third":  ["rain"],
    "forth":  ["storm"]
}
time_icon = None
time_icon = icon_map["second"]

# canvas
img = Image.open(os.path.join(PATH, "logoneek.png")
draw = ImageDraw.Draw(img)


# load icon files and masks
for icon in glob.glob(os.path.join(PATH, "icon-*.png")):
    icon_name = icon.split("icon-")[1].replace(".png", "") 
    icon_image = Image.open(icon)
    icons[icon_name] = icon_image
    mask[icon_name] = create_mask(icon_image)


intuitive_font = ImageFont.truetype(intuitive, int(22 * SCALE_SIZE))

img.paste(icons[time_icon], (), masks[time_icon])
inky_display.set_image(img)
inky_display.show()


# eof  


