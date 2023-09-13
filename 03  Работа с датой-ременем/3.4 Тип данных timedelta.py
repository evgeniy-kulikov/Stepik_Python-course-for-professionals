#  3.4 Тип данных timedelta
""""""

""" *  *  *  *  *  *  *  *  *   """
""" Тип данных timedelta """

"""
Тип данных timedelta представляет из себя временной интервал (разница между двумя объектами datetime или date) 
и используется для удобного выполнения различных манипуляций над типами datetime или date.
При создании объекта timedelta можно указать следующие аргументы (по умолчанию равны 0):
недели (weeks)
дни (days)
часы (hours)
минуты (minutes)
секунды (seconds)
миллисекунды (milliseconds)
микросекунды (microseconds)

Аргументы могут быть целыми числами или числами с плавающей запятой, 
а также могут быть как положительными, так и отрицательными. 
"""
from datetime import timedelta

delta = timedelta(days=7, hours=20, minutes=7, seconds=17)

print(delta)  # 7 days, 20:07:17
print(type(delta))  # <class 'datetime.timedelta'>


#  Аргументы, кроме days, seconds, microseconds, объединяются и нормализуются в три результирующих сочетания.
from datetime import timedelta

delta1 = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)
# 64 days, 8:05:56.000010

delta2 = timedelta(weeks=1, hours=23, minutes=61)       # 8 days, 0:01:00
delta3 = timedelta(hours=25)                            # 1 day, 1:00:00
delta4 = timedelta(minutes=300)                         # 5:00:00
# если во временном интервале (timedelta) значение days равно нулю, то оно не выводится
print(delta1, delta2, delta3, delta4, sep='\n')


# временной интервал (timedelta) может быть отрицательным.
from datetime import timedelta

delta1 = timedelta(minutes=-40)             # -1 day, 23:20:00
delta2 = timedelta(seconds=-10, weeks=-2)   # -15 days, 23:59:50


""" *  *  *  *  *  *  *  *  *   """
""" Атрибуты days, seconds, microseconds и метод total_seconds() """

# тип timedelta внутренне хранит только сочетание days, seconds, microseconds,
# которые можно получить с помощью одноименных атрибутов  (всего три атрибута).

from datetime import timedelta

delta = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)

print('Количество дней =', delta.days)                      # Количество дней = 64
print('Количество секунд =', delta.seconds)                 # Количество секунд = 29156
print('Количество микросекунд =', delta.microseconds)       # Количество микросекунд = 10
print('Общее количество секунд =', delta.total_seconds())   # Общее количество секунд = 5558756.00001  (тип float)


"""
Метод total_seconds() возвращает общее количество секунд, содержащееся во временном интервале timedelta.
у типа timedelta нет атрибутов hours и minutes, позволяющих получить количество часов и минут соответственно. 
Достать часы и минуты можно так:
"""
def hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60

delta = timedelta(days=7, seconds=125, minutes=10, hours=8, weeks=2)

hours, minutes = hours_minutes(delta)

print(delta)    # 21 days, 8:12:05
print(hours)    # 8
print(minutes)  # 12


""" *  *  *  *  *  *  *  *  *   """
""" Сравнение временных интервалов """

# Временные интервалы (тип timedelta) можно сравнивать (==, !=, <, >, <=, >=), как и любые другие типы данных.
from datetime import timedelta

delta1 = timedelta(weeks=1)
delta2 = timedelta(hours=24 * 7)
delta3 = timedelta(minutes=24 * 7 * 59)

print(delta1 == delta2)     # True
print(delta1 != delta3)     # True
print(delta1 < delta3)      # False


# Операторы сравнения == или != всегда возвращают значение bool, независимо от типа сравниваемого объекта.
from datetime import timedelta

delta1 = timedelta(seconds=57)
delta2 = timedelta(hours=25, seconds=2)

print(delta1 != 57)     # True
print(delta2 == '5')    # False


# Для всех других операторов сравнения,
# таких как <, >, <=, >=, когда объект timedelta сравнивается с объектом другого типа,
# возникает ошибка (исключение) TypeError.
from datetime import timedelta

delta1 = timedelta(seconds=57)
delta2 = timedelta(hours=25, seconds=2)

print(delta2 > delta1)  # True
print(delta2 > 5)       # TypeError: '>' not supported between instances of 'datetime.timedelta' and 'int'


""" *  *  *  *  *  *  *  *  *   """
""" Операции над временными интервалами timedelta """

# Сумма и разность временных интервалов
from datetime import timedelta

