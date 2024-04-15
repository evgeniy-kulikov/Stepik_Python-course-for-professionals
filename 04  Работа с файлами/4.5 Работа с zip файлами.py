# 4.5 Работа с zip файлами
""""""

"""
Чтобы начать работать с zip архивами, потребуется импортировать модуль zipfile,
в частности потребуется создать объект ZipFile

!!!
Объекты ZipFile похожи на файловые объекты, возвращаемые функцией open()
"""
from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    zip_file.printdir()
    """
    File Name                                             Modified             Size
    test/                                          2021-11-27 12:47:10            0
    test/Картинки/                                 2021-11-27 12:49:02            0
    test/Картинки/1.jpg                            2021-09-02 12:30:20        90156
    test/Картинки/avatar.png                       2021-08-20 09:38:44        19053
    test/Картинки/certificate.png                  2021-10-23 09:46:36        43699
    test/Картинки/py.png                           2021-07-28 17:55:56        33522
    test/Картинки/World_Time_Zones_Map.png         2021-11-08 07:30:06      2324421
    test/Картинки/Снимок экрана.png                2021-10-01 20:47:02        10878
    test/Программы/                                2021-11-27 12:48:20            0
    test/Программы/image_util.py                   2021-11-18 12:42:22         4955
    test/Программы/sort.py                         2021-11-14 19:31:02           61
    test/Разные файлы/                             2021-11-27 12:48:10            0
    test/Разные файлы/astros.json                  2021-11-08 09:29:58          505
    """

"""
При создании объекта ZipFile мы также можем передать необязательный аргумент mode, 
который задает режим работы (по аналогии с обычными файлами):

r — файл будет открыт для чтения (по умолчанию)
w — если файл существует, то он будет уничтожен и вместо него будет создан новый файл
a — существующий файл будет открыт в режиме добавления в конец


Метод infolist() позволяет получить информацию о файлах из архива в виде списка специальных объектов (тип ZipInfo), 
которые содержат дополнительную информацию о каждом файле:

метод is_dir() - проверить тип объекта: файл или папка. Возвращает True, если объект является папкой, или False.
"""

from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    info = zip_file.infolist()
    print(info[6].file_size)        # 2324421 - размер начального файла в байтах
    print(info[6].compress_size)    # 2322032 - размер сжатого файла в байтах
    print(info[6].filename)         # test/Картинки/World_Time_Zones_Map.png - имя файла
    print(info[6].date_time)        # дата изменения файла - (2021, 11, 8, 7, 30, 6)
    print(info[0].is_dir())         # True
    print(info[6].is_dir())         # False


"""
Метод namelist() возвращает список названий файлов и директорий, содержащихся в архиве.
"""
from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    info = zip_file.namelist()
    print(*info, sep='\n')
    """
    test/
    test/Картинки/
    test/Картинки/1.jpg
    test/Картинки/avatar.png
    test/Картинки/certificate.png
    test/Картинки/py.png
    test/Картинки/World_Time_Zones_Map.png
    test/Картинки/Снимок экрана.png
    test/Неравенства.djvu
    test/Программы/
    test/Программы/image_util.py
    test/Программы/sort.py
    test/Разные файлы/
    test/Разные файлы/astros.json
    """

"""
метод getinfo() позволяет получить информацию о конкретном файле по его имени в архиве
"""
from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    info = zip_file.namelist()              # получаем названия всех файлов архива
    last_file = zip_file.getinfo(info[-4])  # получаем информацию об отдельном файле
    print(last_file.file_size)              # 4955
    print(last_file.compress_size)          # 1641
    print(last_file.filename)               # test/Программы/image_util.py
    print(last_file.date_time)              # (2021, 11, 18, 12, 42, 22)


""" Работа с конкретными файлами из архива """

from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    with zip_file.open('test/Разные файлы/astros.json') as file:
        print(file.read())
        # b'{"number": 10, "people": [{"craft": "ISS", "name": "Mark Vande Hei"}, ...], "message": "success"}'


"""
Метод file.read() возвращает сырые байты (тип bytes) - символ b перед выводом. 
Для того чтобы преобразовать их в строку (тип str), 
нужно использовать метод decode(), 
указав нужную кодировку (файл astros.json имеет кодировку UTF-8).
"""

from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    with zip_file.open('test/Разные файлы/astros.json') as file:
        print(file.read().decode('utf-8'))
        # {"number": 10, "people": [{"craft": "ISS", "name": "Mark Vande Hei"}, ...], "message": "success"}'


