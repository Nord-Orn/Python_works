# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов
# списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

n = int(input('Введите длину списка'))
mlist = []
summ = 0
for i in range(n):
    r = randint(1, 10)
    mlist.append(r)
    if i % 2 != 0: summ += r
print(mlist, 'Сумма нечётных позиций= ', summ)