# 5 Реализовать алгоритм перемешивания списка.

import random as rand

list1 = []
list2 = []
n = int(input("введите размер списка: "))
for i in range(n):
    list1.append(rand.randint(-10, 10))
print(list1)
for i in range(n):
    x = rand.randint(0, len(list1)-1)
    y = list1.pop(x)
    list2.append(y)
print(list2)
