from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "feedback.csv"
OUTPUT_PNG = BASE_DIR / "feedback_word_freq.png"


def clean_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def ensure_nltk():
    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt", quiet=True)

    try:
        nltk.data.find("corpora/stopwords")
    except LookupError:
        nltk.download("stopwords", quiet=True)


ensure_nltk()

df = pd.read_csv(DATA_PATH)
if "review" not in df.columns:
    raise ValueError("CSV повинен містити колонку 'review'.")

cleaned = df["review"].astype(str).map(clean_text).tolist()

try:
    tokenized = [word_tokenize(t) for t in cleaned]
except LookupError:
    nltk.download("punkt_tab", quiet=True)
    tokenized = [word_tokenize(t) for t in cleaned]

stop_words = set(stopwords.words("english"))

tokens: list[str] = []
for toks in tokenized:
    tokens.extend([t for t in toks if t not in stop_words and len(t) >= 3])

freq = Counter(tokens)
top15 = freq.most_common(15)

print("Task 3 — частотний словник")
print("Top 15 слів:")
for word, count in top15:
    print(f"{word:>15}  {count}")

if not top15:
    print("Немає даних для побудови графіка.")
else:
    words = [w for w, _ in top15][::-1]
    counts = [c for _, c in top15][::-1]

    plt.figure(figsize=(10, 6))
    plt.barh(words, counts)
    plt.xlabel("Frequency")
    plt.ylabel("Word")
    plt.title("Top 15 Frequent Words")
    plt.tight_layout()
    plt.savefig(OUTPUT_PNG, dpi=150)

    print(f"\nГрафик збережений: {OUTPUT_PNG.name}")