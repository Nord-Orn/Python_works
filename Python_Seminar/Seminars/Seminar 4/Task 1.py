# Задайте строку из набора чисел. Напишите программу которая покажет большее и меньшее число.
# В качестве символа разделителя используйте пробел.

with open('input_task1.txt', 'r', encoding='utf-8') as file:
    line = file.readline().split() # .split() учитывает пробелы между жанными
    print(line)
    maxx = int(line[0])
    minn = int(line[0])
    for el in line:
        if int(el) > maxx:
            maxx = int(el)
        elif int(el) < minn:
            minn = int(el)
    print(minn, maxx)