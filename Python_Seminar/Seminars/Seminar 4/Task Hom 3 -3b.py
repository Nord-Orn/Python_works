# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

some_list = input().split()
maxx = 0
minn = 1
for el in some_list:
    if float(el) % 1 != 0:
        if float(el) % 1 < minn:
            minn = float(el) % 1
        if float(el) % 1 > maxx:
            maxx = float(el) % 1
print(round(maxx - minn, 2))
