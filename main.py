import os
import openai

from dotenv import load_dotenv
load_dotenv()

# Load your API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

COCA_COLA_COLOR = "#FF2400"

def completion_example():
    return openai.Completion.create(model="text-davinci-003", prompt="Is Cristian handsome?", temperature=0)

def create_new_image(prompt="A promotional banner of coca-cola"):
    response = openai.Image.create(prompt=prompt, size="256x256", n=1)
    return response['data'][0]['url']

def edit_image():
    response = openai.Image.create_edit(
        image=open("resources/coca-cola.png", "rb"),
        prompt=(f'A bottle of coca-cola on the right side surrounded by a background using the color {COCA_COLA_COLOR}'),
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

if __name__ == '__main__':
    # print(create_new_image("An photographic image of a coca-cola bottle and a pringles package next to it over a white background"))
    print(edit_image())
