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
dict_list = []
for _ in range(num):
    name = input('Имя?: ')
    age = int(input('Возраст?: '))
    dict_list.append({'name': name, 'age': age})
print(dict_list)
min_age = dict_list[0]['age']
for some_dict in dict_list:
    if some_dict['age'] < min_age:
        min_age = some_dict['age']
for some_dict in dict_list:
    if some_dict['age'] == min_age:
        print(some_dict['name'])
        break