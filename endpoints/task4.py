"""
Problema:
Gerar automaticamente a implementação de uma função com base numa especificação
estruturada em JSON enviada para um LLM.

Neste exemplo, a especificação descreve uma função chamada `swap_keys_values`,
que deve trocar as chaves pelos valores de um dicionário. O dicionário de entrada
deve ter valores únicos, para evitar colisões ao inverter chave/valor.

Objetivo:
- Enviar a especificação em JSON para o modelo
- Pedir ao modelo para implementar a função em Python
- Receber e imprimir apenas o código gerado

Problema:
Gerar automaticamente a implementação de uma função com base numa especificação
estruturada em JSON enviada para um LLM.
"""
import json
import os
import re
from typing import List, Dict, Any
from dotenv import load_dotenv
from litellm import completion

# BLOCO 1: carregar variáveis de ambiente
load_dotenv()

# BLOCO 2: validar API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY not defined")

# BLOCO 3: definir modelo
MODEL = "groq/llama-3.3-70b-versatile"


# BLOCO 4: chamar o modelo
def generate_response(messages: List[Dict[str, str]]) -> str:
    response = completion(
        model=MODEL,
        messages=messages,
        max_tokens=1024,
        api_key=api_key,
    )
    return response.choices[0].message.content


# BLOCO 5: spec da função
def build_code_spec() -> Dict[str, Any]:
    return {
        "name": "swap_keys_values",
        "description": "Swaps the keys and values in a given dictionary.",
        "params": {
            "d": "A dictionary with unique values."
        },
    }


# BLOCO 6: construir prompt
def build_messages(code_spec: Dict[str, Any]) -> List[Dict[str, str]]:
    return [
        {
            "role": "system",
            "content": (
                "You are an expert software engineer that writes clean functional code. "
                "You always document your functions."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Please implement this Python function based on the following JSON specification:\n"
                f"{json.dumps(code_spec, indent=2)}\n\n"
                "Return only the Python function code. "
                "Do not wrap the answer in markdown fences. "
                "Include a proper docstring."
            ),
        },
    ]


# BLOCO 7: limpar markdown se vier
def clean_code_output(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```python\s*", "", text)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


# BLOCO 8: main
def main() -> None:
    code_spec = build_code_spec()
    messages = build_messages(code_spec)

    response = generate_response(messages)
    clean_code = clean_code_output(response)

    print("=== GENERATED CODE ===")
    print(clean_code)


# BLOCO 9: entry point
if __name__ == "__main__":
    main()
