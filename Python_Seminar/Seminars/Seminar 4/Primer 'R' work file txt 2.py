with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read() # .read() необходимо для считывания и занос данных в переменную
    for sym in text:
        print(sym.strip())
# Вывели элементы построчно, с помощью strip() убрали лишние межстрочные переносы