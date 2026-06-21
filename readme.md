# Ai Concepts Tutor Chatbot


## Setup

- Install [OLAMA](https://ollama.com/download/windows)
- <img width="633" height="479" alt="image" src="https://github.com/user-attachments/assets/ce0a480c-98b2-4c1f-8351-d1b74b4d29a6" />
- After installing, open PowerShell and check:
  ```powershell
  ollama --version
  ``` 
- Then download a small model:
  ```powershell
   ollama pull llama3.2
  ``` 
  <img width="743" height="193" alt="image" src="https://github.com/user-attachments/assets/134a1514-e9da-4fea-b63c-8542e9b898d2" />
- Test it:
  ```powershell
   ollama run llama3.2
  ``` 
  <img width="956" height="209" alt="image" src="https://github.com/user-attachments/assets/ccdb6f01-02f8-496e-bad8-1a347fe4bdd5" />

- Create a virtual environment for the project and activate it
  ```powershell
    python -m venv .venv
    .venv\Scripts\Activate.ps1
  ```
  <img width="565" height="234" alt="image" src="https://github.com/user-attachments/assets/4ec082a6-24de-4067-a28f-39d6e74f10a2" />
-  Install ADK + LiteLLM
  ```powershell
   pip install google-adk litellm
  ```
  <img width="593" height="85" alt="image" src="https://github.com/user-attachments/assets/f35e9166-61d3-4074-8c25-500ea8595f29" />
  **Agent Development Kit**: It gives you the framework for building the chatbot/agent. So instead of writing all chatbot logic yourself, ADK gives you the structure.
 **litellm**: This is the model connector/adapter. ADK needs a way to talk to different model providers. litellm helps ADK talk to models that are not Gemini, including local Ollama models.
```python
from google.adk.models.lite_llm import LiteLlm

model=LiteLlm(model="ollama_chat/llama3.2")
```
That tells ADK:
> Use LiteLLM to talk to Ollama and run the llama3.2 model locally










## References
- [Olama Docs](https://docs.ollama.com/quickstart)
