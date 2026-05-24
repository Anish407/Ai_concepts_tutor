# AI Backend Mental Model — Before We Start

This README gives a beginner-friendly mental model for understanding how AI, Machine Learning, Deep Learning, Neural Networks, Transformers, LLMs, and RAG fit together.

The goal is not to master everything immediately. The goal is to build a clear map in your head so that every future topic has a place.

---

## 1. The Big Picture

AI is not one single technology. It is a broad field.

Think of it like this:

```text
AI
 └── Machine Learning
      └── Deep Learning
           └── Neural Networks
                └── Transformers
                     └── Large Language Models
```

Each level is more specific than the one above it.

---

## 2. What Is AI?

**AI — Artificial Intelligence** means building systems that can perform tasks that normally require human intelligence.

Examples:

- Answering questions
- Translating languages
- Recognizing images
- Detecting fraud
- Recommending products
- Summarizing documents
- Writing code
- Planning tasks
- Talking like a chatbot

AI is the broad goal.

Not all AI uses machine learning. Some older AI systems used manually written rules.

Example:

```text
IF customer_spending > 10000
AND country_changed = true
THEN mark transaction as suspicious
```

This is rule-based AI.

It may look intelligent, but it does not learn by itself.

---

## 3. What Is Machine Learning?

**Machine Learning** is a subset of AI where the system learns patterns from data instead of relying only on manually written rules.

Instead of writing every rule manually, you give the system examples.

Example:

```text
Input Data:
- Transaction amount
- Country
- Time of transaction
- Device used
- Customer history

Expected Output:
- Fraud
- Not fraud
```

The ML model learns patterns from many examples and later predicts whether a new transaction looks suspicious.

### Rule-Based System vs Machine Learning System

| Approach | How It Works | Example |
|---|---|---|
| Rule-based system | Developer writes explicit rules | `IF amount > 10000 THEN suspicious` |
| Machine learning system | Model learns from historical data | Learns fraud patterns from thousands of previous transactions |

The important point:

> In traditional programming, the developer writes the logic.  
> In machine learning, the model learns part of the logic from data.

---

## 4. What Is Deep Learning?

**Deep Learning** is a subset of Machine Learning that uses neural networks with many layers.

Deep learning is powerful because it can learn complex patterns from large amounts of data.

It is commonly used in:

- Image recognition
- Speech recognition
- Natural language processing
- Translation
- Recommendation systems
- Large Language Models

A simple mental model:

```text
Machine Learning:
Uses algorithms to learn patterns.

Deep Learning:
Uses layered neural networks to learn more complex patterns.
```

---

## 5. What Is a Neural Network?

A **Neural Network** is a system made of connected mathematical units called neurons.

A neural network usually has:

```text
Input Layer
   ↓
Hidden Layers
   ↓
Output Layer
```

Example:

```text
Input:
"This customer may cancel the subscription"

Neural network processes patterns:
- Words
- Meaning
- Customer history
- Previous behavior

Output:
Cancellation risk = 82%
```

The network learns by adjusting internal values called **weights**.

---

## 6. What Are Transformers?

A **Transformer** is a deep learning architecture that became very important for language tasks.

Transformers are the architecture behind modern Large Language Models.

They are good at understanding relationships between words in a sequence.

Example sentence:

```text
The bank approved my loan.
```

The word `bank` means a financial institution.

But in this sentence:

```text
The boat reached the river bank.
```

The word `bank` means the side of a river.

A transformer helps the model understand meaning from context.

---

## 7. What Are Large Language Models?

A **Large Language Model**, or **LLM**, is a deep learning model trained on large amounts of text.

Examples of LLM-style systems:

- ChatGPT
- Claude
- Gemini
- Llama
- Mistral

LLMs can:

- Answer questions
- Summarize text
- Generate code
- Explain concepts
- Translate language
- Extract structured data
- Help with reasoning-style tasks
- Generate chat responses

A simple mental model:

```text
LLM = A deep learning model trained to understand and generate language
```

But be careful:

> An LLM does not truly “know” things like a human.  
> It predicts likely text based on training, prompt, and context.

That is why LLMs can sometimes hallucinate.

