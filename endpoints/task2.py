from litellm import completion
from typing import List, Dict
import os

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("GROQ_API_KEY not defined")


def generate_response(messages: List[Dict]) -> str:
    """Gera resposta usando Groq via LiteLLM."""
    response = completion(
        model="groq/llama-3.1-8b-instant",
        messages=messages,
        max_tokens=1024,
        api_key=api_key,
    )
    return response.choices[0].message.content


def main() -> None:
    messages = [
        {
            "role": "system",
            "content": "You are an expert software engineer that prefers functional programming.",
        },
        {
            "role": "user",
            "content": "Write a function to swap the keys and values in a dictionary.",
        },
    ]

    response = generate_response(messages)
    print(response)


if __name__ == "__main__":
    main()