delta1 = timedelta(days=5) + timedelta(seconds=3600)  # 5 дней + 1 час
delta2 = timedelta(days=5) - timedelta(seconds=3600)  # 5 дней - 1 час

print(delta1)  # 5 days, 1:00:00
print(delta2)  # 4 days, 23:00:00


# Умножение временного интервала на число (типы int и float)
# !!!  При умножении временного интервала на вещественное число (тип float) может возникнуть округление
from datetime import timedelta

delta1 = 48 * timedelta(hours=1)     # 2 days, 0:00:00
delta2 = timedelta(weeks=1) * (3/7)  # 3 days, 0:00:00


# Деление временных интервалов на число (типы int и float)
# !!!  При делении временного интервала на вещественное число (тип float) может возникнуть округление
from datetime import timedelta

delta = timedelta(hours=1, minutes=6)
delta1 = delta / 2   # 0:33:00
delta2 = delta // 5   # 0:13:12


# Деление временного интервала на временной интервал
# С помощью операторов / и // мы также можем делить один временной интервал (тип timedelta) на другой.
# По сути происходит деление общей длительности одного интервала на общую длительность другого интервала.
from datetime import timedelta

delta1 = timedelta(weeks=1) / timedelta(hours=5)       # обычное деление, результат float
delta2 = timedelta(weeks=1) // timedelta(hours=5)      # целочисленное деление, результат int

print(delta1)  # 33.6
print(delta2)  # 33


#  можем использовать оператор нахождения остатка от деления %, при этом остаток вычисляется как объект timedelta
from datetime import timedelta

delta1 = timedelta(weeks=1) % timedelta(hours=5)         # 3 часа
delta2 = timedelta(hours=1) % timedelta(minutes=7)       # 4 минуты

print(delta1)  # 3:00:00
print(delta2)  # 0:04:00


# Сложить дату и период
from datetime import date, timedelta
d_start = date(2021, 1, 1)  # 2021-01-01
td = timedelta(days=7)  # 7 days, 0:00:00
res = d_start + td
print(res)  # 2021-01-08


# Задача: рабочая смена длится 7 часов 30 минут, сколько полных смен в 3-х сутках?
from datetime import timedelta

all_time = timedelta(days=3)
smena = timedelta(hours=7, minutes=30)

print(all_time // smena)  # 9
print(all_time % smena)  # 4:30:00
# Таким образом, в 3-х сутках помещается 9 полных смен и еще останется 4 часа 30 минут


""" *  *  *  *  *  *  *  *  *   """
""" Операции над datetime и date """
# К объектам типа datetime и date можно прибавлять (вычитать) временные интервалы (тип timedelta),
# тем самым формируя новые объекты.
from datetime import datetime, date, timedelta

my_datetime1 = datetime(2021, 1, 1, 12, 15, 20) + timedelta(weeks=1, hours=25)  # 2021-01-09 13:15:20
my_datetime2 = datetime(2021, 1, 1, 12, 15, 20) - timedelta(weeks=1, hours=25)  # 2020-12-24 11:15:20

my_date1 = date(2021, 1, 1) + timedelta(hours=49)  # 2021-01-03
my_date2 = date(2021, 1, 1) - timedelta(hours=49)  # 2020-12-30

print(my_datetime1, my_datetime2, my_date1, my_date2, sep='\n')


""" *  *  *  *  *  *  *  *  *   """
""" Примечания """
# Тип данных timedelta является неизменяемым.

# Встроенные функции str() и repr() можно использовать для преобразования объектов типа timedelta к строковому типу
from datetime import timedelta

delta1 = timedelta(weeks=1, hours=23, minutes=61)
delta2 = timedelta(minutes=-300)

print(str(delta1), str(delta2), sep='\n')
# 8 days, 0:01:00
# -1 day, 19:00:00

print(repr(delta1), repr(delta2), sep='\n')
# datetime.timedelta(days=8, seconds=60)
# datetime.timedelta(days=-1, seconds=68400)


# При работе с типом timedelta мы можем использовать встроенную функцию abs().
# Функция возвращает объект timedelta с положительным значением всех атрибутов.
from datetime import timedelta

delta = timedelta(days=-2, minutes=-300)
abs_delta = abs(delta)

print('Исходная:', delta.days, delta.seconds, delta, sep='\n')
# Исходная:
# -3
# 68400
# -3 days, 19:00:00

print('С модулем:', abs_delta.days, abs_delta.seconds, abs_delta, sep='\n')
# С модулем:
# 2
# 18000
# 2 days, 5:00:00

td = timedelta(weeks=-1, hours=-20, minutes=-120)       # -8 days, 2:00:00
abs_td = abs(td)                                         # 7 days, 22:00:00


""""""
""""""
"""   *   *   *   Task   *   *   *   """
""""""
""""""


#  3.4-01
"""
Прибавить к объекту datetime(2021, 11, 4, 13, 6) одну неделю и 12 часов 
и вывести результат в формате DD.MM.YYYY HH:MM:SS.
Input:  *
Output: 12.11.2021 01:06:00
"""
from datetime import datetime, timedelta

dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)

