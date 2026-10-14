import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. Please check your .env file."
    )

client = genai.Client(api_key=GEMINI_API_KEY)


def gemini_ai_call(prompt):
    interaction = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=prompt
    )
    return interaction.output_text