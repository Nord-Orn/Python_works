# Найдите корни квадратного уравнения Ax2+Bx+C=0 двумя способами:
# 1) С помощью математических формул нахождения корней квадратного уравнения
# 2) С помощью дополнительных библиотек Python

with open('input_task2.txt', 'r', encoding='utf-8') as file:
    line = file.readline().split() # .split() учитывает пробелы между жанными
    print(line)
    a, b, c = int(line[0]), int(line[1]), int(line[2])
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('Корней нет')
    elif d == 0:
        print(-b / 2 * a)
    else:
        print((-b + d ** 0.5) / 2 * a)
        print((-b - d ** 0.5) / 2 * a)
