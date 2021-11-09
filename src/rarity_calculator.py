import random
import time


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


def order_index_rarity(index):

    return 1/index


def slice_index_rarity(index):
    '''
    [
        [2/3, 1, 2/3],
        [1, 2, 1], 
        [2/3, 1, 2/3]
    ]
    '''
    CONVERTER_LIST = [2/3, 1, 2/3, 1, 2, 1, 2/3, 1, 2/3]

    return CONVERTER_LIST[index - 1]


def rotation_index_rarity(index):
    '''
    [
        [1, 1/3],
        [1/3, 2/3]
    ]
    '''

    CONVERTER_LIST = [1, 1/3, 2/3, 1/3]

    return CONVERTER_LIST[index - 1]


store = collection()
collection1 = []

while len(store) != 0:

    sample = random.sample(store, 9)
    collection1.append(sample)

    store = set(store) - set(sample)

rarity_store = []
for i, image in enumerate(collection1):

    rarity = 0

    for piece in image:

        rarity += 1000 / \
            piece[0] * slice_index_rarity(piece[1]) * \
            rotation_index_rarity(piece[2])

    rarity_store.append({i: {
        "rarity": rarity,
        "image": image
    }})

print(rarity_store)
