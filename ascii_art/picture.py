from PIL import Image, ImageDraw


class ASCIIPicture:

    def __init__(self, text, background_color='white'):
        """
        Class for saving and displaying ASCII art. Automatically checks if the text is in color. Background can be
        hex, rgb, or html color name.

        :param text: ASCII text
        :param background_color: color of the background. Takes standard html names

        """
        self.text = text
        dummy = Image.new('RGB', (0, 0))
        d = ImageDraw.Draw(dummy)
        text = ''.join([char[0] for char in text])
        d.text((0, 0), text, fill=(255, 255, 255))
        width, height = d.textsize(text)
        self.width = width
        self.height = height
        self.ratio = self.width / self.height
        self.img = Image.new('RGB', (self.width, self.height), background_color)
        d = ImageDraw.Draw(self.img)
        if type(self.text[0]) == list:
            text = ''.join([x[0] for x in self.text])
            colors = [x[1] for x in self.text]
            lines = len([x for x in text if x == '\n'])
            if lines == 0:
                print('Try using draw_color_ascii instead')
                exit()
            char_in_line = int(len(text) / lines)
            move_y = float(self.width / (char_in_line - 1))
            move_x = float(self.height / lines)
            char = 0
            for x in range(lines):
                for y in range(char_in_line):
                    d.text((y * move_y, x * move_x), text[char], fill=colors[char])
                    char += 1
        else:
            d.text((0, 0), text, fill=(0, 0, 0))

    def save(self, save_name, new_height=0):
        """
        :param save_name: path to desired save location
        :param new_height: optional parameter for new y size

        """
        if '.' not in save_name:
            save_name += '.png'
        if new_height == 0:
            self.img.save(save_name)
        else:
            self.height = new_height
            self.width = int(new_height * self.ratio)
            self.img = self.img.resize((self.width, self.height), Image.BILINEAR)
            self.img.save(save_name)

    def show(self, new_height=0):
        """
        :param new_height: optional parameter for new y size

        """
        if new_height == 0 or type(new_height) == str:
            self.img.show()
        else:
            self.height = new_height
            self.width = int(new_height * self.ratio)
            self.img = self.img.resize((self.width, self.height), Image.BILINEAR)
            self.img.show()
