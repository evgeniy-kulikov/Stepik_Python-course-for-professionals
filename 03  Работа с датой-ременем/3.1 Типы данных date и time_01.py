# 3.1 Типы данных date и time. Часть 1
""""""

from datetime import date, time


""" *  *  *  *  *  *  *  *  *   """
""" Модуль datetime """
"""
Модуль datetime состоит из нескольких типов данных:

date	    представляет собой информацию о дате, исключая данные о времени, на основе Григорианского календаря
time	    представляет собой информацию о времени, полностью исключая сведения о дате
datetime	содержит информацию о времени и дате, основываясь на данных из Григорианского календаря
timedelta	описывает определенный период во времени, который находится между двумя различными моментами
tzinfo	    представляет различные сведения о часовом поясе
timezone	описывает время, руководствуясь стандартом UTC
"""


""" *  *  *  *  *  *  *  *  *   """
""" Тип данных date """

"""
date(year, month, day)
атрибуты (обязательно указать все):
year — год даты
month — месяц даты
day — день даты
"""

# При создании новой даты (тип данных date) нужно указать год, месяц и день.
my_date = date(1992, 10, 6)    # тип date: год + месяц + день
print(my_date)  # 1992-10-06

# Через именованные аргументы (порядок не имеет значение)
print(date(day=6, month=10, year=1992))  # 1992-10-06

print(type(my_date))  # <class 'datetime.date'>

# Работа с атрибутами
my_date = date(1992, 10, 6)

print('Год =', my_date.year)  # Год = 1992
print('Месяц =', my_date.month)  # Месяц = 10
print('День =', my_date.day)  # День = 6

# получить информацию о текущей дате на компьютере
creation_date = date.today()
print(creation_date)  # 2023-09-04

# получить текущие дату и время
from datetime import datetime

dt_now = datetime.now()
print(dt_now)  # 2023-09-04 21:29:19.405478
print(dt_now.strftime('%Y-%m-%d %H:%M:%S'))  # 2023-09-04 21:29:19


"""
С помощью встроенного метода weekday() можно определить день недели (нумерация начинается с 0):
0 = понедельник
1 = вторник
2 = среда
3 = четверг
4 = пятница
5 = суббота
6 = воскресенье
"""
date1 = date(2023, 9, 4)
date2 = date(1999, 12, 26)

print(date1.weekday())  # 0
print(date2.weekday())  # 6

# Если требуется определить день недели с нумерацией, начиная с 1, то используется метод isoweekday()
print(date1.isoweekday())  # 1
print(date2.isoweekday())  # 7

#  Для получения минимально и максимально возможных дат (в рамках типа данных date)
print(date.min)  # 0001-01-01
print(date.max)  # 9999-12-31


#  Методы fromordinal() и toordinal()
#  позволяют создать дату из номера дня, начиная с 0001-01-01, и наоборот, преобразовать дату в номер дня.
date1 = date.fromordinal(365)  # дата, соответствующая номеру дня 365 (отчет от 0001-01-01)
print(date1)  # 0001-12-31

date2 = date(1999, 12, 26)  # Номер дня, соответствующий дате 1999-12-26 (отчет от 0001-01-01 т.е. сколько прошло дней)
print(date2.toordinal())  # 730114


""" *  *  *  *  *  *  *  *  *   """
""" Тип данных time """

# from datetime import time

# При создании времени (тип данных time) нужно указать часы, минуты, секунды и микросекунды.
my_time = time(11, 20, 54, 1234)    # тип time: часы + минуты + секунды + микросекунды

print(my_time)  # 11:20:54.001234
print(type(my_time))  # <class 'datetime.time'>

# Через именованные аргументы (hour, minute, second, microsecond). Порядок не имеет значение
"""
В отличие от дат (тип данных date) необязательно указывать все его атрибуты в конструкторе. 
Недостающие данные о времени автоматически заполняются нулями.
"""
time1 = time(11, 20, 54, 1234)  # 11:20:54.001234
time2 = time(11, 20, 54)  # 11:20:54
time3 = time(11, 20)  # 11:20:00
time4 = time(11)  # 11:00:00
time5 = time()  # 00:00:00
time6 = time(minute=23, second=56)  # 00:23:56

"""
Атрибуты  time:
hour — часы времени
minute — минуты времени
second — секунды времени
microsecond — микросекунды времени
"""
my_time = time(11, 20, 54, 1234)

print('Часы =', my_time.hour)  # Часы = 11
print('Минуты =', my_time.minute)  # Минуты = 20
print('Секунды =', my_time.second)  # Секунды = 54
print('Микросекунды =', my_time.microsecond)  # Микросекунды = 1234


""" *  *  *  *  *  *  *  *  *   """
""" Сравнение дат и времени """

