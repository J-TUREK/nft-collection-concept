from PIL import Image

for image_index in range(1, 101):

    name = f"circasso{image_index}.jpeg"

    i = Image.open(f'collection1/{name}')

    width = i.width
    height = i.height

    for x in range(3):

        for y in range(3):

            index = (x * 3) + 1 + y

            img = i.crop((x * width/3, y * height/3,
                          x * width/3 + width/3, y * height/3 + height/3))

            img.save(f'sliced_collection1/circasso{image_index}_{index}.jpeg')


def slice_image(filename, N):
    '''
    Re-usable function
    '''

    i = Image.open(N)

    width = i.width
    height = i.height

    for x in range(N):

        for y in range(N):

            index = (x * N) + 1 + y

            img = i.crop((x * width/N, y * height/N,
                          x * width/N + width/N, y * height/N + height/N))

            img.save(f"{filename}_{index}.jpeg")
