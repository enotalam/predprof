"""
Решение задачи 4 предпрофессионального экзамена.
Программа читает данные из csv-файла, анализирут какие артисты русские,
а какие ионстранные и выводит их количество.
"""
from csv import reader, writer

song01 = list()

with open('songs.csv', encoding='utf-8') as data_file:
    # Преобразовать reader к списку
    song = list(reader(data_file, delimiter=';'))
    # Строка с подписями столбцов
    head_line = song.pop(0)

russian_letters = 'йцукенгшщзхъфывапролджэячсмитьбюёЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
russian_artists = list()
foreign_artists = list()
for i in song:
    count_rus_letters = 0
    name = i[1].replace(' ','')
    for j in range(len(name)):
        if name[j] in russian_letters:
            russian_artists.append(i[1])
            count_rus_letters += 1
            break
    if count_rus_letters == 0:
        foreign_artists.append(i[1])

print(f'Количество российских исполнителей: {len(russian_artists)}')
print(f'Количество иностранных исполнителей: {len(foreign_artists)}')

with open('russian_artists.txt', 'w', encoding='utf-8') as data_file:
    russian_writer = writer(data_file)
    for i in russian_artists:
        russian_writer.writerow(i)

with open('foreign_artists.txt', 'w', encoding='utf-8') as data_file:
    foreign_writer = writer(data_file)
    for i in foreign_artists:
        foreign_writer.writerow(i)