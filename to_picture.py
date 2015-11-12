from PIL import Image, ImageDraw


class ASCIIPicture:
    def __init__(self, text):
        """
        :param text: ASCII text

        """
        dummy = Image.new('RGB', (0, 0))
        d = ImageDraw.Draw(dummy)
        d.text((0, 0), text, fill=(255, 255, 255))
        width, height = d.textsize(text)
        self.width = width
        self.height = height
        self.ratio = self.width / self.height
        self.img = Image.new('RGB', (self.width, self.height), (255, 255, 255))
        d = ImageDraw.Draw(self.img)
        d.text((0, 0), text, fill=(0, 0, 0))

    def save(self, save_name, new_height=0):
        """
        :param save_name: path to desired save location
        :param new_height: optional parameter for new y size

        """
        if new_height == 0:
            self.img.save(save_name)
        else:
            self.height = new_height
            self.width = int(new_height * self.ratio)
            self.img = self.img.resize((self.width, self.height), Image.BILINEAR)
            self.img.save(save_name)


    def show(self):
        self.img.show()
