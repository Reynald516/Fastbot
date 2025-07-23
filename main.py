from fastapi import FastAPI, Request
import json

app = FastAPI()

# Load data dari JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Fungsi chatbot sederhana
def get_response(message: str):
    for item in data:
        if item["question"].lower() in message.lower():
            return item["answer"]
    return "Maaf, saya tidak mengerti."

@app.post("/")
async def chatbot(request: Request):
    req_json = await request.json()
    user_message = req_json.get("message")
    bot_response = get_response(user_message)
    return {"reply": bot_response}
