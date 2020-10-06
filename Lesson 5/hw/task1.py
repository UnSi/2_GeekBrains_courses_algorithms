# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.
from collections import defaultdict, Counter
# from random import uniform


def dict_print(dict: dict):
    for k, v in dict.items():
        print(f'Прибыль компании {k} за 4 квартала: ')
        print(v, '\n')


n = int(input("Введите количество предприятий: "))
# n = 4

company_dict = defaultdict(int)
for i in range(n):
    company_name = input('Введите название компании:\n')
    # company_dict[company_name] = [float(input(f'прибыль за {j+1}-й квартал')) for j in range(4)]
    # company_name = f'comp_{i + 1}'

    for j in range(4):
        # spam = round(uniform(0, 1000000), 2)
        # spam = 1000
        spam = round(float(input(f'прибыль за {j + 1}-й квартал')), 2)
        company_dict[company_name] += spam


dict_print(company_dict)

avg = round(sum(company_dict.values()) / n, 2)
print('Средний доход: ', avg)
comp_count = Counter(company_dict)
for k in comp_count:
    comp_count[k] -= avg

undo_keys = (-comp_count).keys()
over_keys = (+comp_count).keys()
other = comp_count.keys() - undo_keys - over_keys

print("Компании, чей доход ниже среднего: ", *undo_keys or 'отсутствуют')
print("Компании, чей доход выше среднего: ", *over_keys or 'отсутствуют')
print("Компании, чей доход является средним: ",*other or 'отсутствуют')

# если нужна будет прибыль, её можно достать по ключам, но в задании этого нет.




