from PIL import Image


class ASCIIArt:
    GRAYSCALE = " .,:'`\";~-_|/=\<+>?)*^(!}{v[I&]wrcVisJmYejoWn%Xtzux17lCFLT3fSZ2a@y4GOKMU#APk605Ed8Qb9NhBDHRqg$p"
    FULL_RANGE = GRAYSCALE
    HALF_RANGE = GRAYSCALE[::2]
    QUARTER_RANGE = GRAYSCALE[::4]
    EIGHTH_RANGE = GRAYSCALE[::8]
    BLOCK = "#"

    def __init__(self, picture_path, scale=1):
        """
        Converts an image to ASCII Art

        :param picture_path: path to ascii_picture name including extension
        :param scale: 1 is roughly the original grey_image size. Can be larger (3), can be smaller (1/4)
        """
        if '.' not in picture_path:
            picture_path += '.jpg'
        self.picture_path = picture_path
        self.color_image = Image.open(picture_path)
        self.scale = 7 / scale
        self.width = int(self.color_image.size[0] / self.scale)
        self.height = int(self.color_image.size[1] / (self.scale * 1.8))
        self.color_image = self.color_image.resize((self.width, self.height), Image.BILINEAR)
        self.grey_image = self.color_image.convert("L")
        self.ascii_picture = []

    def draw_ascii(self, char_list=' .:-=+*#%@', high_pass=0, low_pass=0, curve=1.2):
        """
        Draws ASCII art using the given parameters. Using an alternate char_set allows for custom ASCII. Use
        sort() to return the correct order if you aren't sure what the greyscale order of the character set is.

        :param char_list: sets the characters used in ASCII rendering
        :param high_pass: 1 to 100 removes darker areas
        :param low_pass: 1 to 100 removes lighter
        :param curve: defaults to linear. curve > 1 is lighter. 1 > curve > 0 is darker. curve < 0 is grey
        :return: list of all characters in the ASCII piece. Use .join() to display the text

        """
        for y in range(0, self.grey_image.size[1]):
            for x in range(0, self.grey_image.size[0]):
                brightness = 255 - self.grey_image.getpixel((x, y))
                if curve < 1:
                    choice = int(brightness * (len(char_list) / 255) ** curve)
                else:
                    choice = int(len(char_list) * (brightness / 255) ** curve)
                if choice >= len(char_list):
                    choice = len(char_list) - 1
                self.ascii_picture.append(char_list[choice])
            self.ascii_picture.append("\n")
        if low_pass > 0:
            low_pass = int(low_pass * len(char_list) / 100)
            for i in range(low_pass):
                self.ascii_picture = [char.replace((char_list[i]), ' ') for char in self.ascii_picture]
        if high_pass > 0:
            high_pass = int(high_pass * len(char_list) / 100)
            for i in range(high_pass):
                self.ascii_picture = [char.replace((char_list[-i]), ' ') for char in self.ascii_picture]
        return self.ascii_picture

    def draw_color_ascii(self, char_list=' .:-=+*#%@', high_pass=0, low_pass=0, curve=1.2):
        """
        Color adaptation of draw_ascii.

        :param char_list: sets the characters used in ASCII rendering
        :param high_pass: 1 to 100 removes darker areas
        :param low_pass: 1 to 100 removes lighter
        :param curve: defaults to linear. curve > 1 is lighter. 1 > curve > 0 is darker. curve < 0 is grey
        :return: list of lists. list[0] contains ASCII character, list[1] contains color value

        """
        ascii_picture = self.draw_ascii(char_list, high_pass, low_pass, curve)
        color_code = self.get_color_codes()
        ascii_color = []
        count = 0
        for index, char in enumerate(ascii_picture):
            if char != '\n':
                ascii_color.append([char, color_code[count]])
                count += 1
            else:
                ascii_color.append([char, '#000000'])
        return ascii_color

    def draw_html(self, char_list=' .:-=+*#%@', high_pass=0, low_pass=0, curve=1.2, background_color='white'):
        """
        HTML adaptation of draw_ascii. Formats colored ASCII to HTML

        :param char_list: sets the characters used in ASCII rendering
        :param high_pass: 1 to 100 removes darker areas
        :param low_pass: 1 to 100 removes lighter
        :param curve: defaults to linear. curve > 1 is lighter. 1 > curve > 0 is darker. curve < 0 is grey
        :return: string of HTML formatting

        """
        init_draw = self.draw_ascii(char_list, high_pass, low_pass, curve)
        ascii_picture = [char for char in init_draw if char != '\n']
        num_breaks = len(init_draw) - len(ascii_picture)
        hex_codes = self.get_color_codes()
        html = ['<body bgcolor={}><pre>'.format(background_color)]
        for index, char in enumerate(ascii_picture):
            if index % (len(ascii_picture) / num_breaks) == 0 and index > 0:
                html.append('<br>')
            html.append('<span style="color: {0};">{1}</span>'.format(hex_codes[index], char))
        html.append('</pre></body>')
        return ''.join(html)

    def get_color_codes(self, mode='hex'):
        """
        Gets the color value of every pixel in the transformed picture

        :param mode: hex or rgb
        :return: list of color codes in the picture

        """
        color_codes = []
        for y in range(0, self.color_image.size[1]):
            for x in range(0, self.color_image.size[0]):
                r, g, b, = self.color_image.getpixel((x, y))
                if mode.lower() == 'hex':
                    color_codes.append('#{:02x}{:02x}{:02x}'.format(r, g, b))
                elif mode.lower() == 'rgb':
                    color_codes.append((r, g, b))
                else:
                    print('Please choose hex or rgb')
        return color_codes

    @staticmethod
    def sort(char_list):
        """
        Sorts a string of characters from lightest to darkest when represented in ASCII art

        :param char_list: string of characters
        :return: sorted string of characters from lightest to darkest

        """
        output = []
        for i in char_list:
            output.append([i, ASCIIArt.GRAYSCALE.index(i)])
        output = [x for (x, y) in sorted(output, key=lambda x: x[1])]
        return ''.join(output)