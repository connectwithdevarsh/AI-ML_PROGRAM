import os
from dotenv import load_dotenv
from groq import Groq
from google import genai
from openai import OpenAI

load_dotenv()

prompt = input("Enter your prompt: ")

groq_key = os.getenv("GROQ_API_KEY")
if groq_key:
    try:
        client = Groq(api_key=groq_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        groq_result = response.choices[0].message.content
    except Exception as e:
        groq_result = "Error: " + str(e)
else:
    groq_result = "API key is missing. Skipping Groq."

gemini_key = os.getenv("GEMINI_API_KEY")
if gemini_key:
    try:
        client = genai.Client(api_key=gemini_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        gemini_result = response.text
    except Exception as e:
        gemini_result = "Error: " + str(e)
else:
    gemini_result = "API key is missing. Skipping Gemini."

openai_key = os.getenv("OPENAI_API_KEY")
if openai_key:
    try:
        client = OpenAI(api_key=openai_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        openai_result = response.choices[0].message.content
    except Exception as e:
        openai_result = "Error: " + str(e)
else:
    openai_result = "API key is missing. Skipping OpenAI."

print("--------------------------------")
print("Provider")
print("Groq")
print("Model")
print("llama-3.3-70b-versatile")
print("Response")
print(groq_result)
print("--------------------------------")
print("Provider")
print("Google Gemini")
print("Model")
print("gemini-2.5-flash")
print("Response")
print(gemini_result)
print("--------------------------------")
print("Provider")
print("OpenAI")
print("Model")
print("gpt-4o-mini")
print("Response")
print(openai_result)
print("--------------------------------")
