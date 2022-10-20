# Задайте число. Составьте список чисел Фибоначчи, в том числе 
# для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

nul = 0
first = 1
sec = 1
num = int(input("Введите количество чисел Фибоначчи: "))

if (num == 1):
    print(1)
elif (num == 2):
    print (1, 1)
else:
    print (nul, first, sec, end =' ')
    for i in range (2, num-1):
        first, sec = sec, first + sec
        print (sec, end = ' ')




 
