import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"


def ask_ollama(messages: list[dict]) -> str:
    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False,
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
    messages = [
        {
            "role": "system",
            "content": "You are a patient AI tutor. Explain concepts clearly and briefly.",
        }
    ]

    while True:
        question = input("You: ")

        if question.lower() == "exit":
            break

        messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        answer = ask_ollama(messages)

        messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        print()
        print("Assistant:")
        print(answer)
        print()