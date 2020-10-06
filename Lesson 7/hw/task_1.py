# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random

# указал 99, т.к. в задании сказано до 100 не включительно.
array = [random.randint(-100, 99) for _ in range(10)]

'''
array = [62, 15, 2, -5, -4, 88, 27, -40, 43, 39]


def bubble_sort_classic(arr):
    arr = arr.copy()
    # iter_count = 0
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            # iter_count += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
        print(arr)
    # print(iter_count)
    return arr
'''


def bubble_sort(arr: list):
    # iter_count = 0

    arr = arr.copy()
    n = 1
    start = 0  # если начало последовательности уже упорядочено, начнем с последнего элемента упорядоченной части

    while n < len(arr):
        count = 0  # счётчик уже упорядоченного начала последовательности
        flag = True  # нужнен для проверки, что это именно начало массива
        for i in range(start, len(arr) - n):
            # iter_count += 1
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

                if not count:
                    flag = False
                    start = 0
                else:
                    start = count - 1
                    flag = False

            elif flag:
                count += 1
        n += 1
        if flag:
            break
    # print(iter_count)
    return arr


# array = [i for i in range(10)][::-1]
# array[-1], array[-2] = array[-5], array[-1]
# array = [-45, 5, 99, -55, -81, -81, -71, -15, -28, 97]
# new_arr = bubble_sort_classic(array)
new_arr = bubble_sort(array)
print(array)
print(new_arr)


def test(func1, func2, arr):
    return func1(arr) == func2(arr)


print(f"результат теста : {test(bubble_sort, lambda arr: sorted(arr, reverse=True), array)}")
