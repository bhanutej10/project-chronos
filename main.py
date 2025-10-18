import os
import re
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

if not GEMINI_API_KEY:
    raise ValueError("Gemini API key not found. Please add GEMINI_API_KEY to your .env file.")

client = genai.Client(api_key=GEMINI_API_KEY)

# Extract possible key terms (slang, abbreviations, etc.)
def extract_keywords(text):
    words = re.findall(r"\b[a-zA-Z]{2,}\b", text.lower())
    slang_like = [w for w in words if len(w) <= 5 or w.isupper()]
    common_terms = ["smh", "lol", "ttyl", "g2g", "idk", "brb", "ppl", "tbh"]
    keywords = list(set(slang_like + [w for w in words if w in common_terms]))
    return keywords

# Search Wikipedia or dictionary links for context
def fetch_context_links(keywords):
    links = []
    for kw in keywords:
        try:
            search_url = f"https://en.wikipedia.org/wiki/{kw}"
            r = requests.get(search_url)
            if r.status_code == 200:
                links.append(search_url)
                continue

            dict_url = f"https://www.dictionary.com/browse/{kw}"
            r = requests.get(dict_url)
            if r.status_code == 200:
                links.append(dict_url)
                continue

            slang_url = f"https://www.dictionary.com/e/slang/{kw}/"
            r = requests.get(slang_url)
            if r.status_code == 200:
                links.append(slang_url)
        except Exception:
            pass

    # Remove duplicates and limit to top 3
    return list(dict.fromkeys(links))[:3]

# Reconstruct text using Gemini
def reconstruct_text(fragment):
    prompt = f"""Reconstruct this internet fragment into a clear, complete message with cultural context.
Input: "{fragment}"
Output:"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text.strip()

# Main program
if __name__ == "__main__":
    fragment = input("Enter the incomplete or obscure text: ").strip()
    reconstructed = reconstruct_text(fragment)
    keywords = extract_keywords(fragment + " " + reconstructed)
    context_links = fetch_context_links(keywords)

    print("\n--- RECONSTRUCTION REPORT ---")
    print("[Original Fragment]")
    print(f'> "{fragment}"')
    print("[AI-Reconstructed Text]")
    print(f'> "{reconstructed}"')
    print("[Contextual Sources]")
    if context_links:
        for link in context_links:
            print(f"* {link}")
    else:
        print("* No contextual links found.")

