from __future__ import annotations

import re
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "feedback.csv"


def clean_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


df = pd.read_csv(DATA_PATH)
if "review" not in df.columns:
    raise ValueError("CSV повинен містити колонку 'review'.")

df["clean_review"] = df["review"].astype(str).map(clean_text)

row_count = len(df)
word_counts = df["clean_review"].map(lambda s: len(s.split()))
avg_words = float(word_counts.mean()) if row_count else 0.0

print("Task 1 — завантаження та очищення")
print(f"Кількість відгуків (рядків): {row_count}")
print(f"Середня довжина відгуку (слів): {avg_words:.2f}")
print("\nПриклад (перші 3 очищених):")
for i, s in enumerate(df["clean_review"].head(3), start=1):
    print(f"{i}. {s}")
