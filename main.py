import os
import openai

from dotenv import load_dotenv
load_dotenv()

# Load your API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def completion_example():
    return openai.Completion.create(model="text-davinci-003", prompt="Is Cristian handsome?", temperature=0)

def create_new_image():
    response = openai.Image.create(prompt="A promotional banner of coca-cola", size="256x256", n=1)
    return response['data'][0]['url']

if __name__ == '__main__':
    print(create_new_image())
