# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = input('Введите число: ')
count_even = 0
count_not_even = 0
str_even = ''
str_not_even = ''

for n in number:
    if int(n)%2 == 0:
        count_even += 1
        str_even = f'{str_even} {n}'
    else:
        count_not_even += 1
        str_not_even = f'{str_not_even} {n}'

print(f'Четных цифр - {count_even}, а именно:{str_even}\nНечетных цифр - {count_not_even}, а именно:{str_not_even} ')