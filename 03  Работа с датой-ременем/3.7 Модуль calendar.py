# 3.7 Модуль calendar
""""""""

"""
По умолчанию модуль calendar следует григорианскому календарю, 
где понедельник является первым днем недели (имеет номер 0), 
а воскресенье — последним днем недели (имеет номер 6). 
В отличие от уже изученных модулей datetime и time, 
которые также предоставляют функции, связанные с календарем, 
модуль calendar предоставляет основные функции, 
связанные с отображением и манипулированием календарями.
"""

""" *  *  *  *  *  *  *  *  *   """
""" Атрибуты модуля calendar """

"""Атрибут day_name"""
# возвращает итерируемый объект, содержащий названия дней недели на английском языке.
import calendar

d_n = calendar.day_name[0]  # 'Monday'
d_n = calendar.day_name[6]  # 'Sunday'

# локализация на русский язык (названия дней недели выводятся с маленькой буквы.)
import calendar, locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
d_n = calendar.day_name[0]  # 'понедельник'
d_n = calendar.day_name[6]  # 'воскресенье'
names = list(calendar.day_name)
# ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

"""Атрибут day_abbr"""
# возвращает итерируемый объект, содержащий сокращенные названия дней недели.
import calendar

d_a = calendar.day_abbr[0]  # 'Mon'
d_a = calendar.day_abbr[6]  # 'Sun'

#  на русском языке сокращенные названия дней недели выводятся с большой буквы
import calendar, locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
d_a = calendar.day_abbr[0]  # 'Пн'
d_a = calendar.day_abbr[6]  # 'Вс'

"""Атрибут month_name"""
# возвращает итерируемый объект, содержащий названия месяцев года.
# !!!  атрибут month_name соответствует соглашению, что январь – это месяц номер 1,
#  поэтому список имеет длину в 13 элементов, первый из которых – пустая строка.
import calendar, locale

english_names = list(calendar.month_name)
# ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
russian_names = list(calendar.month_name)
# ['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']


"""Атрибут month_abbr"""
# возвращает итерируемый объект, содержащий сокращенные названия месяцев года
import calendar, locale

english_names = list(calendar.month_abbr)
# ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
russian_names = list(calendar.month_abbr)
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# ['', 'янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']


"""Атрибуты номеров дней недели"""
# Для получения номеров дней недели можно использовать атрибуты: MONDAY, TUESDAY, ..., SUNDAY
import calendar

s = calendar.MONDAY  # 0
s = calendar.SUNDAY  # 6


""" *  *  *  *  *  *  *  *  *   """
""" Функции модуля calendar """


""" firstweekday() """
#  возвращает целое число, означающее день недели, установленное в качестве начала недели
import calendar
w_f = calendar.firstweekday()  # 0

""" setfirstweekday() """
# устанавливает заданный день недели в качестве начала недели.
import calendar

w_d = calendar.firstweekday()  # 0
# установить первый будний день - воскресенье
calendar.setfirstweekday(calendar.SUNDAY)  # эквивалентно calendar.setfirstweekday(6)
w_d = calendar.firstweekday()  # 6


""" isleap() """
# год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400
# isleap() осуществляет данную проверку

import calendar

calendar.isleap(2020)  # True
calendar.isleap(2021)  # False


""" leapdays() """
# возвращает количество високосных лет в диапазоне от y1 до y2 (исключая)
import calendar
calendar.leapdays(2020, 2024)  # 1


""" weekday() """
# weekday(year, month, day) возвращает день недели в виде целого числа
# где 0 – понедельник, 6 – воскресенье) для заданной даты.
import calendar
calendar.weekday(2021, 9, 1)  # 2
calendar.weekday(2021, 9, 2)  # 3


""" monthrange() """
# Функция monthrange(year, month) возвращает день недели первого дня месяца и количество дней в месяце
# в виде кортежа для указанного года year и месяца month.
import calendar
calendar.monthrange(2022, 1)  # (5, 31)
calendar.monthrange(2021, 9)  # (2, 30)


""" monthcalendar() """
# возвращает матрицу, представляющую календарь на месяц. Каждая строка матрицы представляет неделю.
#  дни, которые не входят в указанный месяц, представлены нулями.
#  При этом каждая неделя начинается с понедельника, если не установлено другое функцией setfirstweekday().
import calendar

m_c = calendar.monthcalendar(2023, 9)
# [[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 0]]

print(*calendar.monthcalendar(2023, 9), sep='\n')
"""
[0, 0, 0, 0, 1, 2, 3]
[4, 5, 6, 7, 8, 9, 10]
[11, 12, 13, 14, 15, 16, 17]
[18, 19, 20, 21, 22, 23, 24]
[25, 26, 27, 28, 29, 30, 0]
"""


""" month() """
"""
Функция month(year, month, w=0, l=0) возвращает календарь на месяц в многострочной строке. 
Аргументами функции являются: 
year (год), month (месяц), w (ширина столбца даты) и l (количество строк, отводимые на неделю).
Аргументы w и l имеют значения по умолчанию, поэтому их можно не передавать явно при вызове функции.
"""
import calendar

print(calendar.month(2023, 9))
"""
   September 2023
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30
"""

print(calendar.month(2021, 9, w=4, l=2))
"""
          September 2021

Mon  Tue  Wed  Thu  Fri  Sat  Sun

            1    2    3    4    5

  6    7    8    9   10   11   12

 13   14   15   16   17   18   19

 20   21   22   23   24   25   26

 27   28   29   30
"""


