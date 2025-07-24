from __future__ import annotations

# 1. list 内包
squares = [x**2 for x in range(1, 21)]
evens = [x for x in range(1,21) if x % 2 == 0]
print("squares:", squares)
print("evens  :", evens)

# 2. ネストした list 内包
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("matrix :", matrix)

# 3. dict 内包
square_dict = {x: x**2 for x in range(1, 11)}
print("square_dict:", square_dict)

# 4. set 内包
unique = {ch for ch in "abracadabra" if ch not in "abc"}
print("unique set :", unique)

# 5. ラムダ + map / filter
doubles = list(map(lambda x: x * 2, range(5)))
div_by_thrre = list(filter(lambda x: x % 3 == 0, range(30)))
print("doubles  :", doubles)
print("div_by_three:", div_by_thrre)

# 6. 小演習: シーザー暗号（3シフト）
def caesar(text: str, shift: int = 3) -> str:
    cipher_chars: list[str] = []
    for c in text.lower():
        if c.isalpha():
            shifted = (ord(c) - 97 + shift) % 26 + 97
            cipher_chars.append(chr(shifted))
        else:
            cipher_chars.append(chr(shifted))
    return "".join(cipher_chars)

if __name__ == "__main__":
    print("--- Caesar cipher demo ---")
    plain = input("平文を入力>> ")
    print("暗号文:", caesar(plain))