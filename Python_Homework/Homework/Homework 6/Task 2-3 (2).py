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
dict_list = []
for _ in range(num):
    name = input('Имя?: ')
    age = int(input('Возраст?: '))
    dict_list.append({'name': name, 'age': age})
print(dict_list)
summa = 0
max_mame = dict_list[0]['name']
for i in dict_list:
    summa += i['age']
    if len(i['name']) > len(max_mame):
        max_mame = i['name']
print(summa // num)
print(max_mame)