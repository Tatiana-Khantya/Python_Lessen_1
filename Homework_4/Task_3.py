# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

# numbers = [1, 5, 2, 3, 6, 4, 5, 6]

# unique_numbers = list(set(numbers))
# print(unique_numbers)

numbers = [1, 5, 2, 3, 6, 4, 5, 6]
result = []
for i in numbers:
    if numbers.count(i) < 2:
        result.append(i)
print(result)