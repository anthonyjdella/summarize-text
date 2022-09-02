import requests


def save_image(image_url):
    img_data = requests.get(image_url).content
    with open('resources/image.jpg', 'wb') as handler:
        handler.write(img_data)
