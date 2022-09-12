# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

num = int(input("Введите число N: "))
summ = 0
s = 0
list1 = {}
for i in range(1, num+1):
    s = (1+ 1 / i)**i
    list1[i] = s
    summ += s
print(list1)
print(summ)