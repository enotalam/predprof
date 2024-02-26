""" Решение 2 задания предпроф экзамена.
Программа читает файл данных, сортирует его по датам.
Она выводит первых 5х победителей, которые выпустили песни раньше всех.(не работает)
 """
from csv import reader, writer

with open('songs.csv', encoding='utf-8') as data_file:
    song = list(reader(data_file, delimiter=';'))
    head_line = song.pop(0)

for i in range(2, len(song)):
    # Сортируем список по годам
    if (int((song[i][-1].split('.'))[-1]) > int((song[i-1][-1].split('.'))[-1]) )or \
    (int((song[i][-1].split('.'))[1]) > int((song[i-1][-1].split('.'))[1])) or \
    (int((song[i][-1].split('.'))[0]) > int((song[i-1][-1].split('.'))[0])) :
        pos = i
        while pos != 1 and  (int((song[i][-1].split('.'))[-1]) > int((song[i-1][-1].split('.'))[-1]) )or \
    (int((song[i][-1].split('.'))[1]) > int((song[i-1][-1].split('.'))[1])) or \
    (int((song[i][-1].split('.'))[0]) > int((song[i-1][-1].split('.'))[0])) :
            # Обмен соседних элементов списка
            element = song[pos]
            song[pos] = song[pos - 1]
            song[pos- 1] = element
            pos-= 1

print(song)

print("топ 5:")
for i in range(5):
    # Находим номер, название песни, артиста и дату выхода
    streams = song[i][0]
    track_name = song[i][2]
    artist_name = song[i][1]
    data = song[i][-1]
    print(f"{str(i + 1)} место: {streams}. {track_name}, {artist_name}, {data}")