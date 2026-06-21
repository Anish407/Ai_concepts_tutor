
# Local Inference

[code](./src/local_chat.py)

Local inference means running the AI model on your own machine instead of calling an external cloud API.

- Running model locally = the model is loaded/executed on your machine
- Inference = asking the model to produce an output from an input
- Local inference = doing that inference on your own machine

In this project, Ollama runs a local HTTP server:

```text
Python code
  -> http://localhost:11434
  -> Ollama
  -> llama3.2 model on your machine
  -> response back to Python
```

This matters because:

- You do not need an external API key.
- Your prompts stay on your machine.
- You can experiment freely without per-request cloud cost.
- You learn the model/backend flow directly.

The tradeoffs:

- Local models are usually weaker than top cloud models.
- They may be slower depending on your hardware.
- They can still hallucinate.
- You are responsible for running and managing the model.

## First Script

Run:

```powershell
python src\local_chat.py
```

The script sends this shape of request to Ollama:

```json
{
  "model": "llama3.2",
  "messages": [
    {
      "role": "system",
      "content": "You are a patient AI tutor. Explain concepts clearly and briefly."
    },
    {
      "role": "user",
      "content": "Explain what local inference means in AI applications."
    }
  ],
  "stream": false
}
```

Important lesson:

> LLMs can sound confident even when the answer is incomplete or slightly wrong.

That is why AI backends need prompts, validation, retrieval, evals, logging, and human judgment.

For this project, the correct definition is:

> Local inference means your application sends prompts to a model running locally on your machine, instead of sending prompts to a remote model provider.
