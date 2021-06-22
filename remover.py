
from PIL import Image


def remove_watermark(path_to_image):
    image = Image.open(path_to_image)
    pixelmap = image.load()
    things = set()
    for i in range(image.size[0]):
        for j in range(image.size[1]):

            if pixelmap[i,j][0:3] != (0,0,0) or pixelmap[i,j][-1]<39:
                pixelmap[i,j] = (255,255,255,255)

    print(things)
    image.show()


remove_watermark(r"C:\Users\Murat\Downloads\tech_1.png")