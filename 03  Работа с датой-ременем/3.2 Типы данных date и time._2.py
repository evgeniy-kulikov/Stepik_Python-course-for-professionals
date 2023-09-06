# 3.2 Типы данных date и time. Часть 2
""""""

from datetime import date, time

""" *  *  *  *  *  *  *  *  *   """
""" Форматирование даты и времени """
"""
По умолчанию вывод даты и времени осуществляется в ISO формате:
дата имеет вид: YYYY-MM-DD
время имеет вид: HH:MM:SS или HH:MM:SS.ffffff

Для форматированного вывода даты и времени используется метод strftime() (для обоих типов date и time).
"""
from datetime import date, time

my_date = date(2021, 8, 10)
my_time = time(7, 18, 34)

# вывод в ISO формате
print(my_date)  # 2021-08-10
print(my_time)  # 07:18:34

# форматированный вывод даты
print(my_date.strftime('%d/%m/%y'))        # 10/08/21
print(my_date.strftime('%A %d, %B %Y'))    # Tuesday 10, August 2021
print(my_time.strftime('%H.%M.%S'))        # 07.18.34


given_date = date(2021, 7, 17)

print(given_date.strftime('%A %d %B %Y'))  # Saturday 17 July 2021
print(given_date.strftime('%Y/%m/%d'))  # 2021/07/17
print(given_date.strftime('%d.%m.%Y (%A, %B)'))  # 17.07.2021 (Saturday, July)
print(given_date.strftime('Day of year: %j, week number: %U'))  # Day of year: 198, week number: 28


given_time = time(14, 4, 29)

print(given_time.strftime('Hours: %H, minutes: %M, seconds: %S.'))  # Hours: 14, minutes: 04, seconds: 29.
print(given_time.strftime('%H:%M:%S'))  # 14:04:29
print(given_time.strftime('%I:%M:%S %p'))  # 02:04:29 PM


""" *  *  *  *  *  *  *  *  *   """
""" Использование локализации """

# Для того чтобы использовать конкретную локализацию (перевод на язык),
# нужно использовать модуль locale

from datetime import date
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')  # установка русской локализации
my_date = date(2021, 8, 10)
print(my_date.strftime("%A %d, %B %Y"))  # вторник 10, Август 2021


locale.setlocale(locale.LC_ALL, 'en_EN.UTF-8')  # установка английской локализации
my_date = date(2021, 8, 10)
print(my_date.strftime("%A %d, %B %Y"))  # Tuesday 10, August 2021


""" *  *  *  *  *  *  *  *  *   """
""" Примечания """

#  Для того, чтобы получить строковое представление объектов типа date и time в ISO формате,
#  можно воспользоваться методом isoformat().

from datetime import date, time

my_date = date(2021, 12, 31)
my_time = time(21, 15, 17)

print('Дата: ' + my_date.isoformat())  # Дата: 2021-12-31
print('Время: ' + my_time.isoformat())  # Время: 21:15:17

# Аналогичный результат можно получить с помощью вызова встроенной функции str()
print('Дата: ' + str(my_date))  # Дата: 2021-12-31
print('Время: ' + str(my_time))  # Время: 21:15:17


""" *  *  *  *  *  *  *  *  *   """
""" Метод fromisoformat() """
"""
Самостоятельное преобразование данных из строки в объекты типа date и time достаточно неудобно. 
Для того чтобы преобразовать строку из ISO формата в объект даты (date), 
можно использовать метод fromisoformat(). Метод был добавлен в Python 3.7.
"""
from datetime import date

my_date = date.fromisoformat('2020-01-31')

print(my_date)  # 2020-01-31
print(type(my_date))  # <class 'datetime.date'>


""" *  *  *  *  *  *  *  *  *   """
""" Перехват ошибки ввода. Блок try-except """

from datetime import date, time

while True:  # читает данные до тех пор, пока пользователь не введет корректную дату
    try:
        day, month, year = input('Введите дату в формате ДД.ММ.ГГГГ').split('.')
        my_date = date(int(year), int(month), int(day))

        print('Введена корректная дата:', my_date)
        break
    except ValueError:    # перехватываем ошибку типа ValueError
        print('Введенная дата не является корректной, попробуйте еще раз')



""""""
"""   *   *   *   Task   *   *   *   """
""""""

#  01
"""
Для времени alarm вывести его компоненты:
количество часов в формате HH
количество минут в формате MM
количество секунд в формате SS
"""

from datetime import time

alarm = time(7, 30, 25)

print('Часы:', alarm.strftime('%H'))  # Часы: 07
print('Минуты:', alarm.strftime('%M'))  # Минуты: 30
print('Секунды:', alarm.strftime('%S'))  # Секунды: 25


#  02
"""
Для даты birthday вывести его компоненты:
полное название месяца на английском
полное название дня недели на английском
год в формате YYYY
номер месяца в формате MM
день месяца в формате DD
"""

from datetime import date

# import locale
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

birthday = date(1992, 10, 6)

print('Название месяца:', birthday.strftime('%B'))  # Название месяца: October
print('Название дня недели:', birthday.strftime('%A'))  # Название дня недели: Tuesday
print('Год:', birthday.strftime('%Y'))  # Год: 1992
print('Месяц:', birthday.strftime('%m'))  # Месяц: 10
print('День:', birthday.strftime('%d'))  # День: 06


