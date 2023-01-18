# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

d = int(input('введите число: '))
list = []
for i in range(2, d + 1):
    if d % i == 0:
        count = 1
        for j in range(2, i):
            if(i % j == 0):
                count = 0
        if(count == 1): list.append(i)
print(list)