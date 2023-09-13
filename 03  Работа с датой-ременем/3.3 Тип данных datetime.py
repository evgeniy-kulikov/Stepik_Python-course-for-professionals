# 3.3 Тип данных datetime
""""""

""" *  *  *  *  *  *  *  *  *   """
""" Тип данных datetime """

"""
Типы данных date и time позволяют работать по отдельности с датами и временами. 
Однако на практике чаще требуется работать одновременно и с датой, и со временем. 
Для таких целей используется тип данных datetime из одноименного модуля datetime.

При создании новой даты-времени (тип datetime) нужно указать 
год, месяц, день, часы, минуты, секунды и микросекунды. 
При этом год, месяц и день являются обязательными, 
а часы, минуты, секунды и микросекунды необязательными.
"""
from datetime import datetime

my_datetime = datetime(1992, 10, 6, 9, 40, 23, 51204)    # создаем полную дату-время
only_date = datetime(2021, 12, 31)                       # создаем дату-время с нулевой временной информацией

print(my_datetime)  # 1992-10-06 09:40:23.051204
print(only_date)  # 2021-12-31 00:00:00
print(type(my_datetime))  # <class 'datetime.datetime'>

"""
Атрибуты datetime:
year — год
month — месяц
day — день
hour — час
minute — минуты
second — секунды
microsecond — микросекунды
"""
from datetime import datetime

my_datetime = datetime(1992, 10, 6, 9, 40, 23, 51204)

print('Год =', my_datetime.year)  # Год = 1992
print('Месяц =', my_datetime.month)  # Месяц = 10
print('День =', my_datetime.day)  # День = 6
print('Часы =', my_datetime.hour)  # Часы = 9
print('Минуты =', my_datetime.minute)  # Минуты = 40
print('Секунды =', my_datetime.second)  # Секунды = 23
print('Микросекунды =', my_datetime.microsecond)  # Микросекунды = 51204


""" *  *  *  *  *  *  *  *  *   """
""" Методы combine(), date(), time() """
"""
Сформировать новый объект типа datetime можно с помощью двух разных объектов, 
представляющих дату и время (date и time). Для этого используется метод combine().
"""
from datetime import date, time, datetime

my_date = date(1992, 10, 6)
my_time = time(10, 45, 17)
my_datetime = datetime.combine(my_date, my_time)

print(my_datetime)  # 1992-10-06 10:45:17

# Если, нужно получить из даты-времени (тип datetime) по отдельности дату (тип date) и время (тип time),
# то используются методы date() и time() соответственно.
from datetime import datetime

my_datetime = datetime(2022, 10, 7, 14, 15, 45)
my_date = my_datetime.date()                     # получаем только дату (тип date)
my_time = my_datetime.time()                     # получаем только время (тип time)

print(my_datetime, type(my_datetime))  # 2022-10-07 14:15:45 <class 'datetime.datetime'>
print(my_date, type(my_date))  # 2022-10-07 <class 'datetime.date'>
print(my_time, type(my_time))  # 14:15:45 <class 'datetime.time'>


""" *  *  *  *  *  *  *  *  *   """
""" Методы now(), utcnow(), today() """
"""
Для того, что получить текущее время на момент исполнения программы,
используются методы now() и utcnow() для локального и UTC времени соответственно.
Всемирное координированное время (Coordinated Universal Time, UTC) — стандарт, 
по которому общество регулирует часы и время. Московское время соответствует UTC+3.

Метод today() аналогичен методу now(). 
Для получения локальной даты-времени рекомендуется использовать именно метод now().
"""
from datetime import datetime

datetime_now = datetime.now()
datetime_utcnow = datetime.utcnow()

print(datetime_now)     # 2021-08-13 08:03:43.224568 -текущее локальное время (московское) на момент запуска программы
print(datetime_utcnow)  # 2021-08-13 08:03:43.224568 -текущее UTC время на момент запуска программы


""" *  *  *  *  *  *  *  *  *   """
""" Метод timestamp() """
"""
Метод timestamp() позволяет преобразовать объект типа datetime в количество секунд, 
прошедших с момента начала эпохи. Данный метод возвращает значение типа float.
Начало эпохи  —  это полночь 1 января 1970 года (00:00:00 UTC).
"""
from datetime import datetime

my_datetime = datetime(2021, 10, 13, 8, 10, 23)
print(my_datetime.timestamp())  # 1634101823.0


""" *  *  *  *  *  *  *  *  *   """
""" Метод fromtimestamp() """
#  Метод fromtimestamp() позволяет преобразовать количество секунд,
#  прошедших с момента начала эпохи, в объект типа datetime.
#  Данный метод является обратным по отношению к методу timestamp().
from datetime import datetime

