# What is ascii_art?
`ascii_art` easily converts images into ascii artwork. `ascii_art` now supports colored ascii art as well as the ability to convert colored ascii to html.

# Example script
For a full example script, see [draw_a_cat.py](https://github.com/jontonsoup4/ascii_art/blob/master/examples/draw_a_cat.py).  
For a full list of example output, see [examples](https://github.com/jontonsoup4/ascii_art/tree/master/examples).  
[Working colored HTML of an ASCII kitten using the character set 'kitten'](http://htmlpreview.github.com/?https://github.com/jontonsoup4/ascii_art/blob/master/examples/cat_scale2_html_kitten.html)

Reads `cat.jpg`, upscales the quality by 5, saves an ASCII rendering to `cat_scale5_draw_ascii.png`, saves a colored ASCII rendering to `cat_scale5_full_range_color.png`, and saves a text file containing the raw ASCII.
```
from ascii_art import ASCIIArt, ASCIIPicture

picture = ASCIIArt('cat', 5).draw_ascii(curve=1)
ASCIIPicture(picture).save('cat_scale5_draw_ascii.png')

colored_picture = ASCIIArt('cat', 5).draw_color_ascii(ASCIIArt.FULL_RANGE, curve=1.5)
ASCIIPicture(colored_picture).save('cat_scale5_full_range_color.png')

with open('cat_scale5_draw.txt', 'w') as f:
    f.write(''.join(picture))
```

## Before
![Before](https://github.com/jontonsoup4/ascii_art/blob/master/examples/cat.jpg)
## After ASCII
![After](https://github.com/jontonsoup4/ascii_art/blob/master/examples/cat_scale5_draw_ascii.png)
## After ASCII Color
![After](https://github.com/jontonsoup4/ascii_art/blob/master/examples/cat_scale5_full_range_color.png)

# Setup
`python3 setup.py install`

# Dependencies
`Pillow==3.0.0`

