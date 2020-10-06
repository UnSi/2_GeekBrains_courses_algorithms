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
    result = [[] for _ in range(8)]
    for i in range(2, 100):
        for j in range(2, 10):
            add_size(j)
            if i % j == 0:
                result[j-2].append(i)
        add_size(i)
    add_size(result)
    for i, line in enumerate(result):
        print(f"{i+2} {len(line)} : {line}")
        add_size(i)
        add_size(line)


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

# 5020