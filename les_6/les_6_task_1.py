#  Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#  Например, если введено число 3486, надо вывести 6843.
from collections import deque
import sys


def total_size(data):
    print(f'{type(data)=} {sys.getsizeof(data)=} {data=}')

    def size(data):
        s = 0
        if hasattr(data, '__iter__'):
            if hasattr(data, 'items'):
                for key, value in data.items():
                    print(f'{type(key)=} {sys.getsizeof(key)=} {key=}')
                    print(f'{type(value)=} {sys.getsizeof(value)=} {value=}')
                    s += sys.getsizeof(key) + sys.getsizeof(value)
            elif not isinstance(data, str):
                for item in data:
                    print(f'{type(item)=} {sys.getsizeof(item)=} {item=}')
                    s += sys.getsizeof(item)
        s += sys.getsizeof(data)
        return s

    return size(data)


print('######################### Решение №1 ############################')
num = int(3486)
revers_num = 0

while num > 0:
    i = num % 10
    num = num // 10
    revers_num = revers_num * 10
    revers_num = revers_num + i

print(revers_num)
size_result = total_size(num) + total_size(revers_num) + total_size(i)
print(f'Сумма байт при использовании трех переменных равна: {size_result}')

print('######################### Решение №2 ############################')
num_list = [3, 4, 8, 6]
num_list = num_list[::-1]
print(num_list)
size_result = total_size(num_list)
print(f'Сумма байт при исползовании list равна: {size_result}')

print('######################### Решение №3 ############################')
num_deque = deque(str('3486'))
num_deque.reverse()
print(num_deque)
size_result = total_size(num_deque)
print(f'Сумма байт при исползовании deque равна: {size_result}')

'''  Для решения данной задачи рациональнее использовать три переменные класса int,
 а не создавать оболочку другого типа данных list, deque. Размер оболочки занимает много места.

Сумма байт при использовании трех переменных равна: 80
Сумма байт при исползовании list равна: 200
Сумма байт при исползовании deque равна: 824
 '''