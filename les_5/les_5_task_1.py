"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import namedtuple

Company = namedtuple('Company', ['name', 'income_1', 'income_2', 'income_3', 'income_4', 'total_income'])
n = int(input('Введите количество предприятий в отчетном периоде: '))
company = []
successful_company = []
failed_company = []
all_income = 0

for i in range(n):
    name = input(f'Введите название предприятия № {i + 1}: ')
    income_1 = int(input(f'Прибыль предприятия "{name}" за первый квартал: '))
    income_2 = int(input(f'Прибыль предприятия "{name}" за второй квартал: '))
    income_3 = int(input(f'Прибыль предприятия "{name}" за третий квартал: '))
    income_4 = int(input(f'Прибыль предприятия "{name}" за четвертый квартал: '))
    total_income = income_1 + income_2 + income_3 + income_4
    all_income += total_income
    company.append(Company(name, income_1, income_2, income_3, income_4, total_income))

average = all_income / n
print(f'Средняя прибыль за год предприятий составила {average} у.е.')

while n > 0:
    if company[n - 1].total_income > average:
        successful_company.append(str(company[n - 1].name) + ' ' + str(company[n - 1].total_income) + " у.е.")
    else:
        failed_company.append(str(company[n - 1].name) + ' ' + str(company[n - 1].total_income) + " у.е.")
    n -= 1

print(f'Список предприятий у которых прибыль выше среднего {successful_company}')
print(f'Список предприятий у который прибыль ниже среднего {failed_company}')

