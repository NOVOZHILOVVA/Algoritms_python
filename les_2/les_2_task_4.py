# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
import random

n = int(input('Введите количество (n) элеменотов: '))
summa_n = 0
element = 1
element_str = ''

while n > 0:
    if n == 1:
        element_str = element_str + str(element)
    else:
        element_str = element_str + str(element) + ', '
    summa_n = summa_n + element
    element = - element / 2
    n -= 1

print(f' Сумма элементов (n): {element_str}\n будет равна: {round(summa_n)}')

