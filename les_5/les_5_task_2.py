"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


def summa_16(a, b):
    suma_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                 0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
                 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    res_1 = 0
    res_2 = 0
    sum_res = deque()

    if len(a) > len(b):
        a, b = deque(a), deque(b)
    else:
        a, b = deque(b), deque(a)

    while len(a) > 0:
        if len(a) >= len(b) != 0:
            res_1 = suma_dict[a.pop()] + suma_dict[b.pop()] + res_2
            res_2 = 0
            if res_1 >= 16:
                res_2 = res_1 // 16
                res_1 = res_1 % 16
            sum_res.appendleft(suma_dict[res_1])
        else:
            if res_1 >= 16:
                res_2 = res_1 // 16
                res_1 = res_1 % 16
                res_1 = suma_dict[a.pop()] + res_2
            else:
                res_1 = suma_dict[a.pop()] + res_2
                res_2 = 0
                if res_1 >= 16:
                    res_2 = res_1 // 16
                    res_1 = res_1 % 16
            sum_res.appendleft(suma_dict[res_1])
        if len(a) == 0 and res_2 != 0:
            sum_res.appendleft(suma_dict[res_2])
    return sum_res


print(summa_16('C4F', 'A2'))


def mult_16(a, b):
    a = deque(a)
    b = deque(b)
    suma = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
            0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
            10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    mult_rest = deque()
    mult_rest_2 = deque()
    for i in range(len(a) - 1, -1, -1):
        res_02 = 0
        for j in range(len(b) - 1, -1, -1):
            res_01 = suma[a[i]] * suma[b[j]] + res_02
            res_02 = 0
            if res_01 >= 16:
                res_02 = res_01 // 16
                res_01 = res_01 % 16
            mult_rest.appendleft(suma[res_01])
            if j == 0 and res_02 > 0:
                mult_rest.appendleft(suma[res_02])
            if j == 0:
                mult_rest_2.appendleft(mult_rest)
                mult_rest = deque()
    if len(mult_rest_2) > 2:
        for i in range(len(mult_rest_2)):
            n = i
            while (len(mult_rest_2) - 1) > n:
                if n == (len(mult_rest_2) - 1):
                    pass
                else:
                    mult_rest_2[i].append(0)
                    n += 1

        mult_rest_3 = deque()

        while len(mult_rest_2) > 1:
            if len(mult_rest_2) // 2 != 0:
                for i in range(len(mult_rest_2) // 3):
                    mult_rest_3.append(summa_16((summa_16(mult_rest_2[i], mult_rest_2[i + 1])), mult_rest_2[i + 2]))
            else:
                for i in range(len(mult_rest_2) // 2):
                    mult_rest_3.append(summa_16(summa_16(mult_rest_2[i], mult_rest_2[i + 1])))
            mult_rest_2 = mult_rest_3
    return mult_rest_2


print(mult_16('C4F', 'A2'))




