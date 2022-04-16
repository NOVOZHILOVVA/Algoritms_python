# Написать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random

number_int_start = int(input('введите начальное целое число диапазаона случайных чисел: '))
number_int_stop = int(input('введите конечное целое число диапазаона случайных чисел: '))
number_int_rand = random.randint(number_int_start, number_int_stop)
print(f'Ваше случайное число {number_int_rand}')

number_float_start = float(input('введите начальное вещественное число диапазаона случайных чисел: '))
number_float_stop = float(input('введите конечное вещественное число диапазаона случайных чисел: '))
number_float_rand = random.random() * (number_float_stop - number_float_start) + number_float_start
print(f'Ваше случайное число {number_float_rand}')

symbol_start = ord(input('Ведите начальный символ диапазаона случайных символов a-z: '))
symbol_stop = ord(input('Ведите конечный символ диапазаона случайных символов a-z: '))
symbol_rand = chr(random.randint(symbol_start, symbol_stop))
print(f'Ваш случайный символ "{symbol_rand}"')
