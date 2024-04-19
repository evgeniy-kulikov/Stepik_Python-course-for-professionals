# 6.3 Тип данных namedtuple
""""""

"""
Python содержит встроенный модуль collections, 
который содержит специализированные типы коллекций, 
альтернативных традиционным list, tuple, dict:

- namedtuple
- defaultdict
- OrderedDict
- Counter
- ChainMap
- deque

Именованные кортежи (тип namedtuple) — это подтип обычных кортежей в Python. 
У них те же функции, что и у обычных, 
но их значения можно получать как с помощью индекса (например, [0]), 
так и с помощью имени через точку (например, .name).
"""

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])     # объявляем тип Point именованного кортежа
point = Point(3, 7)                         # создаем именованный кортеж Point

print(point)                # Point(x=3, y=7)
print(point.x, point.y)     # 3 7
print(point[0], point[1])   # 3 7
print(type(point))          # <class '__main__.Point'>

"""
Важно отметить, что, хотя кортежи и именованные кортежи неизменяемы, 
сохраняемые в них значения не обязательно должны быть неизменяемыми. 
Можно создать кортеж или именованный кортеж, содержащий изменяемые значения.
"""
from collections import namedtuple

Person = namedtuple('Person', ['name1', 'name2'])
band = Person('The Beatles', ['Ringo', 'Paul'])

print(band)     # Person(name='The Beatles', member=['Ringo', 'Paul'])

band.name2.append('George')
print(band)     # Person(name='The Beatles', member=['Ringo', 'Paul', 'George'])

"""
Функция namedtuple() выступает в роли фабричной функции, порождающей новые типы данных.

Сигнатура данной функции имеет вид: 
namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
То есть функция принимает два обязательных параметра typename и field_names 
и три необязательных rename, defaults, module
"""


"""   *   *   *   Task   *   *   *   """


#  6.4-1
"""
"""
from collections import namedtuple

Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])


#  6.4-2
"""
Доступен именованный кортеж Game. 
Создать именованный кортеж типа ExtendedGame, 
имеющий те же поля, что и Game, а также два дополнительных поля — release_date и price.
"""
from collections import namedtuple

Game = namedtuple('Game', 'name developer publisher')

ExtendedGame = namedtuple('ExtendedGame', [*Game._fields, 'release_date', 'price'])
# ExtendedGame = namedtuple('ExtendedGame', [*Game._fields] + ['release_date', 'price'])
# ExtendedGame = namedtuple('ExtendedGame', 'name developer publisher release_date price')


#  6.4-3
"""
https://stepik.org/lesson/740203/step/10?thread=solutions&unit=741843
"""
import pickle
from collections import namedtuple

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    for el in pickle.load(file):
        for key, value in zip(el._fields, el):
            print(f'{key}: {value}')
        print()


with open('data.pkl', 'rb') as file:
    obj = pickle.load(file)
    # [Animal(name='Alex', family='dogs', sex='m', color='brown'),
    # Animal(name='Nancy', family='cats', sex='w', color='white'),
    # ...
    # Animal(name='Chip', family='hedgehogs', sex='m', color='white')]

    for el in obj:
        print(f"name: {el.name}\n"
              f"family: {el.family}\n"
              f"sex: {el.sex}\n"
              f"color: {el.color}\n")


#  6.4-4
"""
https://stepik.org/lesson/740203/step/11?unit=741843
"""
from collections import namedtuple

User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

plans = ['Gold', 'Silver', 'Bronze', 'Basic']

# users.sort(key=lambda x: (plans.index(x.plan), x.email))

for el in sorted(users, key=lambda x: (plans.index(x.plan), x.email)):
    print(f"{el.name} {el.surname}\n"
          f"  Email: {el.email}\n"
          f"  Plan: {el.plan}\n")


#  6.4-5
"""
https://stepik.org/lesson/740203/step/12?unit=741843
Input:  *
Output: *
"""
from collections import namedtuple
import csv
from datetime import datetime

with open('meetings.csv', encoding='u8') as fi:
    data = csv.DictReader(fi)
    User = namedtuple('User', data.fieldnames)
    users = [User(**el) for el in data]

# with open('meetings.csv', encoding='utf-8') as file:
#     data = csv.reader(file)
#     User = namedtuple('User', next(data))
#     users = [User._make(el) for el in data]

with open('meetings.csv', encoding='u8') as fi:
    data = csv.DictReader(fi)
    User = namedtuple('User', data.fieldnames)
    users = [User(**el) for el in data]

    users.sort(key=lambda x: datetime.strptime(f'{x.meeting_date} {x.meeting_time}', '%d.%m.%Y %H:%M'))

    for el in users:
        print(el.surname, el.name)



