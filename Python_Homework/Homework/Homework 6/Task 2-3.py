# 3. Еще немного о друзьях
# Пользователь вводит число N.
# Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Выведите средний возраст всех друзей и самое длинное имя.
# Ввод:
# >> 3 # Количество друзей
# >> Иван
# >> 12
# >> Иннокентий
# >> 20
# >> Леша
# >> 10
# Вывод:
# >> 14
# >> Иннокентий
num = int(input('Количество друзей: '))
count, sm, max  = 0, 0, 0
age = []
name = []
while count < num:
    n = input('Имя: ')
    name.append(n)
    a = int(input('Возраст: '))
    age.append(a)
    count += 1
dictionary = dict(zip(name, age))
print(dictionary)
for i in dictionary:
    for j in i:
        if max < len(i): max = len(i); name2 = i
    sm += dictionary[i]
print('Средний возраст друзей: ', int(sm / count), '//   Самое длинное имя: ', name2)