---

## 8. The AI Backend Application Flow

When building AI applications, the backend usually sits between the user and the model.

A simple AI backend flow looks like this:

```text
User Question
   ↓
Backend API
   ↓
Optional Retrieval from database/docs
   ↓
Prompt construction
   ↓
LLM call
   ↓
Response parsing
   ↓
Return answer to user
```

### Example

User asks:

```text
What is our company's refund policy?
```

Backend flow:

```text
1. User sends question to backend API.
2. Backend checks user identity and permissions.
3. Backend searches company documents.
4. Backend finds relevant refund policy sections.
5. Backend builds a prompt with the question and retrieved text.
6. Backend sends the prompt to the LLM.
7. LLM generates an answer.
8. Backend returns answer with source references.
```

---

## 9. Why the Backend Matters

A beginner may think:

```text
Frontend → LLM API → Answer
```

But real systems are not that simple.

Production AI backends must handle:

- Authentication
- Authorization
- User permissions
- Document access control
- Prompt building
- Retrieval
- Caching
- Rate limiting
- Token limits
- Cost tracking
- Logging
- Monitoring
- Evaluation
- Security
- Prompt injection protection
- Data privacy

A better mental model:

```text
Frontend
   ↓
AI Backend API
   ↓
Auth / Permissions
   ↓
Retrieval / Tools / Business Logic
   ↓
Prompt Builder
   ↓
LLM Provider or Local Model
   ↓
Validation / Formatting
   ↓
Response to User
```

This is where backend engineering becomes extremely valuable in AI.

---

## 10. What Is RAG?

**RAG** means **Retrieval-Augmented Generation**.

It is one of the most important patterns in AI backend applications.

RAG means:

> First retrieve relevant information, then give that information to the LLM so it can answer using that context.

The RAG flow:

```text
Documents
   ↓
Split into chunks
   ↓
Convert chunks to embeddings
   ↓
Store in vector database
   ↓

User asks question
   ↓
Convert question to embedding
   ↓
Find similar chunks
   ↓
Send chunks + question to LLM
   ↓
LLM answers using retrieved context
```

---

## 11. Why RAG Is Needed

An LLM has limitations:

- It may not know your private company data.
- It may not know the latest data.
- It may hallucinate.
- It may not know your internal system documentation.
- Its training data may be outdated.
- It cannot automatically access your database unless you build that integration.

RAG solves part of this by giving the model external knowledge at request time.

Example:

```text
Without RAG:
User: What is our internal deployment process?
LLM: Guesses based on general software practices.

With RAG:
User: What is our internal deployment process?
Backend retrieves internal deployment docs.
LLM answers based on those docs.
```

---

## 12. RAG Ingestion Pipeline

Before users can ask questions, documents must be processed.

This is called the **ingestion pipeline**.

```text
Upload document
   ↓
Extract text
   ↓
Clean text
   ↓
Split into chunks
   ↓
Create embeddings
   ↓
Store chunks + vectors + metadata
```

### Example Metadata

```json
{
  "fileName": "deployment-guide.pdf",
  "page": 12,
  "section": "Rollback Strategy",
  "tenantId": "brand-a",
  "visibility": "engineering"
}
```

Metadata is important because it helps filter what the user is allowed to retrieve.

---

## 13. RAG Query Pipeline

When the user asks a question, the query pipeline runs.

```text
User question
   ↓
Create embedding for question
   ↓
Search vector database
   ↓
Retrieve top matching chunks
   ↓
Apply permission filters
   ↓
Build prompt
   ↓
Call LLM
   ↓
Return answer
```

Example:

```text
Question:
"How do we rollback an ECS deployment?"

Retrieved chunks:
- ECS deployment guide, rollback section
- CloudWatch alarm rollback section
- GitLab pipeline deployment notes

LLM answer:
Uses only the retrieved context to explain rollback steps.
```

---

## 14. AI Backend vs Traditional Backend

Traditional backend:

```text
Request
   ↓
Validate input
   ↓
Run business logic
   ↓
Query database
   ↓
Return deterministic response
```

AI backend:

