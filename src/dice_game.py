from __future__ import annotations

import random


def roll_dice() -> int:
    return random.randint(1, 6)


def play() -> None:
    print("🎲 サイコロ当てゲーム（q で終了）")
    while True:
        guess = input("1~6 を予想して入力>> ")
        if guess.lower() in {"q", "quit"}:
            print("お疲れ！")
            break
        try:
            g = int(guess)
            if not 1 <= g <= 6:
                raise ValueError
        except ValueError:
            print("⚠ 数字は 1~6 でお願いします")
            continue

        actual = roll_dice()
        result = "🎯 HIT!" if g == actual else "✖ はずれ"
        print(f"{result} - 出目 {actual}\n")


if __name__ == "__main__":
    play()
