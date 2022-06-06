"""
1) Определение количества различных подстрок с использованием хеш-функции.
 Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:
p, a, pa, pap, apa, ap
"""
import hashlib

# s = 'papa'
s = input('Введите строку для определения количества различных подстрок: ')


def hash_contrast(s):
    plist = []
    long_plist = len(s)
    for i in range(long_plist + 1):
        for j in range(i + 1, long_plist + 1):
            if s[i:j] != s:
                plist.append(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())

    return len(set(plist))


total = hash_contrast(s)

print(total)
