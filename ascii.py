from PIL import Image


class ASCIIArt:
    def __init__(self, picture_name, scale=1):
        """
        Converts an image to ASCII Art
        :param picture_name: path to picture name including extension
        :param scale: 1/4

        """
        self.picture_name = picture_name
        self.image = Image.open(picture_name)
        self.scale = 7/ scale
        self.width = int(self.image.size[0] / self.scale)
        self.height = int(self.image.size[1] / (self.scale * 1.8))
        self.image = self.image.resize((self.width, self.height), Image.BILINEAR).convert("L")
        self.picture = ""
        self.grayscale = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    def draw(self, char_list=' .:-=+*#%@', highpass=0, lowpass=0):
        """
        :param char_list: sets the characters used in ASCII rendering. Allows for custom char set
        :param highpass: 1 to 100 removes darker areas
        :param lowpass: 1 to 100 removes lighter areas

        """
        for y in range(0, self.image.size[1]):
            for x in range(0, self.image.size[0]):
                brightness = 255 - self.image.getpixel((x, y))
                row = int(brightness * len(char_list) / 255)
                self.picture += char_list[row]
            self.picture += "\n"
        if lowpass > 0:
            lowpass = int(lowpass * len(char_list) / 100)
            for i in range(lowpass):
                self.picture = self.picture.replace((char_list[i]), ' ')
        if highpass > 0:
            highpass = int(highpass * len(char_list) / 100)
            for i in range(highpass):
                self.picture = self.picture.replace((char_list[-i]), ' ')
        return self.picture

    def full_range(self, limiter=0):
        self.draw(self.grayscale, limiter)
        return self.picture

    def half_range(self, limiter=0):
        self.draw(self.grayscale[::2], limiter)
        return self.picture
