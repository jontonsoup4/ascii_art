from ascii_art import ASCIIArt, ASCIIPicture

picture = ASCIIArt('cat.jpg', 2).draw(curve=1)
ASCIIPicture(picture).save('cat_scale2_draw.png')
with open('cat_scale2_draw.txt', 'w') as f:
    f.write(picture)
    f.close()

picture = ASCIIArt('cat.jpg', 3).draw(curve=1)
ASCIIPicture(picture).save('cat_scale3_draw.png')
with open('cat_scale3_draw.txt', 'w') as f:
    f.write(picture)
    f.close()

picture = ASCIIArt('cat.jpg', 5).draw(curve=1)
ASCIIPicture(picture).save('cat_scale5_draw.png')
with open('cat_scale5_draw.txt', 'w') as f:
    f.write(picture)
    f.close()

picture = ASCIIArt('cat.jpg', 2).half_range(curve=1.5)
ASCIIPicture(picture).save('cat_scale2_halfrange.png')
with open('cat_scale2_halfrange.txt', 'w') as f:
    f.write(picture)
    f.close()

picture = ASCIIArt('cat.jpg', 3).half_range(curve=1.5)
ASCIIPicture(picture).save('cat_scale3_halfrange.png')
with open('cat_scale3_halfrange.txt', 'w') as f:
    f.write(picture)
    f.close()

picture = ASCIIArt('cat.jpg', 5).half_range(curve=1.5)
ASCIIPicture(picture).save('cat_scale5_halfrange.png')
with open('cat_scale5_halfrange.txt', 'w') as f:
    f.write(picture)
    f.close()

picture = ASCIIArt('cat.jpg', 2).full_range(curve=1.5)
ASCIIPicture(picture).save('cat_scale2_fullrange.png')
with open('cat_scale2_fullrange.txt', 'w') as f:
    f.write(picture)
    f.close()

picture = ASCIIArt('cat.jpg', 3).full_range(curve=1.5)
ASCIIPicture(picture).save('cat_scale3_fullrange.png')
with open('cat_scale3_fullrange.txt', 'w') as f:
    f.write(picture)
    f.close()

picture = ASCIIArt('cat.jpg', 5).full_range(curve=1.5)
ASCIIPicture(picture).save('cat_scale5_fullrange.png')
with open('cat_scale5_fullrange.txt', 'w') as f:
    f.write(picture)
    f.close()