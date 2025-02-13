import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Now we can get the API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

audio_path = "test.mp3"
with open(audio_path, "rb") as audio_file:
    # For openai==0.28.0 (old usage):
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

print("Transcription:", transcript["text"])
