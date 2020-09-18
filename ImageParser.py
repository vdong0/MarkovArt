from PIL import Image

class ImageParser(object):

    """
    Converts an image into a list of RGB values
    """
    def image_to_list(self, image):

        image = image.convert('RGB')
        rgb_list = []
        width, height = image.size

        for y in range (0, height):
            for x in range (0, width):
                r, g, b = image.getpixel((x, y))
                rgb_list.append((r, g, b))

        return rgb_list

    """
    Converts an RGB list into an image
    """
    def list_to_image(self, rgb_list, width, height):
        size = (width, height)
        image = Image.new('RGB', size, (0,0,0))
        pixels = image.load()

        y = 0
        for pix in range(0, width*height):
            r, g, b = rgb_list[pix]

            x = pix % width
            if x == 0:
                y += 1

            pixels[x, y-1] = (int(r), int(g), int(b))

        return image
