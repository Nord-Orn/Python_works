# Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел,
# делящихся на 9. При решении задачи используйте комбинацию функций filter, map, sum.
# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.

lst = [i for i in range(10, 100)]
print(lst)
one = list(filter(lambda x: x % 9 == 0, lst))
print(one)
sek = sum(list(map(lambda x: x**2, lst)))
print(f'sum: {sek}')