# Temperature

[Code](./src/temperature.py)

Temperature controls how predictable or varied an LLM's answer is.

It does not make the model smarter.

It changes how adventurous the model is when choosing the next token.

> Lower temperature means less randomness
> Lower temperature = more predictable
> Higher temperature = more adventurous

## Simple Mental Model

An LLM generates text one token at a time.

At each step, the model has multiple possible next tokens.

Temperature affects how strongly the model prefers the most likely token.

```text
Low temperature  -> safer, more predictable, more repetitive
High temperature -> more varied, more creative, less predictable
```

## Where Temperature Is Set

In Ollama's `/api/chat` call, temperature is set inside `options`:

```python
payload = {
    "model": MODEL,
    "messages": messages,
    "stream": False,
    "options": {
        "temperature": 0.2,
    },
}
```

In our current `src/temperature.py`, we are using:

```python
"temperature": 0.2
```

That is a good value for tutor-style answers because it keeps the response focused.

## How To Experiment

Use the same prompt multiple times with different temperature values.

Try these values:

```text
0.0
0.2
0.7
1.0
1.3
```

For each value:

1. Change the temperature in `src/temperature.py`.
2. Run the script.
3. Ask the same question.
4. Compare the answers.

Run:

```powershell
python src\temperature.py
```

Example question:

```text
Explain RAG using a simple real-world analogy.
```

Ask it three times with the same temperature.

Then change the temperature and ask the same question again.

## What To Observe

At low temperature:

```text
0.0 to 0.2
```

You should usually see:

- More direct answers.
- Less variation between runs.
- Fewer creative examples.
- Better behavior for classification and structured output.

At medium temperature:

```text
0.5 to 0.7
```

You should usually see:

- More natural explanations.
- Some variation.
- Better examples.
- Good general chatbot behavior.

At high temperature:

```text
1.0 and above
```

You may see:

- More creative wording.
- More surprising examples.
- Less consistency.
- More chance of drifting away from the question.
- More chance of hallucination.

## Recommended Values

For this project:

```text
Concept explanations: 0.2 to 0.5
Friendly tutoring:    0.3 to 0.7
Classification:       0.0 to 0.2
JSON output:          0.0 to 0.2
Creative writing:     0.8 to 1.2
```

For RAG, prefer a lower temperature:

```text
0.1 to 0.3
```

Reason:

RAG answers should stay close to the retrieved source text instead of becoming too creative.

## Good Experiment Prompts

Use these prompts to compare behavior.

### Factual Explanation

```text
Explain what local inference means in AI applications.
```

Expected result:

Low temperature should be clearer and more stable.

### Analogy

```text
Explain RAG using a library analogy.
```

Expected result:

Higher temperature may produce more varied analogies.

### Classification

```text
Classify this user request into one category: rag, coding, setup, or general.
Request: How do I store embeddings in SQLite?
Return only the category.
```

Expected result:

Low temperature should be more reliable.

### Structured Output

```text
Return JSON with two fields: topic and difficulty.
Question: What is MCP?
```

Expected result:

Low temperature should better follow the requested format.

## Token Usage

Temperature does not directly mean "more tokens".

But high temperature can sometimes produce longer or more rambling answers.

That can increase output tokens.

Your script logs:

```text
Prompt tokens
Completion tokens
Total tokens
```

Watch whether high temperature changes completion tokens.

## Key Lesson

Temperature is a behavior control.

Use low temperature when you need reliability.

Use higher temperature when you want creativity.

For learning AI backend systems, the important habit is:

> Change one setting at a time, ask the same prompt, and compare the result.
