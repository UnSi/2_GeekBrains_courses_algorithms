# Урок 3, задание 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.
import cProfile


def search_div():
    for i in range(2, 10):
        result = []
        for j in range(2, 100):
            if j % i == 0:
                result.append(j)
        # print(f"На {i} делится {len(result)} чисел: {result}")


# cProfile.run("search_div()")
#
# 182 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 try1.py:5(search_div)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       178    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#  python -m timeit -n 1000 -s "import try1" "try1.search_div()"
# "try1.search_div()"
# 1000 loops, best of 5: 74.2 usec per loop