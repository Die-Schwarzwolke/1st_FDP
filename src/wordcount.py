from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


def normalize(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r"[^a-z']", " ", text)
    return text.split()


def top_n(words: list[str], n: int = 10) -> list[tuple[str, int]]:
    return Counter(words).most_common(n)


def save_csv(records: list[tuple[str, int]], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        writer.writerows(records)


if __name__ == "__main__":
    src_path = Path("sample.txt")
    if src_path.exists():
        text_data = src_path.read_text(encoding="utf-8")
    else:
        print("テキストを張り付けて Enter→Ctrl-D (Win:Ctrl-Z) :")
        text_data = ""
        try:
            while line := input():
                text_data += line + "\n"
        except EOFError:
            pass

    words = normalize(text_data)
    ranking = top_n(words, 10)

    print("--- Top 10 words ---")
    for i, (w, c) in enumerate(ranking, 1):
        print(f"{i:2d}. {w:<15} {c}")

    save_csv(ranking, Path("top10.csv"))
    print("\nCSV saved to top10.csv")
