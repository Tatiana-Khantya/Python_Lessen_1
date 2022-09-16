# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random as rand
list1 = [1.1, 1.2, 3.1, 5, 10.01]
mx = list1[0]%1
mn = list1[0]%1
print(mx)
print(mn)
for i in range(1, len(list1)):
    if list1[i]%1 > mx:
        mx = round(list1[i]%1, 2)
    if list1[i]%1 > 0 and list1[i]%1 < mn:
        mn = round(list1[i]%1, 2)
    print(mx)
    print(mn)
    print('-'*5)
print(f'min = {mn}, max = {mx}, max-min = {mx-mn}')
