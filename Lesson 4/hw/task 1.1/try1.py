# Урок 2, задание 4.
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Кол-во элементов (n) вводится с клавиатуры.
import cProfile

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
#     100/1    0.000    0.000    0.000    0.000 try1.py:5(get_sum_iter)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ***************************************************

# >python -m timeit -n 1000 -s "import try1" "try1.get_sum_iter(10)"
#   "try1.get_sum_iter(10)"
# 1000 loops, best of 5: 3 usec per loop

#  "try1.get_sum_iter(100)"
# 1000 loops, best of 5: 31.7 usec per loop

# "try1.get_sum_iter(500)"
# 1000 loops, best of 5: 205 usec per loop

# больше 991 - ошибка из-за большого количества вызова