# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

num = int(input("Введите число N: "))
list = ''
mult = 1
list1 = []
for i in range (-num, num+1):
    list1.append(i)
with open ('Homework_2/file.txt', 'r') as f:
    list = f.readline()
list2 = list.split(',')
for i in list2:
    mult *= list1[int(i.strip())]
print(mult)