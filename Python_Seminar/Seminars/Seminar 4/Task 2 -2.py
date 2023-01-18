# Найдите корни квадратного уравнения Ax2+Bx+C=0 двумя способами:
# 1) С помощью математических формул нахождения корней квадратного уравнения
# 2) С помощью дополнительных библиотек Python

with open('input_task2.txt', 'r', encoding='utf-8') as file:
    line = file.readline().split() # .split() учитывает пробелы между жанными
    print(line)
    a, b, c = int(line[0]), int(line[1]), int(line[2])
    import sympy
    x = sympy.Symbol('x')
    print(sympy.solve(f'{a}* x ** 2 + {b} * x + {c}'))

# """terminal -> pip install sympy""" сначала скачивается через терминал sympy, потом решается