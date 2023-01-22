# Создайте список из случайных чисел. Найдите количество различных элементов в нем.

from random import randint
my_list = [randint(1, 26) for i in range(int(input('Введите количество чисел: ')))]
print(my_list)
my_list = set(my_list)
print(my_list)
count = int(sum(map(lambda i: i / i, my_list)))
print(count)