# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random as rand

num = int(input("Введите размер списка: "))
list1 = []
summ = 0
for i in range(num):
    list1.append(rand.randint(0, 20))
for i in range(len(list1)):
    if i%2 == 1:
        summ += list1[i]
print(list1)
print(summ)