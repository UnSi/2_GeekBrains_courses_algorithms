# Урок 3, задание 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.
# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
#
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.

# 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] win32
import sys


addresses = {}
var = {}


def search_div():
    result = [0] * 8
    for i in range(2, 100):
        for j in range(2, 10):
            if i % j == 0:
                result[j-2] += 1
            add_size(j)
        add_size(i)
    add_size(result)

    for i, item in enumerate(result):
        print(f"{i+2} : {item}")
        add_size(i)
        add_size(item)


def add_size(x, level = 0):
    if not id(x) in addresses:
        addresses[id(x)] = sys.getsizeof(x)
        var[id(x)] = [x, level]

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                add_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                add_size(xx, level + 1)


search_div()


print('*' * 50)

for k, v in var.items():
    print(f"{k}: {v} {addresses[k]} bytes")
print("Всего памяти заянто переменными: ", sum(addresses.values()))
print("Различных ячеек памяти: ", len(addresses))
# 2916