# print(dt.strftime('%d.%m.%Y %H:%M:%S'))
print(dt.strftime('%d.%m.%Y %X'))


#  02
"""
Вывести количество дней (целое число) между датами today и birthday
Input:  *
Output: 336
"""
from datetime import date

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = (birthday - today).days
print(days)


#  3.4-03
"""
На вход подается дата в формате DD.MM.YYYY
Вывести  предыдущую и следующую даты относительно введенной даты, каждую на отдельной строке, в формате DD.MM.YYYY.
Гарантируется, что у подаваемой даты есть предыдущая и следующая даты.
Input:  01.11.2021
Output: 31.10.2021
        02.11.2021
"""
# from datetime import date, datetime, timedelta
from datetime import datetime, timedelta

data_in = datetime.strptime(input(), '%d.%m.%Y')

data_previous = data_in - timedelta(days=1)
data_next = data_in + timedelta(days=1)

print(data_previous.strftime('%d.%m.%Y'))
print(data_next.strftime('%d.%m.%Y'))


# Вариант преподавателя
from datetime import datetime, timedelta

pattern, td = '%d.%m.%Y', timedelta(days=1)

data_in = datetime.strptime(input(), pattern)

print((data_in - td).strftime(pattern))
print((data_in + td).strftime(pattern))


#  3.4-04
"""
На вход подается время в формате HH:MM:SS.
Вывести целое количество секунд, прошедшее с начала суток.
Началом суток считается момент времени, соответствующий 00:00:00.
Input:  00:01:01
Output: 61
"""
# from datetime import date, datetime, timedelta

from datetime import datetime

data_input = datetime.strptime(input(), '%H:%M:%S')
data_start = datetime.strptime('00:00:00', '%H:%M:%S')

print((data_input - data_start).seconds)


# Вариант
from datetime import timedelta

h, m, s = map(int, input().split(':'))
td = timedelta(hours=h, minutes=m, seconds=s)

print(td.seconds)


#  3.4-05
"""
На вход программе в первой строке подается текущее время на часах в формате HH:MM:SS. 
В следующей строке вводится целое неотрицательное число n — количество секунд, через которое должен прозвенеть таймер.
Вывести время в формате HH:MM:SS, которое будет на часах, когда прозвенит таймер.
Input:  09:00:00
        90
Output: 09:01:30
"""
from datetime import date, datetime, timedelta, time
from datetime import datetime, timedelta

time_start = datetime.strptime(input(), '%H:%M:%S')
time_delta = timedelta(seconds=(int(input())))

res = time_start + time_delta
print(res.strftime('%H:%M:%S'))


# Вариант
from datetime import datetime, timedelta

pattern = '%H:%M:%S'
res = datetime.strptime(input(), pattern) + timedelta(seconds=int(input()))

print(res.strftime(pattern))


#  3.4-06
"""
Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:
year — натуральное число, год
Функция должна возвращать количество воскресений в году year.
Input:  print(num_of_sundays(2021))
Output: 52
"""
# from datetime import date, datetime, timedelta, time
from datetime import date, timedelta

def num_of_sundays(year):
    d_start = date(year, 1, 1).toordinal()
    d_end = date(year + 1, 1, 1).toordinal()
    cnt = 0

    for el in range(d_start, d_end):
        if date.fromordinal(el).weekday() == 6:
            cnt += 1
    return cnt


# Вариант преподавателя
def num_of_sundays(year):
    counter = 0
    td = timedelta(days=7)  # Интервал 7 дней
    d_start = date(year, 1, 1)  # Начало года

    d_start += timedelta(days=6 - d_start.weekday())  # Переходим на первое воскресенье года
    while d_start.year == year:
        d_start += td  # Приращение даты на 7 дней
        counter += 1
    return counter


# Вариант
#  %U - Порядковый номер недели в году от 0 до 52. Нулевая неделя начинается с воскресенья.
from datetime import datetime
def num_of_sundays(year):
    from datetime import datetime
    d = datetime(year, 12, 31)
    return datetime.strftime(d, '%U')


# Вариант
from datetime import date

