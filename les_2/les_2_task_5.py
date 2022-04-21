#  Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
#  Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

n = 32
m = 128
a = 0
ten_str = ''

while n < m:
    elements = chr(n)
    a = a + 1
    n = n + 1
    ten_str = ten_str + elements + ' ' + str(ord(elements)) + '  '
    if a % 10 == 0:
        print(ten_str)
        ten_str = ''
    elif n == m:
        print(ten_str)
