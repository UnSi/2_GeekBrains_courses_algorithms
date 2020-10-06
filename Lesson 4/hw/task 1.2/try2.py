# Урок 3, задание 4. Определить, какое число в массиве встречается чаще всего.
from random import randint
import cProfile


def get_often_num(n):
    # rand_array = [randint(1, 5) for _ in range(n)]
    # print(rand_array)

    rand_array = []
    for i in range(n):
        rand_array.append(i % 5)
    result, max_count = [], 0

    for num in rand_array:
        count = 0
        for compare in rand_array:

            if num == compare:
                count += 1

            # если количество повторений совпало с максимальным - добавляем число в список результатов.
            if count == max_count:
                result.append(num)
            # если количество повторений превысило результат, заменяем список
            elif count > max_count:
                max_count = count
                result = [num]



# print(f"Числа {list(set(result))} встречались чаще всего, а именно: {max_count} раз")

# cProfile.run("get_often_num(100)")
#   На случайных числах:
#        814 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#       100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:244(randint)
#       100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.002    0.002    0.002    0.002 try2.py:6(get_often_num)
#         1    0.000    0.000    0.000    0.000 try2.py:7(<listcomp>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#       100    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       141    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

#  python -m timeit -n 1000 -s "import try2" "try2.get_often_num(10)"
#    "try2.get_often_num(10)"
# 1000 loops, best of 5: 41.2 usec per loop

#   "try2.get_often_num(100)"
# 1000 loops, best of 5: 1.98 msec per loop

# "try2.get_often_num(1000)" использовал 100 повторений, т.к. очень долго считало
# 100 loops, best of 5: 179 msec per loop


# На заранее подготовленной последовательности:
#  479 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 try2.py:6(get_often_num)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#       475    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# "try2.get_often_num(10)"
# 1000 loops, best of 5: 23.2 usec per loop

# "try2.get_often_num(100)"
# 1000 loops, best of 5: 1.8 msec per loop

#   "try2.get_often_num(1000)"
# 100 loops, best of 5: 179 msec per loop