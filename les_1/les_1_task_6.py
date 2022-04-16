# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

symbol_user = int(input('Введите номер буквы в алфавите: '))

symbol_place = chr(96 + symbol_user)

print(f'Буква под номером {symbol_user} это: {symbol_place}')
