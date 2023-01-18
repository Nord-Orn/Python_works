# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input())
out_list = []
while n > 0:
    out_list.append(str(n % 2))
    n //= 2
out_list.reverse()
print(*out_list, sep='')