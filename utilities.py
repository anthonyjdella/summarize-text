import requests


def save_image(img_url):
    img_data = requests.get(img_url).content
    with open('image.jpg', 'wb') as handler:
        handler.write(img_data)