#  Дату (тип date) и время (тип time) можно сравнивать с помощью операторов ==, !=, <, >, <= и  >=
# from datetime import date, time

date1 = date(2022, 10, 15)
date2 = date(1999, 12, 26)

time1 = time(13, 10, 5)
time2 = time(21, 32, 59)

print(date1 < date2)  # False
print(time1 < time2)  # True


""" *  *  *  *  *  *  *  *  *   """
""" Функции str() и repr() """

# from datetime import date, time

my_date = date(2021, 12, 31)
my_time = time(11, 20, 54)

# Встроенная функция str() возвращает объект в неформальном (понятном человеку) строковом представлении.
print(str(my_date))  # 2021-12-31
print(str(my_time))  # 11:20:54

# Встроенная функция repr() возвращает объект в формальном (понятном интерпретатору) строковом представлении.
print(repr(my_date))  # datetime.date(2021, 12, 31)
print(repr(my_time))  # datetime.time(11, 20, 54)


# Для встроенных типов данных при печати одиночного значения объекта явно вызывать функцию str() не требуется,
# однако при печати списка таких объектов это необходимо.

dates = [date(2021, 12, 31), date(2019, 10, 6), date(2022, 11, 8)]
print(dates)
# [datetime.date(2021, 12, 31), datetime.date(2019, 10, 6), datetime.date(2022, 11, 8)]

dates = [str(date(2021, 12, 31)), str(date(2019, 10, 6)), str(date(2022, 11, 8))]
print(dates)
# ['2021-12-31', '2019-10-06', '2022-11-08']

# Если мы хотим вывести содержимое списка в человеческом виде, то нужно прибегнуть к распаковке,
# в этом случае функция str() будет вызываться для каждого элемента списка за кулисами.
dates = [date(2021, 12, 31), date(2019, 10, 6), date(2022, 11, 8)]
print(*dates, sep='\n')
# 2021-12-31
# 2019-10-06
# 2022-11-08


""" *  *  *  *  *  *  *  *  *   """
""" Примечания """

"""
Оба типа данных date и time являются неизменяемыми. 
Мы можем создать множества, содержащие объекты данных типов (date и time), 
а также они могут выступать в качестве ключей словаря.
"""
# from datetime import date

my_set = {date(2021, 12, 31), date(2019, 3, 19), date(2022, 5, 25)}                # множество
my_dict = {date(2021, 12, 31): 'Новый год', date(2030, 10, 6): 'День рождения'}    # словарь

print(my_set)  # {datetime.date(2019, 3, 19), datetime.date(2021, 12, 31), datetime.date(2022, 5, 25)}
print(my_dict)  # {datetime.date(2021, 12, 31): 'Новый год', datetime.date(2030, 10, 6): 'День рождения'}


"""
Мы можем использовать встроенные функции min(), max(), sorted() и т.д. при работе с типами данных date и time.
"""
# from datetime import date, time

dates = [date(2021, 12, 31), date(2025, 3, 19), date(2017, 5, 25)]

print(min(dates))  # 2017-05-25
print(max(dates))  # 2025-03-19
print(sorted(dates))  # [datetime.date(2017, 5, 25), datetime.date(2021, 12, 31), datetime.date(2025, 3, 19)]

"""
Для создания новой даты на основании уже существующей можно использовать метод replace(). 
Он возвращает новую дату с переданными измененными значениями свойств year, month, day.
"""
# from datetime import date

date1 = date(1992, 10, 6)
date2 = date1.replace(year=1995)            # заменяем год
date3 = date1.replace(month=12, day=17)     # заменяем месяц и число

print(date1)  # 1992-10-06
print(date2)  # 1995-10-06
print(date3)  # 1992-12-17

"""
Аналогично для создания нового времени на основании уже существующего используется метод replace()
"""
from datetime import time

time1 = time(17, 10, 6)
time2 = time1.replace(hour=21)                  # заменяем час
time3 = time1.replace(minute=48, second=59)     # заменяем минуты и секунды

print(time1)  # 17:10:06
print(time2)  #  21:10:06
print(time3)  # 17:48:59


"""
В качестве ограничений по годам в типе date используются значения MINYEAR=1 и MAXYEAR=9999
"""

"""
По умолчанию объекты типов date и time выводятся в ISO 8601 формате:

дата в формате ISO 8601 имеет вид: YYYY-MM-DD
время в формате ISO 8601 имеет вид: HH:MM:SS или HH:MM:SS.ffffff
https://ru.wikipedia.org/wiki/ISO_8601
"""


"""   *   *   *   Task   *   *   *   """


# 01
"""
Вывести текущую дату в ISO формате (YYYY-MM-DD)
"""
# импортируем тип date из модуля datetime
from datetime import date

# выводим текущую дату
now = date.today()
print(now)  # 2023-09-04

