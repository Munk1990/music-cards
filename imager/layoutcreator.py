from PIL import Image, ImageDraw

dpi = 300
mmtoinch = 0.0393700787


def generate_canvas(heightmm, widthmm):
    widthpixel = int(widthmm * mmtoinch * dpi)
    heightpixel = int(heightmm * mmtoinch * dpi)
    mode = 'RGB'
    size = (widthpixel, heightpixel)
    color = (255, 255, 255)
    im = Image.new(mode, size, color)
    return im


def partition_canvas(image, columns, rows, color, linewidth):
    height = image.size[0]
    width = image.size[1]
    draw = ImageDraw.Draw(image)
    for col in range(columns - 1):
        distance = (int((col + 1) * width / columns))
        draw.line((distance, 0, distance, height), fill=color, width=linewidth)

    for row in range(rows - 1):
        distance = int((row + 1) * height / rows)
        draw.line((0, distance, width, distance), fill=color, width=linewidth)


def draw_border(im, height, width, outlinecolor, linewidth):
    draw = ImageDraw.Draw(im)
    draw.rectangle((0, 0, width, height), outline=outlinecolor, width=linewidth)


im = generate_canvas(277, 203)
partition_canvas(im, 2, 4, im.size[0], im.size[1], (0, 0, 0), 3)
im.save("C:/Users/mayan/Workspace/music-cards/outputs/test2.jpg")
im.show()
