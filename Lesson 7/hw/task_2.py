# Отсортируйте по возрастанию методом слияния одномерный вещ. массив, заданный случ. числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

# указал 49,99, т.к. в задании сказано до 50 не включительно и округлил до 2 значений.
array = [round(random.uniform(0, 49.99), 2) for _ in range(10)]

# array = [4, 8, 6, 2, 9, 1, 7, 5, 3]
# array = [4, 9, 1]
# array = [46.68, 28.53, 25.19, 26.65, 28.66, 16.71, 13.92, 41.73, 26.67, 4.07]


def merge_sort(arr):
    # arr = arr.copy()  # если надо сохранять исходный массив - раскомментировать, иначе будет перезаписывать
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    l_arr = merge_sort(arr[:mid])
    r_arr = merge_sort(arr[mid:])
    # print("части: ", l_arr, r_arr)

    i, j = 0, 0
    while i < len(l_arr) and j < len(r_arr):
        if l_arr[i] < r_arr[j]:
            arr[i + j] = l_arr[i]
            i += 1
        else:
            arr[i + j] = r_arr[j]
            j += 1

    if i >= len(l_arr):
        arr[i + j:] = r_arr[j:]

    elif j >= len(r_arr):
        arr[i + j:] = l_arr[i:]

    return arr


print(array)
new_arr = merge_sort(array.copy())
print(new_arr)


def test(func1, func2, arr):
    return func1(arr) == func2(arr)


print(f"результат теста : {test(merge_sort, lambda arr: sorted(arr), array)}")