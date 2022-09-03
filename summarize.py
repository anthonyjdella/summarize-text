import os
import openai
from dotenv import load_dotenv
from detect import detect_text
from utilities import save_image


load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")


def get_text_from_image(url):
    save_image(url)
    return detect_text()


def generate_prompt(url):
    return f"In one-sentence, summarize the following text: \n {get_text_from_image(url)} \n"


def summarize_prompt(url):
    response = openai.Completion.create(
        #model, prompt, temperature, max_tokens
        
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    print(response.choices[0].text)
    return(response.choices[0].text)


# summarize_prompt('./resources/test.jpg')
