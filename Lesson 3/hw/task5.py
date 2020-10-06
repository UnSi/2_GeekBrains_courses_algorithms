# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
from random import randint

MIN_VALUE = -100
rand_array = [randint(MIN_VALUE, 100) for _ in range(50)]
print(rand_array)
max_number = MIN_VALUE

for i, number in enumerate(rand_array):
    if 0 > number > max_number:
        max_number = number
        pos = i

print(f"Максимальное отрицательное число: {max_number}, индекс {pos}, позиция: {pos+1}")
