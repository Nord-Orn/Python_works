# Задача3.	Ввести цифру N, вывести на печать все цифры от  -N до N
   
# a) вариант решения
diapazon = int(input('Введите цифру N для вывода чисел в диапазоне от -N до N: '))
for i in range(-diapazon, diapazon +1):
    print(i, end=', ',)
print()
# b) более короткий вариант решения

diapazon = int(input('Введите цифру N для вывода чисел в диапазоне от -N до N: '))
print(*range(-diapazon, diapazon + 1), sep='; ') # sep = '; ' разделитель списка, * -распаковка списка