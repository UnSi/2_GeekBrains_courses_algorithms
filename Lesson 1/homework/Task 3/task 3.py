# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
import random

mode = input("Введите режим работы: 1 - случайное целое, 2 - случайное вещ., 3- случайный символ\n")
min_param, max_param = input("Введите минимум и максимум через пробел: \n").split()
if min_param > max_param:
    min_param, max_param = max_param, min_param

if mode == '1':
    print(f"Случайное целое число: {random.randint(int(min_param), int(max_param))} ")
elif mode == '2':
    print(f"Случайное вещественное число: {random.uniform(float(min_param), float(max_param))}")
else:
    print(f"Случайный символ: {chr(random.randint(ord(min_param), ord(max_param)))}")