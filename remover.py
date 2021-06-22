
from PIL import Image


def remove_watermark(path_to_image, folder_to_save = None, name_to_save = "removed",):
    image = Image.open(path_to_image)
    pixelmap = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):

            if pixelmap[i,j][0:3] != (0,0,0) or pixelmap[i,j][-1]<39:
                pixelmap[i,j] = (255,255,255,255)


    if folder_to_save is not None:
        image.save(folder_to_save + r"\ "[:-1] + name_to_save + ".png")
    return image


remove_watermark(r"imagepath",
                 r"savepath",
                 "removed1")