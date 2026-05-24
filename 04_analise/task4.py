from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import bigrams


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "feedback.csv"
OUTPUT_CSV = BASE_DIR / "feedback_bigrams.csv"


def clean_text(text):
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

# Чистимо токени так само, як в Task2/Task3
filtered_tokenized: list[list[str]] = []
for toks in tokenized:
    filtered_tokenized.append([t for t in toks if t not in stop_words and len(t) >= 3])

bigram_counter: Counter[tuple[str, str]] = Counter()
for toks in filtered_tokenized:
    bigram_counter.update(list(bigrams(toks)))

top10 = bigram_counter.most_common(10)

print("Task 4 — біаграми")
print("Top 10 біаграм:")
for (w1, w2), count in top10:
    print(f"{w1} {w2:>12}  {count}")

out_df = pd.DataFrame(
    [(f"{w1} {w2}", count) for (w1, w2), count in top10],
    columns=["bigram", "frequency"],
)
out_df.to_csv(OUTPUT_CSV, index=False)

print(f"\nCSV збережений: {OUTPUT_CSV.name}")