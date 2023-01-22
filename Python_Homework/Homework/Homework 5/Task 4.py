# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def compression(x):
    bukvi = []
    chislo = []
    for i in x:
        if i not in bukvi:
            bukvi.append(i)
    for j in bukvi:
        count = 0
        for i in x:
            if j == i:
                count += 1
        chislo.append(str(count))
    rez = list(zip(chislo, bukvi))
    return rez

def recovery(x):
    num = [int(i) for i in x if i.isdigit()]
    text = [i for i in x if not i.isdigit()]
    rez = list(zip(num, text))
    return rez


n = int(input('Введите 1 для сжатия данных или 2 для восстановления: '))
if n == 1:
    with open('Baza_Task4.txt', 'r', encoding='utf-8') as file:
        line_list = list(file.read())
    with open('Rez_Task4.txt', 'w', encoding='utf-8') as file:
        for i, j in compression(line_list):
            file.write(i)
            file.write(j)
if n == 2:
    with open('Rez_Task4.txt', 'r', encoding='utf-8') as file:
        my_list = list(file.read())
    with open('Rez2_Task4.txt', 'w', encoding='utf-8') as file:
        for i, j in recovery(my_list):
            k = i * j
            file.write(k)