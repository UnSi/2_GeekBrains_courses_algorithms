# Урок 3, задание 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.
import cProfile


def search_div():
    result = [0] * 8
    for i in range(2, 100):
        for j in range(2, 10):
            if i % j == 0:
                result[j-2] += 1

    # for i, item in enumerate(result):
    #     print(f"{i+2} : {item}")


# cProfile.run("search_div()")
#
#   4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 try3.py:6(search_div)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#  python -m timeit -n 1000 -s "import try3" "try3.search_div()"
#  "try3.search_div()"
# 1000 loops, best of 5: 141 usec per loop