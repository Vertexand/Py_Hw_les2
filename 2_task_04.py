# 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов,
#  заполненный числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях (не индексах)
# position one: 1
# position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> [15]

n = int(input('Number of elements:  '))
pos_1 = int(input('position one: '))
pos_2 = int(input('position two: '))
l = []
for i in range(-n, n + 1):
    l.append(i)
print(l, l[pos_1 - 1] * l[pos_2 - 1])


#sssssssssssssssssssssssssssssssssssssssss
# num = int(input("Enter the value of N: "))#  др. реш
# n_1 = int(input("Position one: "))
# n_2 = int(input("Position two: "))

# nums_list = list(range(-num, num + 1))

# print(nums_list)
# len_list = len(nums_list)

# if len_list >= n_1 > 0 and len_list >= n_2 > 0:
#     print(nums_list[n_1 - 1] * nums_list[n_2 - 1])
# else:
#     print("There are no values for these indexes!")


