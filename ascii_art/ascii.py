from PIL import Image


class ASCIIArt:
    def __init__(self, picture_name, scale=1):
        """
        Converts an image to ASCII Art
        :param picture_name: path to picture name including extension
        :param scale: 1 is roughly the original image size. Can be larger (3), can be smaller (1/4)

        """
        self.picture_name = picture_name
        self.image = Image.open(picture_name)
        self.scale = 7 / scale
        self.width = int(self.image.size[0] / self.scale)
        self.height = int(self.image.size[1] / (self.scale * 1.8))
        self.image = self.image.resize((self.width, self.height), Image.BILINEAR).convert("L")
        self.picture = ""
        self.grayscale = " .,:'`\";~-_|/=\<+>?)*^(!}{v[I&]wrcVisJmYe" \
                         "joWn%Xtzux17lCFLT3fSZ2a@y4GOKMU#APk605Ed8Qb9NhBDHRqg$p"

    def draw(self, char_list=' .:-=+*#%@', highpass=0, lowpass=0, curve=1.2):
        """
        :param char_list: sets the characters used in ASCII rendering. Allows for custom char set
        :param highpass: 1 to 100 removes darker areas
        :param lowpass: 1 to 100 removes lighter
        :param curve: defaults to linear. curve > 1 is lighter. 1 > curve > 0 is darker. curve < 0 is grey

        """
        for y in range(0, self.image.size[1]):
            for x in range(0, self.image.size[0]):
                brightness = 255 - self.image.getpixel((x, y))
                if curve < 1:
                    choice = int(brightness * (len(char_list) / 255) ** curve)
                else:
                    choice = int(len(char_list) * (brightness / 255) ** curve)
                if choice >= len(char_list):
                    choice = len(char_list) - 1
                self.picture += char_list[choice]
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

    def full_range(self, highpass=0, lowpass=0, curve=1.2):
        self.draw(self.grayscale, highpass, lowpass, curve)
        return self.picture

    def half_range(self, highpass=0, lowpass=0, curve=1.2):
        self.draw(self.grayscale[::2], highpass, lowpass, curve)
        return self.picture

    def sort_grayscale(self, char_list):
        output = []
        for i in char_list:
            output.append([i, self.grayscale.index(i)])
        output = [x for (x, y) in sorted(output, key=lambda x: x[1])]
        return ''.join(output)

