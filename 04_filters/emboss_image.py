# emboss_image.py

from PIL import Image
from PIL import ImageFilter


def emboss(input_image: str, output_image: str) -> None:
    image = Image.open(input_image)
    filtered_image = image.filter(ImageFilter.EMBOSS)
    filtered_image.save(output_image)


if __name__ == "__main__":
    emboss("hummingbird.jpg", "hummingbird_emboss.jpg")