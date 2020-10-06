# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код
# и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2
from math import sqrt


def func_sieve(n, last=1000, sieve=[]):
    if not len(sieve):
        sieve = [i for i in range(last)]
        sieve[1] = 0
    else:
        for i in range(len(sieve), last+1):
            sieve.append(i)

    for i in range(2, last):

        if sieve[i] != 0:
            j = i * 2

            while j < last:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]
    if len(result) <= n:
        print(f"Число больше {last}")
        result = func_sieve(n, last * 10, sieve)
        return result
    return result[n-1]


def prime(n):
    start = 1
    counter = 0
    while True:
        start += 1
        if start != 2 or start != 3:
            break_point = False
            for i in range(2, int(sqrt(start))+1):
                if start % i == 0:
                    break_point = True
                    break
        if break_point:
            continue
        counter += 1

        if counter == n:
            return start


number = int(input(f"Введите, какое по счёту простое число необходимо"))
print(func_sieve(number))
print(prime(number))
