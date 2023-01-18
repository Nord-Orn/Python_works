with open('res.txt', 'w', encoding='utf-8') as file:
    for i in range(1, 101):
        file.write(str(i) + '\n')
    # str(i) - в тхт файл можно записывать только строки
    # + '\n' позволяет переносить данные на новую сроку