# this script uses chatgpt api to ask question to ChatGPT

import os
import openai

# Get your API key from the environment variable
api_key = os.environ.get('OPENAI_API_KEY')

# Check if the API key is set
if api_key is None:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

# Your question or prompt
question = "Translate the following English text to French: 'Hello, how are you?'"

# Send a request to the OpenAI API
response = openai.Completion.create(
    engine="text-davinci-002",  # You can choose an appropriate engine
    prompt=question,
    max_tokens=50,  # You can adjust the token limit based on your needs
    api_key=api_key
)

# Extract and print the answer
answer = response.choices[0].text
print(answer)
