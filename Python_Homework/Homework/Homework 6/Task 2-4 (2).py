# 4. Английский словарь
# "Пора учить английский язык", - сказал себе Степа и решил написать программу
# для изучения английского языка.
# Программа получает на вход слово на английском языке и несколько его переводов на русском языке.
# Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов.
# В этой задаче нужно использовать строчный метод split().
#
# # Ввод:
# >> 4 # Количество слов
# >> apple - яблоко
# >> orange - оранжевый, рыжий, апельсин
# >> grape - виноград, виноградный, гроздь
# >> easy - простой, легкий, нетрудный, удобный, несложный
# # Вывод:
# >> {'apple': ['яблоко'],
# 'orange': ['оранжевый', 'рыжий', 'апельсин'],
# 'grape': ['виноград', 'виноградный', 'гроздь'],
# 'easy': ['простой', 'легкий', 'нетрудный', 'удобный', 'несложный']}

count = int(input('Количество слов для перевода: '))
translate_dict = {}
for _ in range(count):
    eng_rus_str = input()
    some_list = eng_rus_str.split(' - ')
    translate_dict[some_list[0]] = some_list[1].split(', ')
print(translate_dict)
eng_word = input('Введите слово для перевода: ')
if translate_dict.get(eng_word): # Ели слово есть, тогда
    print(', '.join(translate_dict.get(eng_word)))
else: # Если ложь, тогда
    print('Такого слова нет')