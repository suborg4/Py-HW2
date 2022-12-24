# Реализуйте алгоритм перемешивания списка.

import random
list_size = int(input('Введите размер списка = '))
list = list(range(0,list_size))
for i in range(0,list_size):
    j = random.randint(0, list_size-1)
    list[j], list[i] = list[i], list[j]
print(f"{list}")