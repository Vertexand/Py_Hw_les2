# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:  6782 -> 23, 0,67 ->13,  0,56 -> 11

num = float(input('Enter number: '))# вар 1

num_int = int(str(num).replace('.', ''))#заменять
sum = 0

while num_int > 0:
    cut_digit = num_int % 10
    sum += cut_digit
    num_int //= 10

print(sum)

# num = float(input('введите число: '))  # вар 2 (Без работы с методами строк.
# sum_digits = 0

# power = len(str(num)) - 2
# num *= 10 ** power

# while num:
#     sum_digits += num % 10
#     num //= 10

# print(int(sum_digits))

# num_1 = input ("введите ")# вар 3 короткий
# print(sum([int(i) for i in num_1 if i.isdigit()]))