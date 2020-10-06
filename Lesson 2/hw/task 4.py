# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Кол-во элементов (n) вводится с клавиатуры.


# не так прочитал задание, полчаса ломал голову с рекурсией, вывел последовательность
"""
def get_iter(n, m):
    if n==1:
        return m
    return f'{m}, {get_iter(n-1,m/-2)}'

print(get_iter(10,1))
"""

# сделал цикл
"""
n = int(input("Введите число"))
sum = 0
for i in range(n):
    if i == 0:
        start = 1
    else:
        start /= -2
    sum += start
print(sum)
"""


# Понял, что рекурсией лучше. На каждый вариант делал блок схему, оставил последний вариант

def get_sum_iter(n, m):
    if n == 1:
        return m
    return m + get_sum_iter(n - 1, m / -2)


n = int(input("Введите число"))
print(get_sum_iter(n, 1))
