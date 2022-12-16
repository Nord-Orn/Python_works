# Задача 2
# Напишите программу которая принимает на вход 5 чисел и находит наибольшее из них.
#    a)	Вариант выполнения со списком в два цикла

from random import randint

number = int(input('Ввудите колличество цифр необходимое для сравнения: '))
diapazon = int(input('Ввудите цифру N для поиска случайных чисел в диапазоне от -N до N: '))
main_list = []
for _ in range(number + 1):
    x = randint(-diapazon, diapazon)
    x = main_list.append(x)
print(main_list)
maxx = -diapazon
for i in main_list:
    if i > maxx: maxx = i
print('MAX= ', maxx)


     # d) второй вариант выпонения со списком в один цикл.

number = int(input('Ввудите колличество цифр необходимое для сравнения: '))
diapazon = int(input('Ввудите цифру N для поиска случайных чисел в диапазоне от -N до N: '))
main_list = []
maxx = -diapazon
for _ in range(number + 1):
    x = randint(-diapazon, diapazon)
    if x > maxx: maxx = x
    x = main_list.append(x)    
print(main_list, 'MAX= ', maxx) 

     # c) вариант без использования списка 
     
number = int(input('Ввудите колличество цифр необходимое для сравнения: '))
diapazon = int(input('Ввудите цифру N для поиска случайных чисел в диапазоне от -N до N: '))
maxx = -diapazon 
for _ in range(number + 1):
    x = randint(-diapazon, diapazon)
    if x > maxx: maxx = x
    print(x, end = '/ ') # end = '/ ' записывает в строку, а не в столбец. Разделяет '/' вставленным указателем
print('MAX= ', maxx)
 


