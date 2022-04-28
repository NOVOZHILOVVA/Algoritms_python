# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из
# чисел в диапазоне от 2 до 9.

# Решение задачи

a = []
b = []
c = []

for i in range(2, 100):
    a.append(i)

for i in range(2, 10):
    b.append(i)

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] % b[j] == 0:
            c.append(b[j])

for i in range(len(b)):
    n = 0
    for j in range(len(c)):
        if b[i] == c[j]:
            n += 1
    print(f' {b[i]} кртано {n} раз в диапазоне от 2 до 99')
