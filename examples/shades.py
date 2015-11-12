from ascii_art import ASCIIArt, ASCIIPicture
from PIL import Image, ImageDraw
from collections import OrderedDict

raw = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]{}\|;:'",./<>?`~'''
text = ""
for i in raw:
    text += (i * 50 + '\n')*25
ASCIIPicture(text).save('shades.png', 94)
raw = list(raw)
im = Image.open('shades.png', 'r')
shades = []
for y in range(im.size[1]):
    shades.append(255 - im.getpixel((0, y))[0])
print(''.join([x for (y, x) in sorted(zip(shades, raw))]))