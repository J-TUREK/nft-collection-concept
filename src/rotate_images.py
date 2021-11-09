from PIL import Image

for i in range(1, 101):
    # For each unique image

    for n in range(9):
        # For each slice of the image

        name = f"circasso{i}_{n + 1}.jpeg"
        img = Image.open(f'sliced_collection1/{name}')

        for k in range(4):
            # Rotate and save 4 times

            im = img.rotate(k * 90, expand=True)

            im.save(f"rotated_collection1/circasso{i}_{n + 1}_{k + 1}.jpeg")
