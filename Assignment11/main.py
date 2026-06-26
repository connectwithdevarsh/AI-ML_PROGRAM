import os
import cohere
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(api_key=api_key)

print("========== AI TEXT SUMMARIZER ==========")
print("Enter or paste long text (Press Enter twice to finish):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
user_text = "\n".join(lines)

print("\nChoose summary option:")
print("1. Short Summary")
print("2. Medium Summary")
print("3. Detailed Summary")
choice = input("Enter choice (1/2/3): ")

bullet = input("Do you want Bullet Summary? (Yes/No): ")

prompt = "Summarize the following text. "
if choice == "1":
    prompt += "Provide a very short summary (1-2 sentences). "
elif choice == "2":
    prompt += "Provide a medium summary (1 paragraph). "
elif choice == "3":
    prompt += "Provide a detailed summary. "

if bullet.lower() == "yes" or bullet.lower() == "y":
    prompt += "Format the output as a bulleted list. "

prompt += "\n\nText: " + user_text

response = co.chat(message=prompt)
summary = response.text

print("\n========== SUMMARY ==========")
print(summary)

print("\nOriginal Word Count:", len(user_text.split()))
print("Summary Word Count:", len(summary.split()))

kw_prompt = "Extract 5 to 10 important keywords from the following text. Return only the keywords as a comma-separated list:\n\n" + user_text
kw_response = co.chat(message=kw_prompt)
keywords = kw_response.text

print("\nImportant Keywords:")
print(keywords)