my_datetime = datetime.fromtimestamp(1634101823.0)
print(my_datetime)  #2021-10-13 08:10:23


""" *  *  *  *  *  *  *  *  *   """
""" Форматирование даты-времени """
"""
По умолчанию объекты типа datetime (как и объекты типа date и time) выводятся в специальном формате, 
который называется ISO 8601. Данное представление не всегда удовлетворяет нашим запросам.
Чтобы преобразовать дату-время в строку нужного формата, следует воспользоваться методом strftime(), 
указав ему в качестве аргумента параметры форматирования.
"""
from datetime import datetime

my_datetime = datetime(2021, 8, 10, 18, 20, 34)

print(my_datetime)   # 2021-08-10 18:20:34  - вывод в ISO формате
print(my_datetime.strftime('%d.%m.%y --- %H::%M::%S'))    # 10.08.21 --- 18::20::34
print(my_datetime.strftime('%d/%m/%y'))       # 10.08.21 --- 18::20::34
print(my_datetime.strftime('%A %d, %B %Y'))   # Tuesday 10, August 2021
print(my_datetime.strftime('%H:%M:%S'))       # 18:20:34


""" Преобразование строки в дату-время """
#  преобразовать данные из строки в объект типа datetime можно с помощью метода strptime()
from datetime import datetime

datetime_str = input('Введите дату/время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС')  # 06.12.2023 15:09:45
my_datetime = datetime.strptime(datetime_str, '%d.%m.%Y %H:%M:%S')
print(my_datetime)  # 2023-12-06 15:09:45


from datetime import datetime

datetime0 = datetime.strptime('10.08.2034 13:55:59', '%d.%m.%Y %H:%M:%S')  # --> 2034-08-10 13:55:59
datetime1 = datetime.strptime('10/08/21', '%d/%m/%y')  # --> 2021-08-10 00:00:00
datetime2 = datetime.strptime('Tuesday 10, August 2021', '%A %d, %B %Y')  # --> 2021-08-10 00:00:00
datetime3 = datetime.strptime('18.20.34', '%H.%M.%S')  # --> 1900-01-01 18:20:34
datetime4 = datetime.strptime('2021/08/10', '%Y/%m/%d')  # --> 2021-08-10 00:00:00
datetime5 = datetime.strptime('10.08.2021 (Tuesday, August)', '%d.%m.%Y (%A, %B)')  # --> 2021-08-10 00:00:00
datetime6 = datetime.strptime('Year: 2021, Month: 08, Day: 10, Hour: 18.', 'Year: %Y, Month: %m, Day: %d, Hour: %H.')
# --> 22021-08-10 18:00:00


""""""
"""   *   *   *   Task   *   *   *   """
""""""


#  3.3-01
"""
В переменной dt должен содержался объект типа datetime с датой и временем, которые указаны в строке text.
Дата, указанная в строке text, записана в формате DD.MM.YYYY, а время — в формате HH:MM
"""
from datetime import datetime

text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')
print(dt)  # 2022-07-15 08:30:00


#  3.3-02
"""
Преобразовать секунды seconds (прошедшие от начала эпохи) в объект datetime и, наоборот, 
объект datetime в секунды (прошедшие от начала эпохи).
"""
from datetime import datetime

seconds = 2483228800
dt = datetime(2011, 11, 4)
print(datetime.fromtimestamp(seconds))  # 2033-05-18 06:33:20
print(dt.timestamp())  # 1320354000.0


#  3.3-03
"""
Используя список times_of_purchases, содержащий даты (тип datetime), 
в которые были совершены покупки в некотором интернет-магазине. 
Вывести текст:
До полудня - если большее число покупок было совершено до полудня, 
После полудня - в противном случае.
Примечание 1. Гарантируется, что ни одна покупка не была совершена ровно в 12:00:00.
Примечание 2. Гарантируется, что до полудня и после полудня совершено различное количество покупок.
Output: После полудня
"""
from datetime import datetime

times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
                      datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
                      datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
                      datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
                      datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
                      datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
                      datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
                      datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
                      datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
                      datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
                      datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
                      datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
                      datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
                      datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]

before, after = 0, 0
for el in times_of_purchases:
    if el.hour > 11:
        after += 1
    else:
        before += 1
# print(before, after)  # 8 20
print(('До полудня', 'После полудня')[after > before])

# Вариант
am = 0
for el in times_of_purchases:
    if el.strftime('%p') == 'AM':
        am += 1
print(('После полудня', 'До полудня')[am > len(times_of_purchases)])


