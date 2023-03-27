# Yiska Levi

from PIL import Image


def rmember(path):
    msg = ''
    img = Image.open(path)
    for i in range(img.width):
        for j in range(img.height):
            pixel_color = img.getpixel((i, j))
            if pixel_color == 1:
                msg=msg+chr(j)
    return msg

path_img = 'resources/code.png'
if __name__ == '__main__':
    print(rmember(path_img))
