# Урок 2, задание 4.
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Кол-во элементов (n) вводится с клавиатуры.
import cProfile
import functools


@functools.lru_cache()
def get_sum_iter(n, m=1):
    if n == 1:
        return m
    return m + get_sum_iter(n - 1, m / -2)


# n = int(input("Введите число"))
# print(get_sum_iter(n, 1))

# *********************************************
# cProfile.run("get_sum_iter(100, 1)")

#             103 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     100/1    0.000    0.000    0.000    0.000 try3.py:7(get_sum_iter)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ***************************************************

# >python -m timeit -n 1000 -s "import try3" "try3.get_sum_iter(10)"
#    "try3.get_sum_iter(10)"
# 1000 loops, best of 5: 195 nsec per loop

#  "try3.get_sum_iter(100)"
# 1000 loops, best of 5: 135 nsec per loop

# "try3.get_sum_iter(495)"
# 1000 loops, best of 5: 138 nsec per loop

# на 496 - ошибка из-за большого количества вызова