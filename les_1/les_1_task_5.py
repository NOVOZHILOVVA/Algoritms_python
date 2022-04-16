# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

symbol_one = input('Введите превый символ: ')
symbol_to = input('Введите второй символ: ')

place_symbol_one = ord(symbol_one) - 96
place_symbol_to = ord(symbol_to) - 96
diatance_symbol = ord(symbol_to) - ord(symbol_one)

print(f'Первый символ в алфавите находится под номером: {place_symbol_one}')
print(f'Второй символ в алфавите находится под номером: {place_symbol_to}')
print(f'Между ними находится количество букв: {diatance_symbol}')