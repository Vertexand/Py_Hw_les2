# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# 6-> [ 1, 2, 6, 24, 120, 720]

# На//пишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
# num = float(input('Enter any real number: '))

# num_int = int(str(num).replace('.', ''))
# sum = 0

# while num_int > 0:
#     cut_digit = num_int % 10
#     sum += cut_digit
#     num_int //= 10

# print(sum)

# выдает произведений чисел от 1 до n
# n = int(input())
# l = list()
# count = 1
# for i in range(1, n + 1):
#     count *= i
#     print(l.append(count))

# n = int(input())
# l = {}
# total = 0
# for i in range(1, n + 1):
#     l[i] = int(round((1 + 1 / i) ** i, 0))
#     total += l[i]
# print(l, total)

# pflf
# n = int(input('Задайте список: '))
# pos_1 = int(input('Позиция 1: '))
# pos_2 = int(input('Позиция 2: '))
# l = []
# for i in range(-n, n + 1):
#     l.append(i)
# print(l, l[pos_1 - 1] * l[pos_2 - 1])


# перемеш списка
# import random
# list = [1, 2, 3, 4, 5, 6]
# random.shuffle(list)
# print(list)

# import random
# n = int(input('Задайте список: '))
# l = []
# for i in range(-n, n + 1):
#     l.append(i)
# print(l)
# random.shuffle(l)
# print(l)

# listik = [i for i in range(10)]#пример
# print(listik)

# n=int(input())#пример
# listik = [i for i in range(-n, n+1)]
# print(listik)


# f = open(file.txt, r)#не работ
# data = f.read()  # пример
# print(data)


# with open('readme.txt') as f:  # пример#
#     lines = f.readlines()

# open(path_to_file, mode)

# print(lines)

# with open("file.txt", "r") as f:  # пример
# lines = f.readlines()

# print(lines.read)

# f = open('file.txt', 'r')
# print(f.readline())

# # with open("file.txt", 'r') as f:
# #     print(f.read)

# random.randint(2, 6)
# random.randrange(2, 6)
