# 5. Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random
# 10 -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import randrange

num = int(input('введите n: '))
nums_list = list(range(num))
print(nums_list)

for i in range(num):
    n_1, n_2 = randrange(num), randrange(num)
    nums_list[n_1], nums_list[n_2] = nums_list[n_2], nums_list[n_1]

print(nums_list)

# import random# вар 2
# list = [1, 2, 3, 4, 5, 6]
# random.shuffle(list)
# print(list)

# import random  # вар 3
# n = int(input('Задайте список: '))
# l = []
# for i in range(-n, n + 1):
#     l.append(i)
# print(l)
# random.shuffle(l)
# print(l)