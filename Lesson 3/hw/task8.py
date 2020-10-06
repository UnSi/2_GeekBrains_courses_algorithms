# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

MATRIX_SIZE = 4

matrix = [[] for _ in range(MATRIX_SIZE+1)]

for i in range(MATRIX_SIZE+1):
    sum_line = 0
    for j in range(MATRIX_SIZE):
        matrix[i].append(int(input(f"Введите элемент {i+1, j+1}: ")))
        sum_line += matrix[i][j]
    matrix[i].append(sum_line)


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f"{matrix[i][j]:>4}", end='')
    print()
