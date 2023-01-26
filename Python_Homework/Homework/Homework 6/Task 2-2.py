# 2. Старший и младший
# Пользователь вводит число N.
# Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Найдите самого младшего из друзей и выведите его имя.
# Ввод:
# >> 3 # Количество друзей
# >> Иван
# >> 11
# >> Саша
# >> 12
# >> Леша
# >> 10
# Вывод: Леша

num = int(input('Количество друзей: '))
count = 0
age = []
name = []
min = 150
while count < num:
    n = input('Имя: ')
    name.append(n)
    a = int(input('Возраст: '))
    if a < min: min = a
    age.append(a)
    count += 1
dictionary = dict(zip(name, age))
print(dictionary)
for i in dictionary:
    if dictionary[i] == min: print(i)