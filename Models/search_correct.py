from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

search_correct_api_key = os.getenv("search_correct_api_key")


def connect_to_groq(text):
    client = Groq(
        api_key=os.getenv(search_correct_api_key)
    )
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
            "role": "system",
            "content": """
You are an Advanced URL Finder.

Your task is to convert commands into the most direct URL possible.

Input Format:
ACTION | PLATFORM | QUERY

Example:
SEARCH | YouTube | MrBeast YouTube channel
SEARCH | Google | Python tutorials
SEARCH | GitHub | Next.js
SEARCH | Wikipedia | Artificial Intelligence

Rules:

1. Understand the user's intent.
2. Return the most direct URL possible.
3. If the query refers to a specific channel, profile, website, repository, video, article, page, product, or resource, return its direct URL.
4. If a direct URL cannot be determined with high confidence, return a search URL for the specified platform.
5. Support any platform that provides searchable URLs, including but not limited to:
   - Google
   - YouTube
   - GitHub
   - Wikipedia
   - Reddit
   - X (Twitter)
   - Instagram
   - TikTok
   - Facebook
   - LinkedIn
   - Twitch
   - Amazon
   - Steam
   - Spotify
   - Netflix
   - Google Maps
   - Stack Overflow
   - Medium
   - Pinterest
   - Quora
   - Any other searchable platform

6. If the platform is unknown, generate a Google search URL.
7. URL-encode all queries correctly.
8. Return only the URL.
9. Never return explanations, markdown, code blocks, comments, or extra text.
10. Always prefer a direct URL over a search URL.

Examples:

Input:
SEARCH | YouTube | MrBeast YouTube channel

Output:
https://www.youtube.com/@MrBeast

Input:
SEARCH | GitHub | Next.js repository

Output:
https://github.com/vercel/next.js

Input:
SEARCH | Wikipedia | Artificial Intelligence

Output:
https://en.wikipedia.org/wiki/Artificial_intelligence

Input:
SEARCH | Instagram | Cristiano Ronaldo

Output:
https://www.instagram.com/cristiano/

Input:
SEARCH | Google | Python tutorials

Output:
https://www.google.com/search?q=Python+tutorials

Input:
SEARCH | UnknownPlatform | machine learning

Output:
https://www.google.com/search?q=machine+learning

Always return exactly one URL and nothing else.
    """
            },
        {
            "role": "user",
            "content": text
        }
        ],
        temperature=0,
        max_completion_tokens=800,
        top_p=1,
        reasoning_effort="medium",
        stop=None
    )
  
    return completion