def num_of_sundays(year):
    days_all = date(year + 1, 1, 1) - date(year, 1, 1)  # отрезок в днях для нужного года
    return (days_all.days + date(year, 1, 1).weekday()) // 7  # (прибавляем порядковый номер дня недели) // 7


#  3.4-07
"""
Продуктивность
https://stepik.org/lesson/570050/step/19?unit=564593
На вход подается дата подготовки первой задачи в формате DD.MM.YYYY
Вывести 10 дат, удовлетворяющих условию задачи, каждую на отдельной строке, в формате DD.MM.YYYY
правило:
    если сегодня подготовил первую задачу, то вторую он должен подготовить через один день
    если сегодня подготовил вторую задачу, то третью он должен подготовить через два дня
    если сегодня подготовил третью задачу, то четвертую он должен подготовить через три дня
и так далее
Input:  20.12.2021
Output: 20.12.2021
        22.12.2021
        25.12.2021
        29.12.2021
        03.01.2022
        09.01.2022
        16.01.2022
        24.01.2022
        02.02.2022
        12.02.2022
"""
from datetime import datetime, timedelta

dt_in = datetime.strptime(input(), '%d.%m.%Y')
delta = timedelta(days=0)

for el in range(2, 12):
    print((dt_in + delta).strftime('%d.%m.%Y'))
    delta += timedelta(days=el)

# Вариант
from datetime import datetime, timedelta

dt_in = datetime.strptime(input(), '%d.%m.%Y')
for el in range(1, 11):
    print(dt_in.strftime('%d.%m.%Y'))
    dt_in += timedelta(days=el + 1)


# Вариант преподавателя
from datetime import datetime, timedelta

pattern = '%d.%m.%Y'
dt = datetime.strptime(input(), pattern) - timedelta(days=1)

for i in range(1, 11):
    dt += timedelta(days=i)
    print(dt.strftime(pattern))


#  3.4-08
"""
Соседние даты
https://stepik.org/lesson/570050/step/20?unit=564593
Input:  06.10.2021 05.10.2021 08.10.2021 09.10.2021 07.10.2021
Output: [1, 3, 1, 2]
"""
from datetime import datetime

ls_date = [datetime.strptime(el, '%d.%m.%Y') for el in input().split(' ')]
res = [abs((ls_date[el] - ls_date[el + 1]).days) for el in range(len(ls_date) - 1)]
print(res)


# Вариант преподавателя
from datetime import datetime

ls_date = [datetime.strptime(el, '%d.%m.%Y') for el in input().split()]
res = [abs(ls_date[el] - ls_date[el - 1]).days for el in range(1, len(ls_date))]
print(res)

# Вариант
from datetime import datetime

ls_date = list(map(lambda el: datetime.strptime(el, '%d.%m.%Y'), input().split()))
print(list(map(lambda x, y: abs(x - y).days, ls_date[1:], ls_date[:-1])))


#  3.4-09
"""
Функция fill_up_missing_dates()
https://stepik.org/lesson/570050/step/21?unit=564593
Input:  dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
Output: ['01.11.2021', '02.11.2021', '03.11.2021', '04.11.2021', '05.11.2021', '06.11.2021', '07.11.2021']
"""
from datetime import date, datetime

def fill_up_missing_dates(dates):
    ls_date = [datetime.strptime(el, '%d.%m.%Y').toordinal() for el in dates]
    start, end = min(ls_date), max(ls_date)
    res = [date.fromordinal(el).strftime('%d.%m.%Y') for el in range(start, end + 1)]
    return res


# Вариант преподавателя
from datetime import date, datetime, timedelta

def fill_up_missing_dates(dates):
    pattern = '%d.%m.%Y'
    ls_date = [datetime.strptime(el, pattern) for el in dates]
    start, end = min(ls_date), max(ls_date)
    days = (end - start).days
    res = [(start + timedelta(days=el)).strftime(pattern) for el in range(days + 1)]
    return res


#  3.4-10
"""
Реп по матеше
https://stepik.org/lesson/570050/step/22?unit=564593
Input:  10:00
        12:35
Output: 10:00 - 10:45
        10:55 - 11:40
        11:50 - 12:35
"""
from datetime import date, datetime, timedelta, time

start = datetime.strptime(input(), '%H:%M')
end = datetime.strptime(input(), '%H:%M')

lesson = timedelta(minutes=45)
relax = timedelta(minutes=10)

# временной интервал для расписания
schedule = end - start

# возможное кол-во занятий (включая перемену)
lessons = (schedule + relax) // (lesson + relax)

for el in range(lessons):
    print(f"{date.strftime(start, '%H:%M')} - {date.strftime(start + lesson, '%H:%M')}")
    start += lesson + relax

