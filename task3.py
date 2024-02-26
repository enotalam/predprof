"""
Решение задачи 3 предпрофессионального экзамена.
Программа читает данные из csv-файла, выполняет поиск песни введенного артиста.
"""
from csv import reader, writer

with open('songs.csv', encoding='utf-8') as data_file:
    song = list(reader(data_file, delimiter=';'))
    head_lines = song.pop(0)

artist_name = input('Введите имя арстиста: ')

while artist_name != '0':
    position = 1
    for name in song:
        if name[1] == artist_name:
            track_name = name[2]
            position = 0
    if position == 0:
        print(f'У {artist_name} найдена песня: {track_name}')
    if position == 1:
        print('К сожалению, ничего не удалось найти')
    artist_name = input('Введите имя арстиста: ')