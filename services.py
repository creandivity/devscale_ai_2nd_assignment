import os

from dotenv import load_dotenv
from openai import OpenAI
from app.settings import settings


def generate_response(prompt: str) -> str:
    client = OpenAI(base_url=settings.openrouter_base_url, api_key=settings.openrouter_api_key)

    completion = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {"role": "user", "content":prompt}
        ]
    )

    response = completion.choices[0].message.content
    return response or "No reponse from LLM"