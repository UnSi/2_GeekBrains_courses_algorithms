# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * задача считается решённой, если в коде использована функция вычисления хеша (hash(), sha1() или любая другая из модуля hashlib)
import hashlib


def search_uniq_subs(s: str) -> int:
    assert len(s), 'Строка должна быть не пустая'

    dif_list = []

    for start in range(len(s)):
        for size in range(1, len(s) - start + 1):

            if start == 0 and size == len(s):
                continue

            spam = hashlib.sha1(s[start:start + size].encode('utf-8')).hexdigest()
            # spam = s[start:start+size]
            # print(spam)
            if spam not in dif_list:
                dif_list.append(spam)
    # print(dif_list)

    # в условии сказано, что в сумму не включаем пустую строку. Не понял зачем, но на всякий случай сделал проверку.
    # эта функция проверяет как минимум 1 символ, пустых строк не должно быть.
    spam = hashlib.sha1(''.encode('utf-8')).hexdigest()
    if spam in dif_list:
        dif_list.remove(spam)

    return len(dif_list)


s_1 = input("Введите строку: ")
count = search_uniq_subs(s_1)

print(f'В строке {count} различных подстрок')
