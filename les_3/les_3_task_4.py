# Определить, какое число в массиве встречается чаще всего.
# Постановка задачи

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
a = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(a)

# Решение задачи

max_f = 0

for i in range(len(a)):
    f = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            f += 1
    if f > max_f:
        max_f = f
        num = a[i]

if max_f > 1:
    print(f'Цифра {num} встречается {max_f} раз')
else:
    print(f'Все элементы списка уникальны')
