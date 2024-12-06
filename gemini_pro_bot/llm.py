import os
import google.generativeai as genai
from google.generativeai.types.safety_types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv

load_dotenv()

# Disable all safety filters
SAFETY_SETTINGS = {
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
}


genai.configure(api_key=os.getenv("AIzaSyC6AEgAgVu06yt4HMIF8RPeMQZJqv5GG4A"))

# Define model dictionary
models = {
    "gemini-1.5-pro": genai.GenerativeModel("gemini-1.5-pro", safety_settings=SAFETY_SETTINGS),
    "gemini-1.5-flash": genai.GenerativeModel("gemini-1.5-flash", safety_settings=SAFETY_SETTINGS),
    "gemini-exp-1114": genai.GenerativeModel("gemini-exp-1114", safety_settings=SAFETY_SETTINGS),
}

# Default model (can be changed later)
default_model = models["gemini-1.5-flash"]