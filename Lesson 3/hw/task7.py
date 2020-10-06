# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
from random import randint

min_value = 1
max_value = 100
rand_array = [randint(min_value, max_value) for _ in range(20)]
print(rand_array)

first_min = max_value
second_min = max_value

for i in rand_array:
    if i < first_min:
        first_min, second_min = i, first_min
    elif i < second_min:
        second_min = i

print(f"2 наименьших эл-та: {first_min, second_min}")