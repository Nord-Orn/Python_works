# from random import randint
# def random(x):
n = int(input("Задайте натуральное число N \n N = "))
l = []
for i in range(2, n + 1):
    if n % i == 0:
        count = 1
        for j in range(2,(i//2+1)):
            if i % j == 0:
                print(i, j, (i//2 / j), (i//2 % j))
                count = 0
                #break
        if count == 1:
            l.append(i)
print("Список простых множителей: ", l)