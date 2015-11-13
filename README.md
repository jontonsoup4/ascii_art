#What is ascii_art?
`ascii_art` easily converts images into ascii artwork. 

# Example script
Reads `cat.jpg`, upscales the quality by 5, saves a rendering to `cat_draw.jpg`, and saves a text file containing the raw ASCII.
```
from ascii_art import ASCIIArt, ASCIIPicture

picture = ASCIIArt('cat.jpg', 5).draw()
ASCIIPicture(picture).save('cat_draw.jpg')

with open('cat_draw.txt', 'w') as f:
    f.write(picture)
```

##Before
![Before](https://github.com/jontonsoup4/ascii_art/blob/master/examples/cat.jpg)
##After 
![After](https://github.com/jontonsoup4/ascii_art/blob/master/examples/cat_scale5_draw.png)

#Setup
`python3 setup.py install`

#Dependencies
`Pillow==3.0.0`
