# Урок 3, задание 4. Определить, какое число в массиве встречается чаще всего.
from random import randint
import cProfile


def get_often_num(n):
    rand_array = []
    for i in range(n):
        rand_array.append(i%5)

    # rand_array = [randint(1, 5) for _ in range(n)]
    # print(rand_array)
    result, max_count = [], 0

    for num in rand_array[::-1]:
        count = 0
        for compare in rand_array[::-1]:
            # удаляем каждое совпадение из массива, чтобы не пробегать его заново
            if num == compare:
                rand_array.remove(compare)
                count += 1

            # если количество повторений совпало с максимальным - добавляем число в список результатов.
            if count == max_count:
                result.append(num)
            # если количество повторений превысило результат, заменяем список
            elif count > max_count:
                max_count = count
                result = [num]

        # т.к. удаляются элементы из массива, цикл будет итерироваться вхолостую несколько раз
        if len(rand_array) == 0:
            break


    # print(f"Числа {list(set(result))} встречались чаще всего, а именно: {max_count} раз")
#
# cProfile.run("get_often_num(100)")

# На случайных числах:
#  7386 function calls in 0.009 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.009    0.009 <string>:1(<module>)
#      1000    0.001    0.000    0.002    0.000 random.py:200(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:244(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.002    0.002    0.009    0.009 try1.py:6(get_often_num)
#         1    0.000    0.000    0.003    0.003 try1.py:7(<listcomp>)
#         1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
#        12    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       773    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1596    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#      1000    0.005    0.000    0.005    0.000 {method 'remove' of 'list' objects}

#  python -m timeit -n 1000 -s "import try1" "try1.get_often_num(10)"
#  "try1.get_often_num(10)"
# 1000 loops, best of 5: 33.6 usec per loop

#  "try1.get_often_num(100)"
# 1000 loops, best of 5: 336 usec per loop

# "try1.get_often_num(1000)"
# 1000 loops, best of 5: 7.29 msec per loop

# На заранее заготовленной последовательности:
# 300 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 try1.py:6(get_often_num)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         5    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#       190    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       100    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}

# "try1.get_often_num(10)"
# 1000 loops, best of 5: 13 usec per loop

# "try1.get_often_num(100)"
# 1000 loops, best of 5: 131 usec per loop

# "try1.get_often_num(1000)"
# 1000 loops, best of 5: 5 msec per loop
