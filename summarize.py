import os
import openai
from dotenv import load_dotenv
from detect import detect_text
from detect import save_image


load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")


def get_text_from_image(path):
    save_image(path)
    return detect_text()


def generate_prompt(path):
    return f"In one-sentence, summarize the following text: \n {get_text_from_image(path)} \n"


def summarize_prompt(path):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=generate_prompt(path),
        temperature=0.8,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    print(response.choices[0].text)
    return(response.choices[0].text)


# summarize_prompt('./resources/test.jpg')