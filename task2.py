# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Программа принимает на вход число N')
print('и выдает набор произведений чисел от 1 до N')
N = int(input('Введите число N: '))
sum = 1
    
for item in range(1, N + 1):
    sum *= item
    print(sum )