with open('input.txt', 'r', encoding='utf-8') as file:
    line_list = file.read().splitlines() # .splitlines() вносит данные в переменную строками в виде списка
    print(line_list)