#  03
"""
В переменной florida_hurricane_dates хранится список дат
Вывести самую раннюю дату из списка florida_hurricane_dates в трех различных форматах:
в стандарте ISO (YYYY-MM-DD)
в типичном для России стиле (DD.MM.YYYY)
в типичном для Америки стиле (MM/DD/YYYY)
"""
from datetime import date

florida_hurricane_dates = [date(1987, 11, 15), date(1988, 3, 12), date(1976, 5, 12)]   # для проведения теста

# присваиваем самую раннюю дату урагана в переменную first_date
first_date = min(florida_hurricane_dates)
print(first_date)

# конвертируем дату в ISO и RU формат
iso = 'Дата первого урагана в ISO формате: ' + first_date.isoformat()
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')

print(iso)  # 1976-05-12
print(ru)  # 12.05.1976
print(us)  # 05/12/1976


#  04
"""
Вывести дату 24 августа 1992 года в трех различных форматах:
в формате YYYY-MM
в формате month_name (YYYY), где month_name – полное название месяца на английском
в формате YYYY-day_number, где day_number – день года
"""
from datetime import date

andrew = date(1992, 8, 24)

print(andrew.strftime('%Y-%m'))   # 1992-08
print(andrew.strftime('%B (%Y)'))  # August (1992)
print(andrew.strftime('%Y-%j'))  # 1992-237


#  05
"""
Подаются две корректные даты в ISO формате (YYYY-MM-DD), каждая на отдельной строке.
Выбрать из двух введенных дат меньшую и вывести ее в формате DD-MM (YYYY).
Input:  1999-07-15
        1999-07-14
Output: 14-07 (1999)
"""
from datetime import date

dt1 = date.fromisoformat(input())
dt2 = date.fromisoformat(input())

print(min(dt1, dt2).strftime('%d-%m (%Y)'))


#  06
"""
Отсортированные даты
https://stepik.org/lesson/570048/step/13?unit=564591
Вывести введенные даты в порядке неубывания, каждую на отдельной строке, в формате DD/MM/YYYY
Input:  5
        2021-08-01
        2021-08-02
        2021-07-01
        2021-06-01
        2021-05-01
Output: 01/05/2021
        01/06/2021
        01/07/2021
        01/08/2021
        02/08/2021
"""
from datetime import date

dates = [date.fromisoformat(input()) for _ in range(int(input()))]
dates.sort()

for el in dates:
    print(el.strftime('%d/%m/%Y'))


#  07
"""
Функция print_good_dates()
https://stepik.org/lesson/570048/step/14?unit=564591
Input:  dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
        print_good_dates(dates)
Output: September 20, 1992
        October 19, 1992
"""
from datetime import date

def print_good_dates(dates: list):
    dates.sort()
    for el in dates:
        if el.year == 1992 and (el.day + el.month) == 29:
            print(el.strftime('%B %d, %Y'))

# Вариант преподавателя
def print_good_dates(dates):
    for el in sorted(filter(lambda d: d.year == 1992 and d.month + d.day == 29, dates)):
        print(el.strftime('%B %d, %Y'))

dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
# dates = []
print_good_dates(dates)


#  08
"""
Реализуйте функцию is_correct(), которая принимает три аргумента в следующем порядке:
day — натуральное число, день
month — натуральное число, месяц
year — натуральное число, год
Функция должна возвращать True, если дата с компонентами day, month и year является корректной, 
или False в противном случае.
Input:  print(is_correct(31, 13, 2021))
Output: False
"""
from datetime import date

def is_correct(day, month, year):
    try:
        date(int(year), int(month), int(day))
        return True
    except ValueError:
        return False

print(is_correct(31, 13, 2021))


#  09
"""
На вход программе подается последовательность дат в формате DD.MM.YYYY, каждая на отдельной строке. 
Концом последовательности является слово end.
Вывести текст Корректная или Некорректная в зависимости от того, является ли дата корректной, 
а затем вывести количество корректных дат.
Input:  19.05.2016
        05.13.2010
        21.12.2012
        01.01.1000
        32.04.2003
        end
Output: Корректная
        Некорректная
        Корректная
        Корректная
        Некорректная
        3
"""
from datetime import date

dates = []
while True:
    d = input()
    if d == 'end':
        break
    else:
        dates.append(d.split('.'))
# dates = [['19', '05', '2016'], ['05', '13', '2010'], ['21', '12', '2012'], ['01', '01', '1000'], ['32', '04', '2003']]

def is_correct(day, month, year):
    try:
        date(int(year), int(month), int(day))
        return True
    except ValueError:
        return False

cnt = 0
for el in dates:
    if is_correct(*el):
        print('Корректная')
        cnt += 1
    else:
        print('Некорректная')
print(cnt)


# Вариант преподавателя
def is_correct(day, month, year):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False


cnt = 0
dates = input()

while dates != 'end':
    if is_correct(*map(int, dates.split('.'))):
        print('Корректная')
        cnt += 1
    else:
        print('Некорректная')
    dates = input()

print(cnt)

