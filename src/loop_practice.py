from __future__ import annotations

import time


# 1. 九九表
def multiplocation_table() -> None:
    for i in range(1, 10):
        row = [f"{i * j :2d}" for j in range(1, 10)]
        print(" ".join(row))
    print()


# 2. enumerate
def enumerate_string(s: str) -> None:
    for idx, ch in enumerate(s, start=1):
        print(f"{idx}: {ch}")
    print()


# 3. whileでカウントダウン
def countdown(n: int) -> None:
    while n >= 1:
        print(n)
        time.sleep(1)
        n -= 1
    print()


# 4. break/continue総和
def sum_skip_multiples(limit: int) -> int:
    total = 0
    for i in range(1, limit + 1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        total += i
    return total


# 5. FizzBuzzテスト関数
def fizzbuzz(n: int) -> list[str]:
    res: list[str] = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res


# 6. デモ実行
if __name__ == "__main__":
    print("=== 九九表 ===")
    multiplocation_table()

    print("=== enumerate 例 ===")
    enumerate_string("Python")

    print("=== カウントダウン ===")
    countdown(10)
    print("発射！")

    print("=== 3と5の倍数を除外した総和（1～100）===")
    print(sum_skip_multiples(100))

    print("=== FizzBuzz(15) ===")
    print(fizzbuzz(15))
