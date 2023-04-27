import os
import openai

from dotenv import load_dotenv
load_dotenv()

# Load your API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def completion_example():
    return openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)


if __name__ == '__main__':
    print(completion_example())

