# list
fruits: list[str] = ["apple", "banana", "cherry"]
fruits.append("orange")
print("list:", fruits)

# tuple
point: tuple[int, int] = (3, 4)
x, y = point
print("tuple:", point, "x+y =", x + y)

# dict
student: dict[str, int | str] = {"name": "クロユキ", "age": 18}
student["grade"] = "A"
student["age"] += 1
print("dict:", student)

# set
odd = {1, 3, 5, 7}
even = {2, 4, 6, 8}
print("set union :", odd | even)
print("set inter :", odd & {1, 2, 3})

# comprehension preview
squares = [i ** 2 for i in range(1, 11)]
unique_chars = {ch for ch in "mississippi"}
print("squares:", squares)
print("unique :", unique_chars)

# mini exercise
def add_student(db: dict[str, int], name: str, score: int) -> None:
    if score >= 80:
        db[name] = score

if __name__ == "__main__":
    db: dict[str, int] = {}
    for _ in range(3):
        n = input("名前>> ")
        s = int(input("点数>> "))
        add_student(db, n, s)
    
    if db:
        avg = sum(db.values()) / len(db)
        print("登録生徒:", db)
        print(f"平均点: {avg:.1f}")
    else:
        print("80 点以上はいませんでした。")