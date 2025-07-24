# 1. 偶奇判定
def is_even(n: int) -> bool:
    """n が偶数なら True"""
    return n % 2 == 0

# 2. 成績判定
def grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"
    
# 3. 閏年判定
def is_leap(year: int) -> bool:
    return(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 4. サイン関数
def sign(n: int) -> str:
    if n > 0:
        return "正"
    if n < 0:
        return "負"
    return "ゼロ"

# 5. デモ実行
if __name__ == "__main__":
    x = int(input("整数を入力>> "))
    print("偶数です" if is_even(x) else "奇数です")

    score = int(input("点数を入力>. "))
    print(f"評価：{grade(score)}")

    year = int(input("西暦を入力>> "))
    print("閏年です" if is_leap(year) else "平年です")

    print(f"sign({x}) = {sign(x)}")