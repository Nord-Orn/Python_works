# Реализуйте алгоритм перемешивания списка.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( "Исходный список: ", lista)
listb = []
for a in range(len(lista)):
    r = randint(1, 10)
    while r in listb: r = randint(1, 10)
    else: listb.append(r)
print('Полученный список: ', listb)
