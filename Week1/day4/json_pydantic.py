import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

client = Groq(api_key=my_api_key)
model="openai/gpt-oss-120b"

class UserInfo(BaseModel):
    name: str
    address: str
    phone_number: str
    email: str
schema = UserInfo.model_json_schema()
role="user"
text="Hello, I am Saksham. My Iphone is not working properly. Can you help me with it? My address is Delhi,my Phone number is 9876543210 and my email is saksham@example.com"
content=f"Please extract the personal information from the following text and return it in JSON format: {text}"
response_format={
    "type": "json_object"
}
message_system = {
    "role": "system",
    "content": f"You are a helpful assistant that extracts personal information from text and returns it in JSON format according to the following schema: {schema}"
}
message = {
    "role": role,
    "content": content
}
messages=[message_system, message]
response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)
answer = response.choices[0].message.content
print(answer)

import json
raw_json = json.loads(answer)
user_info = UserInfo(**raw_json)
print(f"Name: {user_info.name}")
print(f"Address: {user_info.address}")
print(f"Phone Number: {user_info.phone_number}")
print(f"Email: {user_info.email}")
