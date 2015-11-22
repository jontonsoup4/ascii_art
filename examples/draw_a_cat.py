from ascii_art.ascii_art import ASCIIArt, ASCIIPicture

# ASCII drawing
picture = ASCIIArt('cat', 2).draw_ascii(curve=1)
ASCIIPicture(picture).save('cat_scale2_draw_ascii.png')
with open('cat_scale2_draw.txt', 'w') as f:
    f.write(''.join(picture))

picture = ASCIIArt('cat', 5).draw_ascii(curve=1)
ASCIIPicture(picture).save('cat_scale5_draw_ascii.png')
with open('cat_scale5_draw.txt', 'w') as f:
    f.write(''.join(picture))

# Colored ASCII drawing using sorted custom character sets on a black background
colored_picture = ASCIIArt('cat', 2).draw_color_ascii(ASCIIArt.sort('09215'))
ASCIIPicture(colored_picture, 'black').save('cat_scale2_color_numbers')

colored_picture = ASCIIArt('cat', 5).draw_color_ascii(ASCIIArt.sort('09215'))
ASCIIPicture(colored_picture, 'black').save('cat_scale5_color_numbers')

colored_picture = ASCIIArt('cat', 2).draw_color_ascii(ASCIIArt.sort('jontonsoup4'))
ASCIIPicture(colored_picture, 'black').save('cat_scale2_color_name')

colored_picture = ASCIIArt('cat', 5).draw_color_ascii(ASCIIArt.sort('jontonsoup4'))
ASCIIPicture(colored_picture, 'black').save('cat_scale5_color_name')

# ASCII to HTML
html = ASCIIArt('cat', 2).draw_html()
with open('cat_scale2_html.html', 'w') as f:
    f.write(''.join(html))

html = ASCIIArt('cat', 5).draw_html()
with open('cat_scale5_html.html', 'w') as f:
    f.write(''.join(html))

# ASCII to HTML using only # on a black background
html = ASCIIArt('cat', 2).draw_html(ASCIIArt.BLOCK, background_color='black')
with open('cat_scale2_html_block.html', 'w') as f:
    f.write(''.join(html))

html = ASCIIArt('cat', 5).draw_html(ASCIIArt.BLOCK, background_color='black')
with open('cat_scale5_html_block.html', 'w') as f:
    f.write(''.join(html))

# Colored ASCII with only # on a black background
colored_picture = ASCIIArt('cat', 2).draw_color_ascii(ASCIIArt.BLOCK, curve=1.5)
ASCIIPicture(colored_picture, 'black').save('cat_scale2_block_color.png')

colored_picture = ASCIIArt('cat', 5).draw_color_ascii(ASCIIArt.BLOCK, curve=1.5)
ASCIIPicture(colored_picture, 'black').save('cat_scale5_block_color.png')

# Colored ASCII with full grayscale
colored_picture = ASCIIArt('cat', 2).draw_color_ascii(ASCIIArt.FULL_RANGE, curve=1.5)
ASCIIPicture(colored_picture).save('cat_scale2_full_range_color.png')

colored_picture = ASCIIArt('cat', 5).draw_color_ascii(ASCIIArt.FULL_RANGE, curve=1.5)
ASCIIPicture(colored_picture).save('cat_scale5_full_range_color.png')