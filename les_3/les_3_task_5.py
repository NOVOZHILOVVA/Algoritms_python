# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Постановка задачи

import random

SIZE = 10
MIN_ITEM = - 100
MAX_ITEM = 100
a = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(a)

# Решение задачи
N = len(a)

for i in range(N):
    f = False
    for j in range(N):
        if a[j] < 0 and a[i] < 0:
            f = True
            if a[i] < a[j] and i != j:
                f = False
                break
    if f:
        print(f' Максимальный отрицательный элемент в массиве равен {a[i]}, позиция {i}')

