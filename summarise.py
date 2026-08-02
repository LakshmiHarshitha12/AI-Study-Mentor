from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize(text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an AI Study Mentor. Summarize the document in bullet points."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content