```text
Request
   ↓
Validate input
   ↓
Retrieve context
   ↓
Build prompt
   ↓
Call model
   ↓
Validate model output
   ↓
Return probabilistic response
```

The brutal truth:

> Traditional backend systems are mostly deterministic.  
> AI backend systems are partly probabilistic.

That means AI systems need more testing, monitoring, evaluation, and guardrails.

---

## 15. Deterministic vs Probabilistic Behavior

A normal API usually gives predictable output.

Example:

```http
GET /orders/123
```

Expected response:

```json
{
  "orderId": 123,
  "status": "Shipped"
}
```

An LLM-based API may produce different wording for the same question.

Example:

```text
Question:
Explain order status.

Possible Answer 1:
The order has been shipped and is on its way.

Possible Answer 2:
Your order is currently marked as shipped.

Possible Answer 3:
The package has left the warehouse and is in transit.
```

The meaning may be similar, but the output is not always identical.

This is why AI backend systems need:

- Structured output
- JSON schemas
- Validation
- Retry logic
- Evaluation tests
- Logging
- Human review for critical workflows

---

## 16. Where Agents Fit

An **AI Agent** is an AI system that can use tools and take multiple steps.

Simple LLM:

```text
User asks question
   ↓
LLM answers
```

Agent:

```text
User asks task
   ↓
Agent plans steps
   ↓
Agent calls tools
   ↓
Agent observes results
   ↓
Agent continues or finishes
```

Example:

```text
User:
Create a support ticket for this production issue.

Agent:
1. Summarizes the issue.
2. Checks logs.
3. Searches related incidents.
4. Creates a Jira ticket.
5. Sends a Slack message.
```

Agents are powerful but risky.

They need:

- Tool permissions
- Audit logs
- Human approval
- Safe execution boundaries
- Error handling
- Monitoring

---

## 17. Where MCP Fits

**MCP**, or **Model Context Protocol**, is a standard way for AI applications to connect to tools, data, and systems.

Simple mental model:

```text
AI App
   ↓
MCP Client
   ↓
MCP Server
   ↓
Tools / Files / APIs / Databases
```

Example:

```text
AI assistant wants to query GitHub.

Instead of hardcoding GitHub integration directly into every AI app:
- GitHub functionality can be exposed through an MCP server.
- The AI app connects to that MCP server.
- The model can use the available GitHub tools safely.
```

MCP is useful because it standardizes how AI apps access external context and tools.

---

## 18. The Full Mental Model

A modern AI backend application may look like this:

```text
User
 ↓
Frontend / Chat UI
 ↓
Backend API
 ↓
Authentication + Authorization
 ↓
Conversation Store
 ↓
Retriever / Vector Database
 ↓
Business Data / SQL / Documents / APIs
 ↓
Prompt Builder
 ↓
LLM / Local Model / Cloud Model
 ↓
Output Validator
 ↓
Audit Logs + Metrics + Cost Tracking
 ↓
Response to User
```

This is the architecture mindset you need for serious AI backend development.

---

## 19. What You Should Understand Before Coding

Before building a real AI app, you should understand these questions:

1. What is the user asking?
2. Does the LLM already know enough?
3. Do we need to retrieve private or fresh data?
4. Where is the data stored?
5. How do we chunk and embed the data?
6. How do we ensure users only retrieve allowed data?
7. How do we build the prompt?
8. Which model should answer?
9. How do we validate the output?
10. How do we measure if the answer is correct?
11. How do we log cost, latency, and failures?
12. How do we prevent prompt injection and data leakage?

---

## 20. Summary

The core mental model is:

```text
AI is the broad field.
Machine Learning is AI that learns from data.
Deep Learning is ML using neural networks.
Transformers power modern LLMs.
LLMs generate and understand language.
RAG connects LLMs to external knowledge.
Agents let LLMs use tools and perform workflows.
MCP standardizes tool and context integration.
AI backend engineering makes all of this secure, reliable, observable, and production-ready.
```

For an AI backend developer, the most important shift is this:

> You are not just calling an LLM API.  
> You are designing a system around the LLM.

That system must handle data, permissions, prompts, retrieval, security, cost, latency, monitoring, and evaluation.

---


