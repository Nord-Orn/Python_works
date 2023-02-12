# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('Baza_Task1.txt', 'r', encoding='utf-8') as file:
    line_list = file.read().split()
    print(line_list)
# rez_list = [i for i in line_list if 'а' or 'А' or 'б' or 'Б' or 'в' or 'В' not in i] не работает
simbol = ['а', 'А', 'б', 'Б', 'в', 'В']
rez_list = [i for i in line_list if all(el not in i for el in simbol)]
print(rez_list)
with open('Rez_Task1.txt', 'w', encoding='utf-8') as file:
   for i in rez_list:
       file.write(i + ' ')