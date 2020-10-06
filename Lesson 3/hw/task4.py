# 4. Определить, какое число в массиве встречается чаще всего.
from random import randint

rand_array = [randint(1, 5) for _ in range(50)]
print(rand_array)
# compare_array = rand_array[:]
result, max_count = [], 0
# iter_counter = 0

for num in rand_array[::-1]:
    count = 0
    for compare in rand_array[::-1]:
        # удаляем каждое совпадение из массива, чтобы не пробегать его заново
        if num == compare:
            rand_array.remove(compare)
            count += 1

        # если количество повторений совпало с максимальным - добавляем число в список результатов.
        if count == max_count:
            result.append(num)
        # если количество повторений превысило результат, заменяем список
        elif count > max_count:
            max_count = count
            result = [num]
        # iter_counter += 1

    # т.к. удаляются элементы из массива, цикл будет итерироваться вхолостую несколько раз
    if len(rand_array) == 0:
        break

# print(iter_counter)
print(f"Числа {list(set(result))} встречались чаще всего, а именно: {max_count} раз")

