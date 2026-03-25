from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "LLM API running"}

# @app.post("/generate")
# def generate(request: PromptRequest):
#     response = requests.post(
#         OLLAMA_URL,
#         json={
#             "model": "llama3",
#             "prompt": request.prompt,
#             "stream": False
#         }
#     )

#     data = response.json()

#     return {
#         "prompt": request.prompt,
#         "response": data.get("response", "")
#     }

@app.post("/generate")
def generate(request: PromptRequest):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": request.prompt,
                "stream": False,
                "options": {
                    "num_predict": 100
                }
            }
        )

        data = response.json()

        return {
            "response": data.get("response", "")
        }

    except Exception as e:
        return {"error": str(e)}