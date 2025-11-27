from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("API key NOT found! Did you create the .env file?")
    exit()  


def read_payload_file():
    payload_file = "payload.md"

    if not os.path.exists(payload_file):
        print("payload.md not found!")
        return ""

    with open(payload_file, "r", encoding="utf-8") as f:
        return f.read()



def send_to_groq(payload):
    if not payload:
        print("No payload to send!")
        return None

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # updated supported model
        messages=[
            {"role": "system", "content": "Generate a professional README.md using the provided project data."},
            {"role": "user", "content": payload}
        ]
    )

    result = response.choices[0].message.content

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(result)

    print("✅ AI README.md generated → README.md")
    return result