""" Запись в zip архив """
# необходимо создать объект ZipFile в режимах mode='w' (создать и записать)
# или mode='a' (добавить запись)

from zipfile import ZipFile

with ZipFile('archive.zip', mode='w') as zip_file:
    zip_file.write('program.py')
    zip_file.write('lse.jpeg')
    print(zip_file.namelist())
    # ['program.py', 'lse.jpeg']

# Метод write() может принимать еще один строковый аргумент, задающий новое имя файла в архиве.
from zipfile import ZipFile

with ZipFile('archive.zip', mode='w') as zip_file:
    zip_file.write('program.py', 'new_program.py')  # первый аргумент - это имя файла
    zip_file.write('lse.jpeg', 'lse1.jpeg')         # второй аргумент - это имя файла в архиве
    print(zip_file.namelist())
    # ['new_program.py', 'lse1.jpeg']


""" Извлечение содержимого zip-файла в каталог """

"""
Для извлечения данных из архива в каталог используются методы extract() и extractall().

Если требуется извлечь отдельные файлы, то используется метод extract(), 
он принимает два аргумента: название файла и путь, по которому требуется извлечь файл. 
Если путь не указывать, то файл будет извлечен в папку, где находится файл с программой.
"""
# Извлечь указанные файлы
from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    zip_file.extract('test/Картинки/avatar.png')
    zip_file.extract('test/Программы/image_util.py')
    zip_file.extract('lse.jpeg')

# Извлечь все файлы
from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    zip_file.extractall()


"""
Примечание 1. 
При создании объекта ZipFile мы также можем передать еще два необязательных аргумента:

compression, который определяет метод сжатия, который должен использоваться при записи в архив. 
Он принимает одно из значений: ZIP_STORED, ZIP_DEFLATED, ZIP_BZIP2, ZIP_LZMA. 
По умолчанию используется значение compression=ZIP_STORED

allowZip64, который позволяет разрешить использование расширений zip64, 
которые дают возможность создавать архивы размером больше 4 гигабайт. 
По умолчанию равен allowZip64=True


Примечание 2. 
Для того чтобы проверить является ли некоторый файл zip архивом, 
используется функция zipfile.is_zipfile(), которая принимает на вход путь к файлу (или сам файловый объект) 
и возвращает значение True, если указанный файл является zip архивом, или False в противном случае.
"""



"""   *   *   *   Task   *   *   *   """

#  4.5-1
"""
Напишите программу, которая выводит единственное число — количество файлов в этом архиве.
Input:  workbook.zip
"""
from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    res = sum(not el.is_dir() for el in info)
    print(res)  # 18


#  4.5-2
"""
Напишите программу, которая выводит суммарный объем файлов архива в сжатом и не сжатом видах в байтах
Input:  workbook.zip
"""
from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    res1 = sum(el.file_size for el in info)
    res2 = sum(el.compress_size for el in info)

    print(f'Объем исходных файлов: {res1} байт(а)')
    print(f'Объем сжатых файлов: {res2} байт(а)')

# за один проход
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    res1, res2 = 0, 0
    for el in info:
        res1 += el.file_size
        res2 += el.compress_size
    print(f'Объем исходных файлов: {res1} байт(а)')
    print(f'Объем сжатых файлов: {res2} байт(а)')


#  4.5-3
"""
Напишите программу, которая выводит название файла из этого архива, 
который имеет наилучший показатель степени сжатия.
Input:  workbook.zip
Output: *fontlist-v330.json
"""
from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    res = min((el.compress_size / el.file_size, el.filename) for el in info if not el.is_dir())
    print(res[1].split('/')[-1])


#  4.5-4
"""
Напишите программу, которая выводит название файлов из этого архива, 
которые были созданы или изменены позднее 2021-11-30 14:22:00. 
Названия файлов должны быть расположены в лексикографическом порядке, каждое на отдельной строке.
Input:  workbook.zip
Output: *fontlist-v330.json
"""
from zipfile import ZipFile
from datetime import datetime

# dt = datetime.fromisoformat('2021-11-30 14:22:00')
# dt = datetime.strptime('2021-11-30 14:22:00', '%Y-%m-%d %H:%M:%S')
dt = datetime(2021, 11, 30, 14, 22)

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    res = [el.filename.split('/')[-1] for el in info if not el.is_dir() and datetime(*el.date_time) > dt]
    [print(el) for el in sorted(res)]


