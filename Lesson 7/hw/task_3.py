# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import collections
import random
import functools


m = random.randint(2, 20)
m = 1000
array = [random.randint(0, 100) for _ in range(2 * m + 1)]
# array = [i%10 for i in range(201)]
# array = [93, 49, 99, 58, 68, 11, 17, 55, 94, 67, 68, 36, 70, 0, 64, 33, 37, 64, 87, 40, 79, 3, 97, 6, 82, 24, 98, 62, 93, 50, 87, 78, 91]
# array = [22, 28, 6, 0, 18, 11, 11, 95, 82, 18, 9, 92, 10, 48, 49, 57, 39, 41, 99, 96, 45, 60, 75, 41, 63, 17, 38]
# m = len(array)//2
# array = [1, 2, 3, 4, 3, 2, 1]
# m = len(array)//2
# print(array)
# m = 5
# array = [28, 0, 35, 53, 81, 45, 96, 47, 59, 55, 9]
# array = [0, 1, 5, 2, 7, 4, 3, 1, 5, 7, 2]
# print(sorted(array)[m])  # 47



functools.lru_cache()
def search_med(arr, need=m):
    def _order_arr(arr, idx):
        # print(arr, idx)
        deq = collections.deque([arr[idx]])
        new_idx = 0
        for item in arr[:idx] + arr[idx + 1:]:
            if item > arr[idx]:
                deq.append(item)
            else:
                deq.appendleft(item)
                new_idx += 1
        return list(deq), new_idx

    arr = arr.copy()
    arr, idx = _order_arr(arr, need)

    if idx == need:
        return arr
    elif idx < need:
        arr[idx:] = search_med(arr[idx:], need - idx)
        return arr
    elif idx > need:
        arr[:idx] = search_med(arr[:idx], need)
        return arr


# Вариация Тимошина
def search_med_2(arr):
    for i in range(len(arr)):
        bigger = lesser = count = 0
        for j in range(len(arr)):
            if i != j:
                if arr[i] > arr[j]:
                    bigger += 1
                if arr[i] < arr[j]:
                    lesser += 1
                if arr[i] == arr[j]:
                    count += 1

        if abs(bigger - lesser) <= count:
            median = arr[i]
            break
    return median


def test(func1, func2, arr):
    return func1(arr)[m] == func2(arr)[m] and sum(func1(arr)[:m]) == sum(func2(arr)[:m]) and sum(func1(arr)[m:]) == sum(
        func2(arr)[m:])
    # return func1(arr)[m] == func2(arr)


print(f"Исходный массив: {array}")
new_arr = search_med(array)
print(f"Отсортированный массив: {new_arr}\nмедиана: {new_arr[m]}")
# res = test(search_med, search_med_2, array)
res = test(search_med, lambda arr: sorted(arr), array)
print(f"результат теста (проверяет медиану, сумму элементов справа, сумму элементов слева): {res}")
