# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 4, 3, 1, 8]
# Ввод: 10
# [-10, -9, ...-4, -3, -2, -1, 0, 1, 2, 3,4....10]

num = int(input("Введите число N: "))
list1 = []
for i in range (-num, num+1):
    list1.append(i)
print(list1)

index = []
for i in input("Введите индексы: ").split():
    index.append(int(i))

mult = 1
for i in index:
    mult *= list1[i]
print(f'Произведение равно {mult}')