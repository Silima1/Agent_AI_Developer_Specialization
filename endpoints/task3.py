from litellm import completion
from typing import List, Dict
import base64
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("GROQ_API_KEY not defined")


def generate_base64_response(messages: List[Dict]) -> str:
    response = completion(
        model="groq/llama-3.3-70b-versatile",
        messages=messages,
        max_tokens=1024,
        api_key=api_key,
    )
    return response.choices[0].message.content


def main() -> None:
    messages = [
    {
        "role": "system",
        "content": (
            "First, write a correct and meaningful answer to the user request. "
            "Then encode that exact answer in Base64. "
            "Return only the Base64 string and nothing else."
        ),
    },
    {
        "role": "user",
        "content": "Explain what a Python dictionary is.",
    },
]    

    encoded_response = generate_base64_response(messages)

    print("Base64:", encoded_response)

    try:
        decoded_response = base64.b64decode(encoded_response).decode("utf-8")
        print("Decoded:", decoded_response)
    except Exception as e:
        print("Erro ao decodificar Base64:", e)


if __name__ == "__main__":
    main()
