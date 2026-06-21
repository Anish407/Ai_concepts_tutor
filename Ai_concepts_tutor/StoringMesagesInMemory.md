# Local Chat Script

Storing previous messages in memory lets the model consider earlier parts of the conversation before answering. The model itself does not remember your previous questions automatically.

Every time you call Ollama, it is a fresh request. If you want the model to “remember,” your app must resend the relevant previous messages.