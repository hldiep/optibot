import os
import re
import requests
from markdownify import markdownify
import requests

url = "https://support.optisigns.com/api/v2/help_center/en-us/articles.json"

articles = []

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')
os.makedirs("docs", exist_ok=True)
while url:
    print(f"Fetching: {url}")

    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.status_code)
        break

    data = response.json()

    articles.extend(data["articles"])

    url = data["next_page"]

print(f"\nTotal articles: {len(articles)}")
for article in articles:

    title = article["title"]

    html = article["body"]

    url = article["html_url"]

    md = markdownify(html)

    filename = slugify(title) + ".md"

    filepath = os.path.join("docs", filename)

    with open(filepath, "w", encoding="utf-8") as f:

        f.write(f"# {title}\n\n")

        f.write(f"Article URL: {url}\n\n")

        f.write(md)

print("Done!")