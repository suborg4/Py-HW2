# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
list_size = int(input('Введите размер списка = '))
list = []
for i in range(list_size):
    list.append(random.randint(-list_size, list_size))

print(list)

mult = 1
file = open('file.txt', 'r')
for line in file:
    mult *= list[int(line)]
file.close()