# Вводится строка. Требуется, используя введенную строку,
# сформировать N=10 пар кортежей в формате:
# (символ, порядковый индекс)
# Первый индекс имеет значение 0. Строка может быть короче 10 символов, а может быть и длиннее.
# То есть, число пар может быть 10 и менее.
# Используя функцию zip сформируйте указанные кортежи и сохраните в список с именем lst.

s = input('Введите строку: ')
lst = list(zip(range(10), s)) # zip будет отрезать все что > rang(10)
print(lst)