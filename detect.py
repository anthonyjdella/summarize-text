import io
import os
import requests
from google.cloud import vision


def save_image(image_url):
    img_data = requests.get(image_url).content
    with open('resources/image.jpg', 'wb') as handler:
        handler.write(img_data)


def detect_text():
    client = vision.ImageAnnotatorClient()

    file_name = os.path.abspath('resources/image.jpg')

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    return(texts[0].description)
