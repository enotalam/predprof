"""
Решение задачи 1 предпрофессионального экзамена.
Программа читает данные из csv-файла, ищет все песни по дате выхода не позже 01.01.2002.
Затем подсчитывает по формуле количество просмотрв, заменяет им результаты 0
и сохраняет в новый файл.
"""

from csv import reader, writer

song01 = list()

with open('songs.csv', encoding='utf-8') as data_file:
    # Преобразовать reader к списку
    song = list(reader(data_file, delimiter=';'))
    # Строка с подписями столбцов
    head_line = song.pop(0)

for i in song:
    b = []
    data = i[-1].split('.')
    day = int(data[0])
    month = int(data[1])
    year = int(data[-1])
    if i[0] == '0':
        day1 = 12
        month1 = 5
        year1 = 23
        razniza_dat = (day1-day) + (month1 - month)*30 + (year1 - year)*365
        i[0] = str(abs((razniza_dat) / (len(i[1].replace(' ','')) + len(i[2].replace(' ','')))))
    if day >= 1 and month >= 1 and year >= 2002:
        b.append(i[2])
        b.append(i[1])
        b.append(i[0])
        song01.append(b)

new_head_line = []
new_head_line.append('track_name')
new_head_line.append('artist_name')
new_head_line.append('streams')

with open('songs_new.csv', 'w', encoding='utf-8') as data_file:
    data_writer = writer(data_file,delimiter=',')
    data_writer.writerow(new_head_line)
    data_writer.writerows(song01)