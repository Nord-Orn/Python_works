# Задача 1. 
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
#   Пример:
#   - 6 -> да
#   - 7 -> да
#   - 1 ->  нет

day = int(input("Введите день недели от 1 до 7: "))
while day < 1 or day > 7:
    day = int(input("Введите день недели от 1 до 7: "))
if 0 < day < 6: print('Рабочий день')
else: print('Выходной день')