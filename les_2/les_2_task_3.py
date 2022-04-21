#  Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#  Например, если введено число 3486, надо вывести 6843.

num = int(input('Введите число чтобы получить обратное по порядку: '))
revers_num = 0

while num > 0:
    i = num % 10
    num = num // 10
    revers_num = revers_num * 10
    revers_num = revers_num + i

print(revers_num)
