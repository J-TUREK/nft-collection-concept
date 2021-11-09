from PIL import Image
import random
from os import path


def collection(n=100):
    '''
    Collection of tuples representing the images, sliced and rotated
    '''

    collection = range(1, n + 1)

    store = []

    for original_image in collection:

        # split each image into 9 pieces.
        for i in range(1, 10):

            # create 4 copies of the piece, each representing a unique rotation
            for x in range(1, 5):

                store.append((original_image, i, x))

    return store


def string_builder(pieces):

    string = ""

    for p in pieces:

        string_section = f"({p[0]}-{p[1]}-{p[2]})"

        string += string_section

    return string


store = collection()

while len(store) != 0:

    sample = random.sample(store, 9)

    im_path_list = []
    for p in sample:

        filename = f"circasso{p[0]}_{p[1]}_{p[2]}.jpeg"
        filepath = path.join("rotated_collection1", filename)
        im_path_list.append(filepath)

    images = list(map(Image.open, im_path_list))
    widths, heights = zip(*(i.size for i in images))

    new_im = Image.new('RGB', (int(sum(widths) / 3), int(sum(heights) / 3)))

    for x in range(3):

        for y in range(3):

            index = (x * 3) + y
            im = Image.open(im_path_list[index - 1])

            x_offset = int(x * im.width)
            y_offset = int(y * im.height)

            new_im.paste(im, (x_offset, y_offset))

    name = string_builder(sample)
    new_im.save(f"circasso_collection1/circasso_{name}.jpeg")

    store = set(store) - set(sample)
