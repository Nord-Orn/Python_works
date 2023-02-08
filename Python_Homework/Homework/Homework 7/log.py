import datetime


def write(data):
    with open('cash.csv', 'a', encoding='utf-8') as l:
        l.write(f'{data}. Время запроса: {datetime.datetime.now()}' + '\n')



def making(data):
    with open('cash.csv', 'a', encoding='utf-8') as l:
        l.write(f'{data}. Время внесения данных: {datetime.datetime.now()}' + '\n')
