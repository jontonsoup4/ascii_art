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
        self.img = Image.new('RGB', (width, height), (255, 255, 255))
        d = ImageDraw.Draw(self.img)
        d.text((0, 0), text, fill=(0, 0, 0))

    def save(self, save_name):
        """
        :param save_name: path to desired save location

        """
        self.img.save(save_name)

    def show(self):
        self.img.show()