#  3.3-04
"""
Доступны: список dates, содержащий даты, и список times, содержащий времена. 
Количество элементов в этих списках одинаковое. 
Вывести datetime объекты, полученные путем объединения элементов списков dates и times, 
находящихся на одинаковых позициях. 
Полученные объекты должны быть расположены в порядке возрастания секунд, каждый на отдельной строке.
Input:  dates = [date(2020, 11, 12), date(2021, 7, 2), date(2020, 9, 25)]
        times = [time(12, 50, 22), time(12, 19, 1), time(7, 30, 1)]
Output: 2021-07-02 12:19:01
        2020-09-25 07:30:01
        2020-11-12 12:50:22
"""
from datetime import date, time, datetime

dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
         date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
         date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]

times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
         time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
         time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]


ls = [datetime.combine(d, t) for d, t in zip(dates, times)]
ls.sort(key=lambda el: el.second)
[print(el) for el in ls]


#  3.3-05
"""
Словарь data содержит результаты учеников. 
Ключом в словаре является имя ученика, а значением — кортеж, 
первый элемент которого — время начала решения, второй элемент — время окончания решения. 
Вывести имя ученика, который затратил на решение домашнего задания меньше всего времени.

Примечание 1. Гарантируется, что искомый ученик единственный.
Примечание 2. Дата-времена в кортежах представлены в виде строк в формате DD.MM.YYYY HH:MM:SS.
"""
# from datetime import date, time, datetime
from datetime import datetime

data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

d_min = dict()
for el in data:
    d_min[el] = datetime.strptime(data[el][1], '%d.%m.%Y %H:%M:%S').timestamp() - \
               datetime.strptime(data[el][0], '%d.%m.%Y %H:%M:%S').timestamp()

# получаем ключ словаря по его значению
val_min = min(d_min.values())
res = list(filter(lambda key: d_min[key] == val_min, d_min))
print(*res)  # Егор

# Вариант печати ключа с минимальным значением
print(min(d_min, key=d_min.get))  # применение ключа key в функции min()
# Егор


#  3.3-06
"""
Дневник космонавта
https://stepik.org/lesson/611754/step/18?unit=607091

"""
# from datetime import date, time, datetime
from datetime import datetime

with open('diary.txt', 'r', encoding='utf-8') as file_txt:
    ls = file_txt.read().split('\n\n')

# Формируем словарь. Ключ - timestamp() от даты. Значение - list() абзац (дата + текст + перенос)
d = dict()
for el in ls:
     data_key = datetime.strptime(el[:el.find('\n')], '%d.%m.%Y; %H:%M').timestamp()  # 1206288960.0
     d.setdefault(data_key, el + '\n')

# Сортируем словарь по ключу - timestamp()
res = sorted(d.items())

for el in res:
    print(el[1])


# Короче (без словаря)
with open('diary.txt', 'r', encoding='utf-8') as file_txt:
    ls = file_txt.read().split('\n\n')
res = sorted(ls, key=lambda el: datetime.strptime(el[:el.find('\n')], '%d.%m.%Y; %H:%M'))
print(*res, sep='\n\n')


#  3.3-07
"""
Функция is_available_date() 
https://stepik.org/lesson/611754/step/19?unit=607091
Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:

booked_dates — список строковых дат, недоступных для бронирования. 
Элементом списка является либо одиночная дата, либо период (две даты через дефис). Например:
['04.11.2021', '05.11.2021-09.11.2021']
date_for_booking — одиночная строковая дата или период (две даты через дефис), 
на которую гость желает забронировать номер. Например:
'01.11.2021' или '01.11.2021-04.11.2021'
Функция is_available_date() должна возвращать True, 
если дата или период date_for_booking полностью доступна для бронирования. 
В противном случае функция должна возвращать False.

Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.
Примечание 2. В периоде (две даты через дефис) граничные даты включены.

Input:  dates = ['04.11.2021', '05.11.2021-09.11.2021']
        some_date = '01.11.2021'
        print(is_available_date(dates, some_date))
Output: True
"""
from datetime import datetime

def get_data_set(lst: list) -> set:
    """ Преобразование строкового списка в множество значений номеров дат """
    dates_ls = []
    for el in lst:
        el = el.split('-')
        if len(el) == 2:
            data_range = range(datetime.strptime(el[0], '%d.%m.%Y').toordinal(),
                            datetime.strptime(el[1], '%d.%m.%Y').toordinal() + 1)
            dates_ls += [i for i in data_range]
        else:
            dates_ls += [datetime.strptime(el[0], '%d.%m.%Y').toordinal()]
    return set(dates_ls)


def is_available_date(booking, guest) -> bool:
    """ Проверка возможности брони """
    return get_data_set(booking).isdisjoint(get_data_set([guest]))


# dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
# some_date = '14.11.2021-22.11.2021'
# print(is_available_date(dates, some_date))  # False

# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '01.11.2021'
# print(is_available_date(dates, some_date))  # True
