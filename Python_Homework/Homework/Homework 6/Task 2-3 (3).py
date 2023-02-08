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

# Создание словаря согласно условию
num = int(input('Количество друзей: '))
dict_list = []
for _ in range(num):
    name = input('Имя?: ')
    age = int(input('Возраст?: '))
    dict_list.append({'name': name, 'age': age})
print(dict_list)

# Поиск самого длинного имени и среднего возраста
summa = 0
max_mame = dict_list[0]['name']
for i in dict_list:
    summa += i['age']
    if len(i['name']) > len(max_mame):
        max_mame = i['name']
print(summa // num)
print(max_mame)

# Пример как быстро достать все имена из списка и все возраста в отдельные словари
name_list = [i['name'] for i in dict_list]
print(name_list)
age_list = [i['age'] for i in dict_list]
print(age_list)
print(sum(age_list) // num) # Поиск среднего возраста

# Создание большого словаря
# big_dict = {}
# for el in dict_list:
#     big_dict.update(el)
# print(big_dict) # Одинаковых ключей не может быть в одном словаре (выдаст последний ввод ключа)

# Сбор всех имен под одним ключом и возрастов под другим ключом
big_dict = {'name': [], 'age': []}
for el in dict_list:
    big_dict['name'].append(el['name'])
    big_dict['age'].append(el['age'])
print(big_dict)
print(big_dict.values())