# Вариант
from datetime import datetime
print(datetime.now().strftime('%Y-%m-%d'))  # 2023-09-04


#  02
"""
Вывести день недели (начиная с 0) для даты 24 августа 1992 года,
"""
# импортируем тип date из модуля datetime
from datetime import date

# создаем объект, соответсвующий дате урагана
hurricane_andrew = date(1992, 8, 24)

# выводим день недели
print(hurricane_andrew.weekday())  # 0


#  03
"""
https://stepik.org/lesson/609341/step/18?unit=604560
florida_hurricane_dates = [date(1987, 11, 15), date(1988, 3, 12), date(1976, 5, 12)]
Input:  *
Output: Из 235 ураганов только 10 обрушились на Флориду до официального начала сезона ураганов.
"""
# импортируем тип date из модуля datetime
from datetime import date

florida_hurricane_dates = [date(1987, 11, 15), date(1988, 3, 12), date(1976, 5, 12)]  # Тестовый список

# счетчик для нужного количества ураганов
early_hurricanes = 0

# цикл по датам в которые был ураган
for hurricane in florida_hurricane_dates:
    # если месяц урагана меньше чем июнь (порядковый номер 6)
    if hurricane.month < 6:
        early_hurricanes += 1

print(early_hurricanes)  # 10


#  04
"""
https://stepik.org/lesson/609341/step/19?unit=604560
1 квартал	январь, февраль, март
2 квартал	апрель, май, июнь
3 квартал	июль, август, сентябрь
4 квартал	октябрь, ноябрь, декабрь
Input:  *
Output: <год>-Q<номер квартала>
        2010-Q3
        2017-Q1
"""
from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11),
         date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21),
         date(1666, 6, 6), date(1968, 5, 26)]

# Через словарь
quarter = {'Q1': (1, 2, 3),
           'Q2': (4, 5, 6),
           'Q3': (7, 8, 9),
           'Q4': (10, 11, 12)}

for el in dates:
    for key in quarter.keys():
        if el.month in quarter[key]:
            print(f'{el.year}-{key}')
            break  # исключить лишние проверки

# Хорошее решение
for el in dates:
    print(f'{el.year}-Q{(el.month + 2) // 3}')

# Вариант через округление
from math import ceil

for el in dates:
    print(f'{el.year}-Q{ceil(el.month / 3)}')


#  05
"""
Реализуйте функцию get_min_max(), которая принимает один аргумент:
dates — список дат (тип date)
Функция должна возвращать кортеж, 
первым элементом которого является минимальная дата из списка dates, 
вторым — максимальная дата из списка dates. 
Если список dates пуст, функция должна вернуть пустой кортеж.
Input:  dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
        print(get_min_max(dates))
Output: (datetime.date(1992, 6, 10), datetime.date(2021, 10, 5))
"""

# dates = [date(2021, 10, 5), date(2021, 10, 5), date(2021, 10, 5), date(2021, 10, 5)]
# (datetime.date(2021, 10, 5), datetime.date(2021, 10, 5))

# dates = [date(1999, 9, 9)]
# (datetime.date(1999, 9, 9), datetime.date(1999, 9, 9))

# dates = []
# ()

from datetime import date

def get_min_max(lst: list) -> tuple:
    if lst:
        return min(lst), max(lst)
    return ()

dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
print(get_min_max(dates))
# (datetime.date(1992, 6, 10), datetime.date(2021, 10, 5))


#  06
"""
Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:
start — начальная дата, тип date
end — конечная дата, тип date
Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start до end включительно. 
Если start > end, функция должна вернуть пустой список.
"""

from datetime import date

def get_date_range(start: date, end: date) -> list:
    if start > end:
        return []
    return [date.fromordinal(el) for el in range(start.toordinal(), end.toordinal() + 1)]


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')
# 2021-10-01
# 2021-10-02
# 2021-10-03
# 2021-10-04
# 2021-10-05


from datetime import date

#  07
"""
Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:
start — начальная дата, тип date
end — конечная дата, тип date
Функция должна возвращать количество суббот между датами start и end включительно.
Даты могут передаваться в любом порядке, то есть не гарантируется, что первая дата меньше второй.
"""


from datetime import date

def saturdays_between_two_dates(start: date, end: date) -> int:
    if start > end:
        start, end = end, start
    res = [date.fromordinal(el).weekday() == 5 for el in range(start.toordinal(), end.toordinal() + 1)]
    return sum(res)

# Вариант
def saturdays_between_two_dates(start: date, end: date) -> int:
    if start > end:
        start, end = end, start
    res = [date.fromordinal(el) for el in range(start.toordinal(), end.toordinal() + 1)]
    return len(list(filter(lambda el: el.weekday() == 5, res)))


date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)
print(saturdays_between_two_dates(date1, date2))  # 3

