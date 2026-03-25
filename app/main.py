from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
import requests
import json

app = FastAPI()

# OLLAMA_URL = "http://localhost:11434/api/generate"

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "LLM API running"}

@app.post("/generate")
def generate(request: PromptRequest):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": request.prompt,
            "stream": False
        }
    )

    data = response.json()

    return {
        "prompt": request.prompt,
        "response": data.get("response", "")
    }

@app.post("/generate-stream")
def generate_stream(request: PromptRequest):
    def stream():
        with requests.post(
            OLLAMA_URL,
            json={
                "model": "mistral",
                "prompt": request.prompt,
                "stream": True
            },
            stream=True
        ) as response:
            for line in response.iter_lines():
                if line:
                    try:
                        data = json.loads(line.decode("utf-8"))
                        if "response" in data:
                            yield data["response"]
                    except:
                        continue

    return StreamingResponse(stream(), media_type="text/plain")