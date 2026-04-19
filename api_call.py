from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def generate_note(images, fix_type):
  response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[images, f"Give me {fix_type} of the images. Make sure to include all necessary markdown formatting. The {fix_type} should be concise and informative, providing key insights and observations about the images. Use bullet points or numbered lists to organize the information effectively. Ensure that the {fix_type} captures the essential details and highlights the most important aspects of the images in a clear and structured manner. If provided image not related to coding, return an error."]
  )
  return response.text

