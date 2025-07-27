# 1. 変数の宣言
age = 18  # int
height = 1.75  # float (m)
name = "クロユキ"  # str
is_student = True  # bool

# 2. 値と型を表示
print(f"age = {age}, type = {type(age)}")
print(f"height = {height}, type = {type(height)}")
print(f"name = {name}, type = {type(name)}")
print(f"is_student = {is_student}, type = {type(is_student)}")

# 3. かんたんな演算
print(f"来年の年齢: {age + 1}")
print(f"身長 +10cm: {height + 0.10}")
print(f"自己紹介: {name + 'です'}")
print(f"大学生かつ成人? {is_student and age >= 18}")
