"""Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;"""

import hashlib


def get_uniq_substring_count(s):
    uns = set()
    length = len(s)
    h = hashlib.sha1(s.encode('utf-8')).hexdigest()
    for i in range(length):
        for j in range(i + 1, length+1):
            sb = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
            uns.add(sb)
    uns.remove(h)
    return len(uns)


st = input('Введите строку: ')
print(f'Количество различных подстрок: {get_uniq_substring_count(st)}')
