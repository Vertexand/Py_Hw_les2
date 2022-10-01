# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример: - Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

num = int(input('введите число: '))#вар с округ до 2 знаков
sum_nums = 0
list_nums = []

for i in range(1, num + 1):
    result = round((1 + 1 / i) ** i, 3)
    list_nums.append(result)
    sum_nums += result

print(list_nums)
print(sum_nums)

# n = int(input("введите число: "))  #вар 2 
# V = {n: round((1+(1/n))**n) for n in range(1, n+1)}
# print(V)
# print(sum(V.values()))

# print(i, end=" ")

# n = int(input('Задайте n: '))# вар 3
# l = {}
# total = 0
# for i in range(1, n + 1):
#     l[i] = int(round((1 + 1 / i) ** i, 0))
#     total += l[i]
# print(l, total)





