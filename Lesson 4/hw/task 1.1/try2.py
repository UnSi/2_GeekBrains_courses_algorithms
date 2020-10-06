# Урок 2, задание 4.
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Кол-во элементов (n) вводится с клавиатуры.
import cProfile


def get_sum_iter(n):
    summ = 0
    start = 1
    for i in range(n):
        summ += start
        start /= -2


# *********************************************
# cProfile.run("get_sum_iter(100)")

#                     4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 try2.py:5(get_sum_iter)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ***************************************************

# >python -m timeit -n 1000 -s "import try2" "try2.get_sum_iter(10)"
#    "try2.get_sum_iter(10)"
# 1000 loops, best of 5: 1.97 usec per loop

#   "try2.get_sum_iter(100)"
# 1000 loops, best of 5: 13.1 usec per loop

#  "try2.get_sum_iter(500)"
# 1000 loops, best of 5: 67.2 usec per loop

# "try2.get_sum_iter(1000)"
# 1000 loops, best of 5: 143 usec per loop