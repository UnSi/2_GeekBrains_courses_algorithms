#  Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
#  1+2+...+n = n(n+1)/2, где n — любое натуральное число.


def sum_int(n):
    if n == 1:
        return n
    return n + sum_int(n - 1)


n = int(input("Введите число:"))
print(sum_int(n) == n * (n + 1) / 2)
