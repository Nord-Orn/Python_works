# Напишите программу которая принимает на вход два числа и проверяет является ли одно число квадратом другого

number = int(input('Введите число А= '))
number2 = int(input('Введите число B= '))
if number ** 2 == number2 or number2 ** 2 == number: print('Yes')
else: print('No')