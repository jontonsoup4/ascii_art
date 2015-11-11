from ascii_art import ASCIIArt, ASCIIPicture

picture = ASCIIArt('cat.jpg').draw()
ASCIIPicture(picture).save('cat_draw.jpg')

with open('cat_draw.txt', 'w') as f:
    f.write(picture)