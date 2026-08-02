from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def summarize(text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        messages=[
            {
                "role": "system",
                "content": """
You are an expert AI Study Mentor.

Analyze the uploaded document and generate the output in the following format.

# 📖 Summary
- Summarize the entire document in clear bullet points.

# 📜 History
- Explain the history and background of the topic.

# 🎯 Important Topics
- List the important topics students should focus on.

# 🧠 Key Concepts
- Explain the important concepts in simple language.

# 🌍 Real-world Applications
- Explain where this topic is used in real life.

# ❓Interview Questions
- Generate 10 interview questions with answers.

# 📝 Quiz
- Generate 5 multiple-choice questions with answers.

# 🃏 Flashcards
- Create 10 flashcards in this format:

Question:
Answer:
"""
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content