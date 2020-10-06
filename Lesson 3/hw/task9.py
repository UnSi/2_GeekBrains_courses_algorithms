# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы

from random import randint

MATRIX_SIZE = 5
min_value = 1
max_value = 100
matrix = [[randint(min_value, max_value) for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]


def matr_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]:>4}", end='')
        print()


min_list = [max_value for _ in range(MATRIX_SIZE)]
max_el = min_value

for i in range(MATRIX_SIZE):
    for j in range(MATRIX_SIZE):
        if matrix[j][i] < min_list[i]:
            min_list[i] = matrix[j][i]
    if min_list[i] > max_el:
        max_el = min_list[i]

matr_print(matrix)
print(f"Минимальные элементы каждого столбца: {min_list}. Максимальный из них: {max_el}")