import json
import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"


def ask_ollama(message: str) -> str:
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are a patient AI tutor. Explain concepts clearly and briefly.",
            },
            {
                "role": "user",
                "content": message,
            },
        ],
        "stream": False,
        "options": {
            "temperature": 2,
        },
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    result = response.json()

    prompt_tokens = result.get("prompt_eval_count", 0)
    completion_tokens = result.get("eval_count", 0)
    total_tokens = prompt_tokens + completion_tokens

    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Completion tokens: {completion_tokens}")
    print(f"Total tokens: {total_tokens}")
    return result["message"]["content"]

if __name__ == "__main__":
    while True:
        question = input("Ask something (or 'exit' to quit): ")
        if question.lower() == "exit":
            break
        answer = ask_ollama(question)
        print("Answer:")
        print(answer)
        print()
