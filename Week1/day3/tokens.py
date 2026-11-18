import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

client = Groq(api_key=my_api_key)
model="openai/gpt-oss-120b"
role="user"
content1="Hello"
content2="Write a poem about the sun."
content3="Write a 1000-word essay on climate change."
contents=[content1, content2, content3]
for content in contents:
  message = {
      "role": role,
      "content": content
  }
  messages=[message]
  response = client.chat.completions.create(model=model, messages=messages)
  usage=response.usage
  print(f"Prompt tokens: {usage.prompt_tokens}, Completion tokens: {usage.completion_tokens}, Total tokens: {usage.total_tokens}")
# print(response.choices[0].message.content)