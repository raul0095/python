import urllib.request
import json

# Prompt for the URL
url = input("Enter URL: ")

# Open the URL and read the data
print(f"Retrieving {url}")
response = urllib.request.urlopen(url)
data = response.read().decode()
print(f"Retrieved {len(data)} characters")

# Load the JSON data
info = json.loads(data)

# Extract comment counts and compute the sum
counts = [item['count'] for item in info['comments']]
print("Count:", len(counts))
print("Sum:", sum(counts))