#  3.5 Решение задач
""""""

""""""
"""   *   *   *   Task   *   *   *   """
""""""


#  3.5-01
"""
Во время решения очередной задачи программист фиксирует время начала и окончания ее решения 
и добавляет полученные результаты в список data. 
Каждый результат представляет собой кортеж, 
первым элементом которого является время начала решения в виде строки в формате HH:MM, 
вторым элементом — время окончания решения в виде строки в том же формате. 
Вывести общее целое количество минут, которое программист затратил на решение всех задач.
Input:  data
Output: 545
"""
# from datetime import date, datetime, timedelta, time

from datetime import date, datetime, timedelta, time

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

res = timedelta(seconds=0)
for el in data:
    res += datetime.strptime(el[1], '%H:%M') - datetime.strptime(el[0], '%H:%M')
print(res.seconds // 60)  # 545

# Вариант преподавателя
res = 0
for el in data:
    start, end = [datetime.strptime(x, '%H:%M') for x in el]
    res += (end - start).total_seconds()
print(int(res // 60))  # 545
# print(seconds // 60)  # 545.0

# Вариант
res = [(datetime.strptime(el[1], '%H:%M') - datetime.strptime(el[0], '%H:%M')).seconds for el in data]
print(sum(res) // 60)  # 545


#  3.5-02
"""
Докажите, что 13-е число месяца чаще всего приходится на пятницу. 
Напишите программу, которая вычисляет, 
сколько тринадцатых чисел приходится на каждый день недели в период с 01.01.0001 по 31.12.9999
Программа должна вывести 7 чисел — количество тринадцатых чисел, которые приходятся на 
понедельник, вторник, среду, четверг, пятницу, субботу и воскресенье в период с 01.01.0001 по 31.12.9999
Output: 17123  17124  17173  17097  17199  17099  17173
"""
from datetime import date, timedelta

d_res = dict()
start = date.min
td = timedelta(days=1)

for el in range((date.max - date.min).days):
    if start.day == 13:
        d_res.setdefault(start.weekday(), 0)
        d_res[start.weekday()] += 1
    start += td

# d_res = {5: 17099, 1: 17124, 4: 17199, 6: 17173, 2: 17173, 0: 17123, 3: 17097}
res = [el for el in d_res.items()]
res.sort()
for el in res:
    print(el[1])


# Хорошее решение
from datetime import date

count = [0, 0, 0, 0, 0, 0, 0]

for years in range(1, 10000):
    for months in range(1, 13):
        count[date(years, months, 13).weekday()] += 1

print(*count, sep='\n')

#  3.5-03
"""
Снова не успел
https://stepik.org/lesson/571244/step/3?unit=565785
На вход подаются текущие дата и время в формате DD.MM.YYYY HH:MM.
Вывести количество минут, которое осталось до закрытия магазина, 
или текст Магазин не работает, если он закрыт.
Input:  01.11.2021 20:45
Output: 15
"""

from datetime import date, datetime, time, timedelta

def get_time(start, end):
    if start <= dt_in.time().hour < end:
        res = (datetime.combine(date(1, 1, 1), time(hour=end)) - dt_in).seconds // 60
        # td = timedelta(hours=dt_in.hour, minutes=dt_in.minute)  # через timedelta
        # res = int((timedelta(hours=21) - td).total_seconds() // 60)
    else:
        res = 'Магазин не работает'
    return res

dt_in = datetime.strptime(input(), '%d.%m.%Y %H:%M')

if dt_in.weekday() in [5, 6]:
    print(get_time(10, 18))
else:
    print(get_time(9, 21))


# Вариант
from datetime import date, time, datetime

def get_time(date):
    if date.weekday() in (5, 6):
        start, end = date.replace(hour=10, minute=0), date.replace(hour=18, minute=0)
    else:
        start, end = date.replace(hour=9, minute=0), date.replace(hour=21, minute=0)

    if start <= date < end:
        return int((end - date).total_seconds() // 60)
    else:
        return 'Магазин не работает'

dt_in = datetime.strptime(input(), '%d.%m.%Y %H:%M')
print(get_time(dt_in))


#  3.5-04
"""
Самое понятное условие
https://stepik.org/lesson/571244/step/4?unit=565785
Даны две даты — левая и правая границы диапазона соответственно. 
Напишите программу, которая из этого диапазона, включая границы, выводит, начиная с даты, 
у которой сумма дня и месяца нечетная, каждую третью дату, только если она не понедельник и не четверг.
Гарантируется, что первая дата не больше второй.
Input:  06.11.2021
        27.11.2021
Output: 06.11.2021
        09.11.2021
        12.11.2021
        21.11.2021
        24.11.2021
        27.11.2021
"""
from datetime import date, datetime, timedelta

start = datetime.strptime(input(), '%d.%m.%Y')
end = datetime.strptime(input(), '%d.%m.%Y')

# Находим стартовую дату.
for el in range(start.toordinal(), end.toordinal() + 1):
    if (date.fromordinal(el).month + date.fromordinal(el).day) % 2 != 0:
        start = date.fromordinal(el)
        break

# Находим стартовую дату (хороший вариант).
# while not (start.month + start.day) % 2:
#     start += timedelta(days=1)

for el in range(start.toordinal(), end.toordinal() + 1, 3):
    if date.fromordinal(el).weekday() not in (0, 3):
        print(date.fromordinal(el).strftime('%d.%m.%Y'))


#  3.5-05
"""
Сотрудники организации
https://stepik.org/lesson/571244/step/5?unit=565785
Определить самого старшего сотрудника из списка.

На вход программе в первой строке подается натуральное число n — количество сотрудников, работающих в организации. 
В последующих n строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом. 
Дата рождения указывается в формате DD.MM.YYYY
Определить самого старшего сотрудника и вывести его дату рождения, имя и фамилию, разделив пробелом. 
Если таких сотрудников несколько, программа должна вывести их дату рождения, а также их количество, разделив пробелом.
Гарантируется, что у всех сотрудников имена и фамилии различны.
Input:  3
        Иван Петров 01.05.1995
        Петр Сергеев 29.04.1995
        Сергей Иванов 01.01.1996
Output: 29.04.1995 Петр Сергеев

Input:  3
        Иван Петров 01.05.1995
        Петр Сергеев 29.05.1995
        Сергей Иванов 01.05.1995
Output: 01.05.1995 2
"""
from datetime import datetime

def get_data(data: str):
    dt = datetime.strptime(data[-10:], '%d.%m.%Y')
    user = data[:-11]
    return dt, user

lst = sorted([get_data(input()) for _ in range(int(input()))])
# lst = [(datetime(1995, 4, 29, 0, 0), 'Петр Сергеев'), (datetime(1995, 5, 1, 0, 0), 'Иван Петров'),
#        (datetime(1996, 1, 1, 0, 0), 'Сергей Иванов')]

cnt, first = -1, lst[0][0]
for el in lst:
    if el[0] == first:
        cnt += 1

if not cnt:
    print(lst[0][0].strftime('%d.%m.%Y'), lst[0][1])
else:
    print(lst[0][0].strftime('%d.%m.%Y'), cnt + 1)


# Вариант
from datetime import datetime

data = dict()
youngest = datetime.max  # datetime(9999, 12, 31, 23, 59, 59, 999999)

for _ in range(int(input())):
    *name, birthday = input().split()
    name, birthday = ' '.join(name), datetime.strptime(birthday, '%d.%m.%Y')
    if birthday < youngest:
        youngest = birthday  # определение наименьшей даты
    data[name] = birthday  # словарь из входных данных

oldest = [name for name, birthday in data.items() if birthday == youngest]

if len(oldest) > 1:
    print(youngest.strftime('%d.%m.%Y'), len(oldest))
else:
    print(youngest.strftime('%d.%m.%Y'), oldest[0])

# Хорошее решение
from datetime import datetime

data = [tuple(input().rsplit(' ', 1)) for _ in range(int(input()))]

oldest = min(data, key=lambda x: datetime.strptime(x[1], '%d.%m.%Y'))

result = list(filter(lambda x: x[1] == oldest[1], data))

if len(result) > 1:
    print(oldest[1], len(result))
else:
    print(*oldest[::-1])  # переворот кортежа



#  3.5-06
"""
Сотрудники организации 2
https://stepik.org/lesson/571244/step/6?unit=565785
Определить в какую из дат родилось больше всего сотрудников из списка.

На вход программе в первой строке подается натуральное число n — количество сотрудников, работающих в организации. 
В последующих n строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом. 
Дата рождения указывается в формате DD.MM.YYYY
Если таких дат несколько, программа должна вывести их все в порядке возрастания, 
каждую на отдельной строке, в том же формате.
Input:  5
        Иван Петров 01.05.1995
        Петр Сергеев 29.04.1995
        Сергей Романов 01.01.1996
        Роман Григорьев 01.01.1996
        Григорий Иванов 01.05.1995
Output: 01.05.1995
        01.01.1996
"""
from datetime import datetime

lst = [datetime.strptime(input()[-10:], '%d.%m.%Y') for _ in range(int(input()))]
# lst = [datetime(1995, 5, 1, 0, 0), datetime(1995, 4, 29, 0, 0), datetime(1996, 1, 1, 0, 0),
#         datetime(1996, 1, 1, 0, 0), datetime(1995, 5, 1, 0, 0)]

dt = dict()

for el in lst:
    dt[el] = dt.setdefault(el, 0) + 1


res = sorted([(v, k) for k, v in dt.items()])
# res = [(1, datetime(1995, 4, 29, 0, 0)), (2, datetime(1995, 5, 1, 0, 0)), (2, datetime(1996, 1, 1, 0, 0))]

if res[0][0] == res[-1][0]:  # все первые значения кортежей одинаковы
    [print(el[1].strftime('%d.%m.%Y')) for el in res]
else:  # выводим те, у которых первые значения кортежей равны первому значению последнего кортежа
    [print(el[1].strftime('%d.%m.%Y')) for el in res if el[0] == res[-1][0]]


# Короче
from datetime import datetime

dt = dict()
for _ in range(int(input())):
    name, date = input().rsplit(maxsplit=1)
    dt[datetime.strptime(date, '%d.%m.%Y')] = dt.get(datetime.strptime(date, '%d.%m.%Y'), 0) + 1

[print(el.strftime('%d.%m.%Y')) for el in filter(lambda x: dt[x] == max(dt.values()), sorted(dt))]


#  3.5-07
"""
Сотрудники организации 
https://stepik.org/lesson/571244/step/7?unit=565785
Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. 
Определить самого молодого сотрудника, празднующего свой день рождения в течение ближайших 7 дней от текущей даты.

На вход программе в первой строке подается:
текущая дата в формате DD.MM.YYYY.
натуральное число n — количество сотрудников, работающих в организации. 
В последующих n строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом. 
Дата рождения указывается в формате DD.MM.YYYY

Вывести имя и фамилию, разделив пробелом. Если таких сотрудников нет, программа должна вывести:
"Дни рождения не планируются"
Гарантируется, что у всех сотрудников даты рождения различны.
Input:  29.12.2021
        4
        Иван Петров 30.12.1995
        Петр Сергеев 04.01.1997
        Сергей Романов 03.01.1994
        Маша Иванова 31.12.1996
Output: Петр Сергеев
"""
from datetime import datetime, timedelta

data_in = datetime.strptime(input(), '%d.%m.%Y')
day_in, month_in = set(), set()

for el in range(1, 8):
    day_in.add((data_in + timedelta(days=el)).day)
    month_in.add((data_in + timedelta(days=el)).month)

def data_name(data: str):
    name, birthday = data.rsplit(maxsplit=1)
    birthday = datetime.strptime(birthday, '%d.%m.%Y')
    return birthday, name

def get_user(data: datetime):
    return data.day in day_in and data.month in month_in

lst_in = [data_name(input()) for _ in range(int(input()))]
res = [el for el in lst_in if get_user(el[0])]
res.sort(reverse=True)

print(res[0][1] if res else 'Дни рождения не планируются')


# Вариант с использованием метода data.replace(year=...)
from datetime import datetime, timedelta

d_in = datetime.strptime(input(), '%d.%m.%Y')
d_ls = [d_in + timedelta(days=el) for el in range(1, 8)]

def data_name(data: str):
    name, dt = data.rsplit(maxsplit=1)
    dt = datetime.strptime(dt, '%d.%m.%Y')
    return dt, name

def get_user(data: datetime):
    if data.month == 1 and data.day in (1, 2, 3, 4, 5, 6, 7):
        data = data.replace(year=d_in.year + 1)  # увеличиваем год для первых 7 дней января
    else:
        data = data.replace(year=d_in.year)
    if data in d_ls:
        return True

lst_in = [data_name(input()) for _ in range(int(input()))]
res = [el for el in lst_in if get_user(el[0])]
res.sort(reverse=True)

print(res[0][1] if res else 'Дни рождения не планируются')

# Вариант короче (иногда даты как строки вида "31.12", иногда как datetime)
from datetime import datetime, timedelta

d_in = datetime.strptime(input(), '%d.%m.%Y')
d_ls = [(d_in + timedelta(i)).strftime('%d.%m.%Y')[:5] for i in range(1, 8)]
user_ls = [input().rsplit(' ', 1) for _ in range(int(input()))]  # сотрудники
res = list(filter(lambda x: x[1][:5] in d_ls, user_ls))  # сотрудники у которых д/р на неделе
if res:
    young = max(res, key=lambda x: datetime.strptime(x[1], '%d.%m.%Y'))  # младший сотрудник
    print(young[0])
else:
    print('Дни рождения не планируются')


#  3.5-08
"""
FAKE NEWS
https://stepik.org/lesson/571244/step/8?unit=565785
Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00. 
Напишите программу, которая принимает на вход текущие дату и время и определяет, 
сколько времени осталось до выхода курса.
Input:  16.11.2021 06:30
Output: До выхода курса осталось: 357 дней и 5 часов

Input:  08.11.2022 12:15
Output: Курс уже вышел!
"""
from datetime import datetime

def get_plural(amount: int, unit: int) -> str:
    word = [['день', 'дня', 'дней'],
          ['час', 'часа', 'часов'],
          ['минута', 'минуты', 'минут']]
    one, dual = amount % 10, amount % 100
    if one == 1 and dual != 11:
        return word[unit][0]
    elif one in (2, 3, 4) and dual not in (12, 13, 14):
        return word[unit][1]
    return word[unit][2]

release = datetime(2022, 11, 8, 12)
current = datetime.strptime(input(), '%d.%m.%Y %H:%M')
# current = datetime(2022, 10, 7, 11, 55)
line = 'До выхода курса осталось:'

d = (release - current).days
h = (release - current).seconds // 3600
m = (release - current).seconds % 3600 // 60

if release.timestamp() - current.timestamp() > 0:
    if d:
        if h:
            print(f'{line} {d} {get_plural(d, 0)} и {h} {get_plural(h, 1)}')
        else:
            print(f'{line} {d} {get_plural(d, 0)}')
    else:
        if h:
            if m:
                print(f'{line} {h} {get_plural(h, 1)} и {m} {get_plural(m, 2)}')
            else:
                print(f'{line} {h} {get_plural(h, 1)}')
        else:
            print(f'{line} {m} {get_plural(m, 2)}')
else:
    print('Курс уже вышел!')


# Последний блок if короче
from datetime import datetime

def get_plural(amount: int, unit: int) -> str:
    word = [['день', 'дня', 'дней'],
          ['час', 'часа', 'часов'],
          ['минута', 'минуты', 'минут']]
    one, dual = amount % 10, amount % 100
    if one == 1 and dual != 11:
        return word[unit][0]
    elif one in (2, 3, 4) and dual not in (12, 13, 14):
        return word[unit][1]
    return word[unit][2]

release = datetime(2022, 11, 8, 12)
current = datetime.strptime(input(), '%d.%m.%Y %H:%M')

if release.timestamp() - current.timestamp() > 0:
    d = (release - current).days
    h = (release - current).seconds // 3600
    m = (release - current).seconds % 3600 // 60
    print('До выхода курса осталось:', end='')
    if d:
        print(f' {d} {get_plural(d, 0)}', end='')
    if h:
        print(f'{" и" * (d > 0)} {h} {get_plural(h, 1)}', end='')
    if m and not d:
        print(f'{" и" * (h > 0)} {m} {get_plural(m, 2)}')
else:
    print('Курс уже вышел!')

