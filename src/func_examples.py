from __future__ import annotations

import math


def area_circle(r: float) -> float:
    if r < 0:
        raise ValueError("radius must be non-negative")
    return math.pi * r**2


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    return 1 if n in (0, 1) else n * factorial(n - 1)


def greet(name: str, loud: bool = False) -> str:
    msg = f"Hello, {name}."
    return msg.upper() if loud else msg


if __name__ == "__main__":
    print(area_circle(3))
    print(factorial(6))
    print(greet("クロユキ"))
    print(greet("クロユキ", loud=True))
