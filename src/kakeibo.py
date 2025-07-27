from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

CSV_PATH = Path("records.csv")


def append_record(kind: str, amount: float) -> None:
    date = datetime.today().strftime("%Y-%m-%d")
    with CSV_PATH.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, kind, amount])


def main() -> None:
    print("家計簿CLI (q 終了)")
    while True:
        cmd = input("[a]収入 [e]支出 [q]終了 >> ").lower()
        if cmd == "q":
            break
        if cmd not in {"a", "e"}:
            print("コマンド不明")
            continue
        amt = float(input("金額>> "))
        append_record(cmd, amt)
        print("記録しました\n")


if __name__ == "__main__":
    main()
