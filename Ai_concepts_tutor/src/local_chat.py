import json
import urllib.request


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
    }

    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")

    result = json.loads(response_body)
    return result["message"]["content"]


if __name__ == "__main__":

    # question = "Explain what local inference means in AI applications."
    question = input("Ask something: ")
    answer = ask_ollama(question)

    print("Question:")
    print(question)
    print()
    print("Answer:")
    print(answer)
