# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.
# Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

from random import randint
n=int(input('Введите длину списка: '))
mlist=[]
slist =[]
for i in range(n):
    r = randint(1, 6)
    mlist.append(r)
count, pr = 0,0
if len(mlist) % 2 == 0:
    for j in range(len(mlist) // 2):
        pr = mlist[j] * mlist[-j-1]
        slist.append(pr)
else:
    for j in range((len(mlist) // 2)+1):
        pr = mlist[j] * mlist[-j-1]
        slist.append(pr)
print(mlist, slist)