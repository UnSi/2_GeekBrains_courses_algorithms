# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
# задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом

import re
from collections import deque, OrderedDict

LETTER_DICT = OrderedDict({'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15})


def get_hex_deque():
    while True:
        num = input('Введите число в 16-ричной системе счисления: ').upper()
        # num_1 = '123132asdas'.upper()
        # num_1 = 'ssss'.upper()
        need = re.search(r'[0-9A-F]+', num)
        if need:
            # print(need)
            num = deque(need[0])
            break
        else:
            print('Строка не содержит числа в 16-ричной системе счисления')
    return num


def convert_letter(spam: deque, key='indigit'):
    num = spam.copy()
    if not num:
        return deque([0])

    for i, item in enumerate(num):
        num[i] = str(item)

    if key == 'indigit':
        for count, item in enumerate(num):
            if item in 'ABCDEF':
                num[count] = LETTER_DICT[item]
            else:
                num[count] = int(item)
    else:
        for count, item in enumerate(num):
            if item in ('10', '11', '12', '13', '14', '15') :
                num[count] = list(LETTER_DICT.keys())[int(item)-10]
            else:
                num[count] = str(item)

    return num


def sum_hex(num_1:deque, num_2:deque):
    dif = 0
    num_1 = convert_letter(num_1)
    num_2 = convert_letter(num_2)

    if len(num_1) < len(num_2):
        num_1, num_2 = num_2, num_1
    for i in range(len(num_1) - len(num_2)):
        num_2.appendleft(0)

    result = deque()

    for i in range(len(num_1))[::-1]:
        res = (num_1[i] + num_2[i] + dif) % 16
        dif = (num_1[i] + num_2[i] + dif) // 16
        result.appendleft(res)

    if dif > 0:
        result.appendleft(dif)
    result = convert_letter(result, key='inletter')
    return result


def mult_hex(num_1:deque, num_2:deque):
    num_1 = convert_letter(num_1)
    num_2 = convert_letter(num_2)

    result = deque()

    for j in range(len(num_2))[::-1]:
        dif = 0
        prev = result.copy()
        result = deque()

        # Если 0 - нет смысла считать
        if num_2[j] == 0:
            result.append(0)
        else:
            for i in range(len(num_1))[::-1]:
                res = (num_2[j]*num_1[i] + dif) % 16
                dif = (num_2[j]*num_1[i] + dif) // 16
                result.appendleft(res)
            if dif > 0:
                result.appendleft(dif)

        # сдвиг влево
        spam = len(num_2) - j - 1
        if spam != 0:
            for j in range(spam):
                result.append(0)

        result = convert_letter(result, key='inletter')
        result = sum_hex(prev, result)

    result = convert_letter(result, key='inletter')
    return result


# number_1 = get_hex_deque()
# number_2 = get_hex_deque()
number_1 = deque('FCDF25')
number_2 = deque('FCDF25')
# number_1 = deque('A2')
# number_2 = deque('C4F')
# print(number_1)
# print(convert_letter(number_1))

print(f"введены числа{list(number_1), list(number_2)}")

print(f"Сумма чисел: {list(sum_hex(number_1, number_2))}")
print(f"Произведение чисел: {list(mult_hex(number_1, number_2))}")
