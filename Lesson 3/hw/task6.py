# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import randint
min_value = 1
max_value = 100
rand_array = [randint(min_value, max_value) for _ in range(10)]
print(rand_array)
max_value, min_value = min_value, max_value

min_idx = 0
max_idx = 0
for i, number in enumerate(rand_array):
    if number > max_value:
        max_value, max_idx = number, i
    if number < min_value:
        min_value, min_idx = number, i

if max_idx < min_idx:
    max_idx, min_idx = min_idx, max_idx

sum_arr = 0
for i in rand_array[min_idx+1: max_idx]:
    sum_arr += i

print(f"Минимамальное число: {min_value}, максимальное число: {max_value} , сумма элементов между ними: {sum_arr} ")