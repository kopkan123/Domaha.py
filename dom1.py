# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
s = input("Введите трехзначное число что бы найти сумму его чисел: ")
num = 0
if len(s) == 3:
    for i in s:
        num += int(i)
    print(F"Суммой трех чилес является: {num}")
else:
    print("Это не трехзначное число")