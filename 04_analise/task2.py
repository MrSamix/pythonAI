from __future__ import annotations

import re
from pathlib import Path

import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "feedback.csv"


def clean_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def ensure_nltk() -> None:
    # Завантажуємо ресурси лише якщо їх немає.
    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt", quiet=True)

    try:
        nltk.data.find("corpora/stopwords")
    except LookupError:
        nltk.download("stopwords", quiet=True)


def tokenize_reviews(reviews: list[str]) -> list[list[str]]:
    tokenized: list[list[str]] = []
    for text in reviews:
        tokenized.append(word_tokenize(text))
    return tokenized


ensure_nltk()

df = pd.read_csv(DATA_PATH)
if "review" not in df.columns:
    raise ValueError("CSV повинен містити колонку 'review'.")

cleaned = df["review"].astype(str).map(clean_text).tolist()

try:
    tokenized = tokenize_reviews(cleaned)
except LookupError:
    # В деяких версіях NLTK може знадобитися punkt_tab
    nltk.download("punkt_tab", quiet=True)
    tokenized = tokenize_reviews(cleaned)

stop_words = set(stopwords.words("english"))

total_tokens_before = sum(len(toks) for toks in tokenized)

filtered_tokenized: list[list[str]] = []
for toks in tokenized:
    filtered = [t for t in toks if t not in stop_words and len(t) >= 3]
    filtered_tokenized.append(filtered)

total_tokens_after = sum(len(toks) for toks in filtered_tokenized)

print("Task 2 — токенізація та видалення стоп-слів")
print(f"Токенів ДО очищення: {total_tokens_before}")
print(f"Токенів ПІСЛЯ (без стоп-слів та <3): {total_tokens_after}")

print("\nПриклад токенів (перші 2 відгуки):")
for i in range(min(2, len(filtered_tokenized))):
    print(f"{i+1}. {filtered_tokenized[i]}")