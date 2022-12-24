# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

print('Программа считает сумму цифр введенного числа')
number = input('Введите число: ')
sumDigits = 0

for item in number:
    if item.isdigit():
        sumDigits += int(item)
print(sumDigits)