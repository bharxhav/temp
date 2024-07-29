import random
from PIL import Image, ImageDraw


def generate_image(output_path, size=(400, 400)):

    image = Image.new('RGB', size, color='white')
    draw = ImageDraw.Draw(image)

    start = (random.randint(0, size[0]), random.randint(0, size[1]))
    end = (random.randint(0, size[0]), random.randint(0, size[1]))

    draw.line([start, end], fill='black', width=2)

    image.save(output_path)
