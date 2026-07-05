import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

uploaded_files = []

for filename in os.listdir("docs"):
    if filename.endswith(".md"):
        print(f"Uploading {filename}")

        file = client.files.upload(
    file=os.path.join("docs", filename),
    mime_type="text/markdown"
)

        uploaded_files.append(file)

print(f"\nUploaded {len(uploaded_files)} files")