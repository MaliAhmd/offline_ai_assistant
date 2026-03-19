import requests
from bs4 import BeautifulSoup
import os

BASE_URL = "https://nidripcentralelectronics.co.uk"

pages = [
    "/",
    "/about-us",
    "/contact-us",
]

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_dir = os.path.join(BASE_DIR, "data", "raw")
os.makedirs(output_dir, exist_ok=True)

def scrape_page(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    text = soup.get_text(separator=" ")

    return text


for page in pages:

    url = BASE_URL + page

    text = scrape_page(url)

    filename = page.replace("/", "_")

    with open(os.path.join(output_dir, f"{filename}.txt"), "w", encoding="utf8") as f:
        f.write(text)

print("Scraping complete")