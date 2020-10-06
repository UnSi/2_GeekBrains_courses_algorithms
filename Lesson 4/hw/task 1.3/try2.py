# Урок 3, задание 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.
import cProfile


def search_div():
    result = [[] for _ in range(8)]
    for i in range(2, 100):
        for j in range(2, 10):
            if i % j == 0:
                result[j-2].append(i)

    # for i, line in enumerate(result):
    #     print(f"{i+2} {len(line)} : {line}")


# search_div()
# cProfile.run("search_div()")
#
# 183 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 try2.py:6(search_div)
#         1    0.000    0.000    0.000    0.000 try2.py:7(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       178    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#  python -m timeit -n 1000 -s "import try2" "try2.search_div()"
#  "try2.search_div()"
# 1000 loops, best of 5: 143 usec per loop