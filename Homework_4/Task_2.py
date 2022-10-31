# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

num = int(input("Задайте натуральное число N: "))

sieve = set(range(2, num+1))

prime_list = []
while sieve:
    prime = min(sieve)
    prime_list.append(prime)
    sieve -= set(range(prime, num + 1, prime))
#print(prime_list)
prime_list_num = []
for i in prime_list:
    if num% i == 0:
        prime_list_num.append(i)
print(prime_list_num)
