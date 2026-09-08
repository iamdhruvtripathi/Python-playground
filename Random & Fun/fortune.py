import requests
import random

URL = "https://zenquotes.io/api/quotes"

response = requests.get(URL, timeout=5)
response.raise_for_status()

quotes = response.json()

quote = random.choice(quotes)

print("\nYour questionable life advice:")
print(f'"{quote["q"]}"')
print(f"— {quote["a"]}")