""" calendar() """
"""
Функция calendar(year, w=2, l=1, c=6, m=3) возвращает календарь на весь год в виде многострочной строки. 
Аргументами функции являются: 
year (год),  
w (ширина столбца даты) и l (количество строк, отводимые на неделю), 
c (количество пробелов между столбцом месяца),  
m (количество столбцов).

Аргументы w, l, c, m имеют значения по умолчанию, поэтому их можно не передавать явно при вызове функции.
"""


""" prmonth(), prcal() """
"""
prmonth() - печатает календарь на месяц   - print(month(year, month, w=0, l=0))
prcal() - печатает календарь на весь год  - print(calendar(year, w=0, l=0, c=6, m=3)
"""


""""""
"""   *   *   *   Task   *   *   *   """
""""""


#  3.7-01
"""
Напишите программу, которая определяет, является ли год високосным
На вход программе в первой строке подается целое число n, 
в последующих n строках вводятся натуральные числа, представляющие года.
Вывести True, если он является високосным, или False в противном случае.
Input:  4
        1999
        2000
        2001
        2002
Output: False
        True
        False
        False
"""
from calendar import isleap

cal = [int(input()) for _ in range(int(input()))]
for el in cal:
    print(isleap(el))


# Короче
from calendar import isleap

for _ in range(int(input())):
    print(isleap(int(input())))


#  3.7-02
"""
Календарь на месяц
Input:  2021 Dec  (подаются год и сокращенное название месяца на английском, разделенные пробелом)
Output: вывести календарь на введенные год и месяц.
"""
import calendar

year, month = input().split()
abr = list(calendar.month_abbr)

for el in abr:
    if el == month:
        month = abr.index(el)

calendar.prmonth(int(year), month)

# Короче 1
import calendar
year, month = input().split()
index = list(calendar.month_abbr).index(month)
print(calendar.month(int(year), index))

# Короче 2
from calendar import prmonth
from datetime import datetime
dt = datetime.strptime(input(), '%Y %b')
prmonth(dt.year, dt.month)


#  3.7-03
"""
На вход программе подается дата в формате YYYY-MM-DD
Вывести полное название дня недели на английском, который соответствует введенной дате
Input:  2021-11-02
Output: Tuesday
"""
import calendar
from datetime import datetime

data_in = datetime.strptime(input(), '%Y-%m-%d').weekday()
print(calendar.day_name[data_in])


# Вариант
days = list(calendar.day_name)
print(days[datetime.strptime(input(), '%Y-%m-%d').weekday()])


#  3.7-04
"""
вход программе подаются год и порядковый номер месяца (начиная с 1), разделенные пробелом.
вывести единственное число — количество дней в введенном месяце.
Input:  2008 1
Output: 31
"""
import calendar

year, month = map(int, input().split())
print(calendar.monthrange(year, month)[1])


#  3.7-05
"""
вход программе подаются год и полное название месяца на английском, разделенные пробелом.
вывести единственное число — количество дней в введенном месяце
Input:  1983 January
Output: 31
"""
import calendar

year, month = input().split()
m = list(calendar.month_name).index(month)
print(calendar.monthrange(int(year), m)[1])


#  3.7-06
"""
Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем порядке:
year — натуральное число
month — полное название месяца на английском
Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month и года year.
Input:  get_days_in_month(2021, 'December')
Output: [datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), ..., 
        datetime.date(2021, 12, 30), datetime.date(2021, 12, 31)]
"""
import calendar
from datetime import date

def get_days_in_month(year: int, month: str):
    month = list(calendar.month_name).index(month)
    cnt_days = calendar.monthrange(year, month)[1]
    return [date(year, month, el) for el in range(1, cnt_days + 1)]


print(get_days_in_month(2021, 'December'))


#  3.7-07
"""
Реализуйте функцию get_all_mondays(), которая принимает один аргумент:
year — натуральное число
Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year, 
выпадающих на понедельник.
Input:  get_all_mondays(2021)
Output: [datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ..., 
        datetime.date(2021, 12, 20), datetime.date(2021, 12, 27)]
"""
import calendar
from calendar import monthrange
from datetime import date

def get_all_mondays(year: int):
    res = []
    for m in range(1, 13):
        for d in range(1, monthrange(year, m)[1] + 1):
            if calendar.weekday(year, m, d) == 0:
                res += [date(year, m, d)]
    return res

print(get_all_mondays(2021))


#  использование calendar.monthcalendar()
import calendar
from datetime import date

def get_all_mondays(year):
    res = []
    for m in range(1, 13):
        for week in calendar.monthcalendar(year, m):
            if week[0]:
                res.append(date(year, m, week[0]))
    return res


#  3.7-08
"""
Во многих музеях существует один день месяца, когда посещение музея бесплатно. 
Например, это третий четверг месяца.
Определить даты бесплатных дней посещения музея в заданном году.
Input:  2021
Output: Даты должны быть расположены в порядке возрастания, каждая на отдельной строке, в формате DD.MM.YYYY.
        21.01.2021
        18.02.2021
        ...
        18.11.2021
        16.12.2021
"""
import calendar
from datetime import date

year = int(input())

for month in range(1, 13):
    if calendar.monthcalendar(year, month)[0][3]:  # если в первой неделе месяца есть четверг
        day = calendar.monthcalendar(year, month)[2][3]
    else:
        day = calendar.monthcalendar(year, month)[3][3]  # иначе сдвигаемся на одну неделю
    res = date(year, month, day)
    print(res.strftime('%d.%m.%Y'))

