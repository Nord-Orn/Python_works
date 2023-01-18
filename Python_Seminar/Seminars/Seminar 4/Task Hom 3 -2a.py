# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.
# Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

some_list = input().split()
new_list = []
if len(some_list) % 2 == 0:
    middle = len(some_list) // 2
else:
    middle = len(some_list) // 2 + 1
for start in range(0, middle):
    new_list.append(int(some_list[start]) * int(some_list[len(some_list) - start - 1]))
print(new_list)