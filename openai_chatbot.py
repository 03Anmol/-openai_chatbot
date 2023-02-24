import openai
import os
import json
import requests

openai.api_key = "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"
import json

with open("openai_chatbot.json", "r") as f:
    context = json.load(f)

question = "who is the father of science?"
response = openai.Completion.create(
    engine="davinci",
    prompt=f"Q: {question}\nContext: {context}\nA:",
    temperature=0.5,
    max_tokens=100,
    n=1,
    stop=None,
)
answer = response.choices[0].text.strip()
print(answer)

