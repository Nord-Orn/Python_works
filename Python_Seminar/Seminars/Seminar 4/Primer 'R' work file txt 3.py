with open('input.txt', 'r', encoding='utf-8') as file:
    while True:
        line = file.readline() # Считывание данных по строчкам
        if not line:
            break    # Если данных строки нет значит прервать работу
        print(line.strip())
# Для работы с большими данными вывод данных построчно, а не всех сразу