# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
a = int(input('Enter number: '))
if a == 6 or a == 7:
    print("yes")
elif 0 < a < 6 :
    print('no')
else:
    print('there is no such a day of week')