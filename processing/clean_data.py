import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_dir = os.path.join(BASE_DIR, "data", "raw")
output_dir = os.path.join(BASE_DIR, "data", "cleaned")

os.makedirs(output_dir, exist_ok=True)

# words we want to remove (website UI noise)
noise_patterns = [
    r"skip to content",
    r"login",
    r"log in",
    r"signup",
    r"register",
    r"cart",
    r"compare products",
    r"newsletter",
    r"subscribe",
    r"all rights reserved",
    r"menu",
    r"search",
    r"×",
]

for file in os.listdir(input_dir):

    with open(os.path.join(input_dir, file), "r", encoding="utf8") as f:
        text = f.read().lower()

    # remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # remove urls
    text = re.sub(r"http\S+", "", text)

    # remove noise words
    for pattern in noise_patterns:
        text = re.sub(pattern, "", text)

    # remove special characters
    text = re.sub(r"[^\w\s.,]", " ", text)

    # remove repeated spaces again
    text = re.sub(r"\s+", " ", text)

    with open(os.path.join(output_dir, file), "w", encoding="utf8") as f:
        f.write(text.strip())

print("Cleaning complete")