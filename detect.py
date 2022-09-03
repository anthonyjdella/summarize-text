import io
import os
from urllib import response
from google.cloud import vision


def detect_text():
    client = vision.ImageAnnotatorClient()

    file_name = os.path.abspath('resources/image.jpg')

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    return(texts[0].description)
