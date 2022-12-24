# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

mlist=[1.1, 1.2, 3.1, 5, 10.01]
max, min = 0.001, 0.99
for i in range(len(mlist)):
    numm = mlist[i] -  mlist[i]//1
    if numm > max: max = numm
    elif numm < min: min = numm
rez = max - min
print(mlist,'=>', rez)
