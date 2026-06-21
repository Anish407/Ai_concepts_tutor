# Storing Messages In Memory

When we build a chatbot, we usually want it to understand follow-up questions.

For example:

```text
User: What is RAG?
Assistant: RAG means Retrieval-Augmented Generation.

User: Why is it useful?
```

The second question says `it`.

A human understands that `it` means RAG because we remember the previous sentence.

But an LLM does not automatically remember previous requests. Every API call is a new request unless we send the previous messages again.

## The Core Idea

Message memory means keeping the conversation history in our application.

In Python, this is usually just a list:

```python
messages = [
    {
        "role": "system",
        "content": "You are a patient AI tutor.",
    },
    {
        "role": "user",
        "content": "What is RAG?",
    },
    {
        "role": "assistant",
        "content": "RAG means Retrieval-Augmented Generation.",
    },
    {
        "role": "user",
        "content": "Why is it useful?",
    },
]
```

Then we send this full list to Ollama.

This gives the model enough context to understand that `it` refers to RAG.

## Without Message Memory

If we send only the latest question:

```python
messages = [
    {
        "role": "user",
        "content": "Why is it useful?",
    },
]
```

The model may not know what `it` means.

It may guess, ask for clarification, or answer incorrectly.

The flow looks like this:

```text
Question 1 -> Ollama -> Answer 1
Question 2 -> Ollama -> Answer 2
Question 3 -> Ollama -> Answer 3
```

Each request is separate.

The model does not see the previous conversation.

## With Message Memory

With memory, we keep adding messages to the conversation:

```text
System instruction
User question 1
Assistant answer 1
User question 2
Assistant answer 2
User question 3
```

Then every new request includes the useful previous context.

The flow looks like this:

```text
Conversation history + new question -> Ollama -> better answer
```

This is what makes the app feel like a real chatbot instead of a question-answer script.

## Benefits

Message memory helps the model:

- Understand follow-up questions.
- Resolve words like `it`, `that`, `this`, and `they`.
- Avoid repeating explanations unnecessarily.
- Keep the same teaching style during a session.
- Refer back to earlier parts of the conversation.
- Build step-by-step explanations across multiple turns.

Example:

```text
User: Explain local inference.
Assistant: Local inference means running the model on your own machine.

User: How is that different from using an API key?
```

With memory, the model knows `that` means local inference.

Without memory, the model may not know what comparison the user wants.

## Important Tradeoff: More Memory Uses More Tokens

Your concern is correct:

> If we keep sending previous messages, the prompt gets larger.

A larger prompt means:

- More tokens are used.
- Responses may become slower.
- Local models may use more memory.
- Cloud models may cost more money.
- The model may eventually hit its context window limit.

So message memory is useful, but it must be managed carefully.

## Context Window

An LLM can only read a limited amount of text at once.

That limit is called the context window.

If the conversation becomes too long, we cannot keep sending everything forever.

At some point, we need a strategy.

## Common Memory Strategies

### 1. Keep Everything

This is the simplest approach.

```text
Send the full conversation every time.
```

Good for learning and small demos.

Bad for long conversations.

### 2. Sliding Window

Keep only the most recent messages.

```text
Keep the last 10 messages.
Drop older messages.
```

This is simple and often works well.

But the model may forget older important details.

### 3. Summarize Old Messages

Summarize older conversation into a shorter note.

Example:

```text
Summary:
The user is learning local inference with Ollama.
They understand payloads, endpoints, serialization, and chat loops.
They are now learning message memory.
```

Then keep:

```text
System instruction
Conversation summary
Recent messages
New user question
```

This saves tokens while preserving important context.

### 4. Store History In A Database

Later, we can store messages in SQLite.

That lets us:

- Save conversations after the app closes.
- Load previous sessions.
- Search old conversations.
- Build long-term memory.

But even if messages are stored in a database, we still should not send all of them to the model every time.

We only send the relevant parts.

## Temporary Memory vs Permanent Memory

Our first version will use temporary memory:

```text
Messages live in a Python list.
When the app stops, memory disappears.
```

Later, we can add permanent memory:

```text
Messages are saved in SQLite.
When the app restarts, old conversations can be loaded again.
```

## Key Lesson

Message memory does not mean the model remembers by itself.

It means:

> Our application remembers the conversation and sends the relevant messages back to the model.

That is the foundation of chatbot memory.
