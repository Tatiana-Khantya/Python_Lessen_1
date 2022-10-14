# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

task_string = 'fjkjjkal;afvmffkgoaooriosaadkkmvfk'
string = 'afv'

answer = "".join(task_string.split(string))

print(answer)
