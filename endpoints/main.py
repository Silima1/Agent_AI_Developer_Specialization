from openai import OpenAI
import os

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RecursionError("GROQ_API_KEY no enviroment defined")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "Say Hello how can I help you"}
    ]
)
print(response.choices[0].message.content)