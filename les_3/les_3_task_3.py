# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# Постановка задачи

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
a = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(a)

# Решение задачи
b = []
N = len(a) - 1

for i in range(N):
    f = True
    for j in range(N):
        if a[i] < a[j] and i != j:
            f = False
            break
    if f:
        pos_max = i

for i in range(N):
    f = True
    for j in range(N):
        if a[i] > a[j] and i != j:
            f = False
            break
    if f:
        pos_min = i

pos_one = pos_max
pos_to = pos_min

if pos_max > pos_min:
    while pos_max > pos_min:
        a[pos_max], a[pos_max - 1] = a[pos_max - 1], a[pos_max]
        pos_max -= 1
    while pos_min + 1 < pos_one:
        a[pos_min + 1], a[pos_min + 2] = a[pos_min + 2], a[pos_min + 1]
        pos_min += 1
else:
    while pos_min > pos_max:
        a[pos_min], a[pos_min - 1] = a[pos_min - 1], a[pos_min]
        pos_min -= 1
    while pos_max + 1 < pos_to:
        a[pos_max + 1], a[pos_max + 2] = a[pos_max + 2], a[pos_max + 1]
        pos_max += 1

print(a)
print(f' Позиция максимального числа до перемещения {pos_one},\n '
      f'Позиция минимального числа до перемещения {pos_to}')

