# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.


def sum_digits(number):
    if number//10 == 0:
        return number%10
    return number%10 + sum_digits(number//10)


number = int(input("Введите количество чисел"))
max = 0
result = ''

for i in range(number):
    n = int(input(f"Введите {i+1}-е число: "))
    sd = sum_digits(n)
    if sd > max:
        max = sd
        result = f'Максимальное число: {n}, сумма цифр: {max}'

print(result)