#  4.5-5
"""
Форматированный вывод
https://stepik.org/lesson/547172/step/18?unit=540798
Input:  workbook.zip
Output: *
"""
from zipfile import ZipFile
from datetime import datetime as dt

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    res = [el for el in info if not el.is_dir()]
    res.sort(key=lambda x: x.filename.split('/')[-1])
    for el in res:
        print(el.filename.split('/')[-1])
        print(f"  Дата модификации файла: {dt(*el.date_time).strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  Объем исходного файла: {el.file_size} байт(а)")
        print(f"  Объем сжатого файла: {el.compress_size} байт(а)\n")


# короче
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    res = sorted([i for i in info if not i.is_dir()], key=lambda x: x.filename.split('/')[-1])
    for el in res:
        print(el.filename.split('/')[-1],
              f"  Дата модификации файла: {dt(*el.date_time)}",
              f"  Объем исходного файла: {el.file_size} байт(а)",
              f"  Объем сжатого файла: {el.compress_size} байт(а)\n", sep='\n')


#  4.5-6
"""
Запись в zip архив
https://stepik.org/lesson/547172/step/19?unit=540798
Создать архив files.zip и добавить в него все файлы из списка file_names.
"""
from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

with ZipFile('files.zip', mode='w') as zip_file:  # можно mode='a'
    for el in file_names:
        zip_file.write(el)


#  4.5-7
"""
Запись в zip архив
https://stepik.org/lesson/547172/step/20?unit=540798
Добавить в архив files.zip только те файлы из списка file_names, 
объем которых не превышает 100 байт
"""
from zipfile import ZipFile, ZipInfo
import os.path

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

with ZipFile('files.zip', mode='w') as zip_file:
    for el in file_names:
        # if os.path.getsize(el) <= 100:
        if ZipInfo.from_file(el).file_size <= 100:
            zip_file.write(el)



#  4.5-7
"""
Функция extract_this()
https://stepik.org/lesson/547172/step/21?unit=540798
Реализуйте функцию extract_this(), которая принимает один или более аргументов в следующем порядке:
zip_name — название zip архива,
*args — переменное количество позиционных аргументов, каждый из которых является названием некоторого файла
Функция должна извлекать файлы *args из архива zip_name в папку с программой. 
Если в функцию не передано ни одного названия файла для извлечения, 
то функция должна извлечь все файлы из архива.
"""
from zipfile import ZipFile

def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if not args:
            zip_file.extractall()
        else:
            for el in args:
                zip_file.extract(el)

#  4.5-8
"""
Функция extract_this()
https://stepik.org/lesson/547172/step/22?unit=540798
Input:  data.zip
"""
from zipfile import ZipFile
import json

def correct_json(el):
    try:
        json.loads(el)
    except json.JSONDecodeError:
        return False
    return True

with ZipFile('data.zip') as zip_file:
    info = zip_file.infolist()
    ls = []
    for el in info:
        if not el.is_dir() and el.filename.endswith('.json'):
            with zip_file.open(el.filename) as json_fl:
                val = json_fl.read().decode('utf-8', errors='ignore')  # 'ignore' - пропуск ошибок декодирования
                if correct_json(val):
                    data_json = json.loads(val)
                    if data_json['team'] == 'Arsenal':
                        ls.append(f"{data_json['first_name']} {data_json['last_name']}")
print(*sorted(ls), sep="\n")


# Без использования проверочной функции
ls = []
with ZipFile('data.zip') as zip_file:
    info = zip_file.infolist()
    for el in info:
        if el.filename.endswith('.json'):
            with zip_file.open(el.filename) as json_fl:
                try:
                    data_json = json.loads(json_fl.read().decode('utf-8'))
                except:
                    continue
            if data_json['team'] == 'Arsenal':
                ls.append(f"{data_json['first_name']} {data_json['last_name']}")
print(*sorted(ls), sep="\n")


#  4.5-10
"""
Структура архива 🌶️🌶️
https://stepik.org/lesson/547172/step/23?unit=540798
Input:  desktop.zip
"""
from zipfile import ZipFile


def convert_bytes(size):
    cnt = 0
    while size // 1024 > 0 and cnt < 3:
        size /= 1024
        cnt += 1
    return f"{round(size)} {['B', 'KB', 'MB', 'GB'][cnt]}"


with ZipFile('desktop.zip') as zip_file:
    info = zip_file.infolist()
    for el in info:
        file_name = el.filename.strip('/').split('/')
        str_name = '  ' * (len(file_name) - 1) + file_name[-1]
        if el.is_dir():
            print(str_name)
        else:
            print(str_name, convert_bytes(el.file_size))
