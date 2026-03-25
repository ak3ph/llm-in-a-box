# llm-in-a-box

> Running Large Language Models locally with an API layer — no external APIs required

---

## Idea / Problem

Most developers use hosted LLM APIs (like OpenAI), which are:

* fast
* easy to use

But they come with trade-offs:

* cost
* dependency on external services
* lack of control

This project explores a different approach:

→ Running LLMs locally and exposing them via an API

---

## What It Does

* Runs a local LLM using Ollama
* Exposes the model via FastAPI
* Accepts prompts via API requests
* Returns generated responses
* Supports streaming responses (experimental)
* Dockerized for portability

---

## Tech Stack

* Ollama (Local LLM runtime)
* FastAPI (API layer)
* Python
* Docker

---

## Architecture

```
User
 ↓
FastAPI (HTTP API)
 ↓
Ollama (Local LLM)
 ↓
Model (mistral / llama3)
 ↓
Response
```

---

## Key Features

* Fully local LLM execution (no external APIs)
* Clean API interface for integration
* Model flexibility (switch between models)
* Dockerized setup (run anywhere)
* Lightweight and beginner-friendly architecture

---

## How to Run

### 1. Install Ollama

Download from:
[https://ollama.com](https://ollama.com)

Run a model:

```bash
ollama run mistral
```

---

### 2. Clone Repository

```bash
git clone https://github.com/ak3ph/llm-in-a-box.git
cd llm-in-a-box
```

---

### 3. Run Locally

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

---

### 4. Access API

```
http://127.0.0.1:8000/docs
```

---

## Docker Usage

### Build Image

```bash
docker build -t llm-in-a-box .
```

### Run Container

```bash
docker run -p 8000:8000 llm-in-a-box
```

> Note: Ollama must be running on host machine

---

## API Example

### POST /generate

```json
{
  "prompt": "Explain DevOps"
}
```

---

## Performance Notes

* Runs on CPU (no GPU required)
* Response time depends on model size
* Smaller models (mistral) are faster than larger ones (llama3)

---

## Learnings

* How local LLMs work
* Differences between local vs API-based models
* Building APIs for AI systems
* Handling model performance trade-offs
* Containerizing AI applications

---

## Future Improvements

* GPU support
* Model caching optimization
* Frontend UI
* Advanced streaming support
* Deployment to cloud

---

## Author

<!-- Yash Thakur -->

[Yash Thakur](https://ak3ph.dev)

<!-- 🔗 [https://ak3ph.dev](https://ak3ph.dev) -->
<!-- 🔗 [https://github.com/ak3ph](https://github.com/ak3ph) -->
