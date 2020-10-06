# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

rand_array = [randint(1, 100) for _ in range(100)]

min_el = max_el = rand_array[0]
min_idx = max_idx = 0

for i, num in enumerate(rand_array):
    if num > max_el:
        max_el, max_idx = num, i
    if num < min_el:
        min_el, min_idx = num, i


print(f"Максимальный: {max_el} на месте: {max_idx+1}\nМинимальный: {min_el} на месте: {min_idx+1}")
rand_array[max_idx], rand_array[min_idx] = rand_array[min_idx], rand_array[max_idx]
print(rand_array)
