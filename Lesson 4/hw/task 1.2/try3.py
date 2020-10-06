# Урок 3, задание 4. Определить, какое число в массиве встречается чаще всего.
from random import randint
import cProfile

def get_often_num(n):
    rand_array = [randint(1, 5) for _ in range(n)]
    # print(rand_array)

    # rand_array = []
    # for i in range(n):
    #     rand_array.append(i % 5)
    result, max_count = [], 0
    
    for i, num in enumerate(rand_array):
        count = 0
        for compare in rand_array[i:]:
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

# cо случайными числами:
#  653 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:244(randint)
#       100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.001    0.001    0.001    0.001 try3.py:5(get_often_num)
#         1    0.000    0.000    0.000    0.000 try3.py:6(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        76    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       172    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

#  python -m timeit -n 1000 -s "import try3" "try3.get_often_num(10)"
# "try3.get_often_num(10)"
# 1000 loops, best of 5: 33.7 usec per loop

# "try3.get_often_num(100)"
# 1000 loops, best of 5: 1.28 msec per loop

# "try3.get_often_num(1000)"
# 100 loops, best of 5: 96.3 msec per loop

# с фиксированной последовательностью:
#    194 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 try3.py:6(get_often_num)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       190    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#  python -m timeit -n 1000 -s "import try3" "try3.get_often_num(10)"
#  "try3.get_often_num(10)"
# 1000 loops, best of 5: 16.3 usec per loop

#   "try3.get_often_num(100)"
# 1000 loops, best of 5: 940 usec per loop

# "try3.get_often_num(1000)" использовал 100 повторений, т.к. очень долго считало
# 100 loops, best of 5: 90.3 msec per loop

