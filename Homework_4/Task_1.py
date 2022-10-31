# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

x = math.pi

# d = 0.001
# count = 0
# while d < 1:
#     count +=1
#     d *= 10

# for i in range(1,count+1):
#      d /= 10
# # print(d)
# print((count, round(x, count)))


d = 1
num = int(input("Введите количество знаков после запятой: "))
for i in range(1,num+1):
    d /= 10
# print(d)
print((num, round(x, num)))


