# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

x = int(input('Введите трехзначное число abc: '))

a = x // 100
b = (x % 100) // 10
c = x % 10

sum_abc = a + b + c
prod_abc = a * b * c

print(f'Сумма abc: {sum_abc}, произведение abc: {prod_abc}')