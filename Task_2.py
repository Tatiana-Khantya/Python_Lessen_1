# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("Введите значение x: "))
y = int(input("Введите значение y: "))
z = int(input("Введите значение z: "))

def checkPredicate(x, y, z):
    left = not (x or y or z)
    right = not x and not y and not z
    result = left == right
    return result

if checkPredicate(x, y, z) == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")