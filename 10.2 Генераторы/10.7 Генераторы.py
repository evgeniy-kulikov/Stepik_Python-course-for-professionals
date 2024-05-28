#  10.7 Генераторы
""""""


"""   *   *   *   Task   *   *   *   """


#  10.7-1
"""
Доступен именованный кортеж Person, который содержит данные о человеке. 
Дополните приведенный ниже код с использованием конвейеров генераторов, 
чтобы он вывел имя и фамилию самого молодого живого (death=0) мужчины (male) из Швеции (Swedish)
"""
from collections import namedtuple

Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])

persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
           Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
           Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
           Person('Genevieve Asse', 'French', 'female', 1949, 0),
           Person('Irene Adler', 'Swedish', 'female', 2005, 0),
           Person('Sergio Asti', 'Italian', 'male', 1926, 0),
           Person('Olof Backman', 'Swedish', 'male', 1999, 0),
           Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
           Person('Dana Atchley', 'American', 'female', 1941, 2000),
           Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
           Person('Shura_Stone', 'Russian', 'male', 2000, 0),
           Person('Jon Bale', 'Swedish', 'male', 2000, 0)]

selector = (i for i in persons if all((i.nationality == 'Swedish', i.death == 0, i.sex == 'male')))
young = max(selector, key=lambda x: x.birth)
print(young.name)

# конвейер генераторов
male = (i for i in persons if i.sex == 'male')
alive = (i for i in male if i.death == 0)
swede = (i for i in alive if i.nationality == 'Swedish')
young = max(swede, key=lambda x: x.birth)
print(young.name)


#  10.7-2
"""
Функция parse_ranges()
Назовем диапазоном запись двух натуральных чисел через дефис a-b, 
где a — левая граница диапазона, b — правая граница диапазона, причем a <= b. 
Диапазон содержит в себе все числа от a до b включительно. 
Например, диапазон 1-4 содержит числа  1, 2, 3 и 4.

Реализуйте генераторную функцию parse_ranges(), которая принимает один аргумент:
ranges — строка, в которой через запятую указаны диапазоны чисел
Функция должна возвращать генератор, порождающий последовательность чисел, содержащихся в диапазонах ranges.
"""
def parse_ranges(ranges: str):
    select = (el.split('-') for el in ranges.split(','))
    res = (range(int(el[0]), int(el[1]) + 1) for el in select)
    return (el for sequence in res for el in sequence)


# Одним выражением
def parse_ranges(ranges):
    return (el
            for select in ranges.split(',')
            for start, end in [select.split('-')]
            for el in range(int(start), int(end) + 1))


# Вариант (не совсем по теме)
def parse_ranges(ranges: str):
    for el in ranges.split(","):
        start, end = map(int, el.split("-"))
        yield from range(start, end + 1)


# ['1', '2'] ['4', '4'] ['8', '10']
# range(1, 3) range(4, 5) range(8, 11)
print(*parse_ranges('1-2,4-4,8-10'))
# 1 2 4 8 9 10


#  10.7-3
"""
Реализуйте генераторную функцию filter_names(), которая принимает три аргумента в следующем порядке:
- names — список имен
- ignore_char — одиночный символ
- max_names — натуральное число

Функция должна возвращать генератор, порождающий max_names имён из списка names, игнорируя имена, которые
* начинаются на ignore_char (в любом регистре)
* содержат хотя бы одну цифру
Если max_names больше количества имен в списке names, 
то генератор должен породить все возможные имена из данного списка. 
"""
def filter_names(names, ignore_char, max_names):
    char = (el for el in names if not el.lower().startswith(ignore_char.lower()))
    digit = (el for el in char if el.isalpha())
    res = (val for idx, val in enumerate(digit) if idx < max_names)
    return res


# Вариант (не совсем по теме)
def filter_names(names, ignore_char, max_names):
    for el in names:
        if el[0].lower() != ignore_char.lower() and el.isalpha() and max_names:
            yield el
            max_names -= 1

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
print(*filter_names(data, 'D', 3))
# Timur Arthur Arina

#  10.7-4
"""
Инвестиции
Доступен файл data.csv, который содержит информацию об инвестициях в различные стартапы. 
В первом столбце записано название компании (стартапа), 
во втором — инвестируемая сумма в долларах, 
в третьем — раунд инвестиции
Напишите программу с использованием конвейеров генераторов, определяющую общую сумму, 
которая была инвестирована в раунде а, и выводящую полученный результат. 

Input:  company,raisedAmt,round
        LifeLock,6850000,b
        LifeLock,6000000,a
        LifeLock,25000000,c
        MyCityFaces,50000,seed
        ...
Output: 4380015000
"""
with open('data.csv', encoding='utf-8') as file:
    file_lines = (line for line in file)
    line_values = (line.rstrip().split(',') for line in file_lines)
    res = sum(int(el[1]) for el in line_values if el[2] == 'a')
print(res)
# 4380015000

# Вариант
import csv
with open('data.csv', encoding='utf-8') as file:
    line_values = csv.reader(file)
    res = sum(int(el[1]) for el in line_values if el[2] == 'a')
print(res)
# 4380015000


#  10.7-5
"""
Реализуйте генераторную функцию years_days(), которая принимает один аргумент:
year — натуральное число
Функция должна возвращать генератор, порождающий последовательность всех дат (тип date) в году year.
"""
from datetime import date, timedelta
def years_days(year):
    data = date(year, 1, 1)
    while data.year == year:
        yield data
        data += timedelta(hours=24)


# Хорошее решение
from datetime import date, timedelta
from calendar import isleap

def years_days(year):
    days = 365 + isleap(year)
    return (date(year, 1, 1) + timedelta(days=i) for i in range(days))



dates = years_days(2022)
print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))
# 2022-01-01
# 2022-01-02
# 2022-01-03
# 2022-01-04


#  10.7-6
"""
Реализуйте генераторную функцию nonempty_lines(), которая принимает один аргумент:
file — название текстового файла, например, data.txt
Функция должна возвращать генератор, порождающий последовательность всех непустых строк файла file 
с убранным символом переноса строки \n. 
Если строка содержит более 25 символов, она заменяется многоточием ....
"""
def nonempty_lines(file):
    with open(file, encoding='utf-8') as f:
        lines_in = (line.strip() for line in f)
        lines_full = (line for line in lines_in if line)
        lines_crop = (line if len(line) <= 25 else '...' for line in lines_full)
        yield from lines_crop


# readlines() - дает список. Это плохо
def nonempty_lines(file):
    with open(file, encoding='utf-8') as f:
        return (line.strip() if len(line) <= 25
                else '...'
                for line in f.readlines() if line.strip())


lines = nonempty_lines('file1.txt')
print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))
# bee
# geek
# stepik
# aaaaaaaaaaaaaaaaaaaaaaaaa


#  10.7-7
"""
https://stepik.org/lesson/673155/step/11?unit=671418
Функция txt_to_dict()
Реализуйте генераторную функцию txt_to_dict(), которая не принимает никаких аргументов.
Функция должна возвращать генератор, порождающий последовательность словарей, 
каждый из которых содержит информацию об очередной планете из файла planets.txt
{'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}
"""
def txt_to_dict():
    with open('planets.txt', encoding='utf-8') as file:
        lines_in = (el.strip() for el in file)
        planet = dict()
        for el in lines_in:
            if el:
                planet.update(dict([el.split(' = ')]))
            else:
                yield planet
                planet = dict()
        yield planet


# Вариант
def txt_to_dict():
    with open('planets.txt', encoding='utf-8') as file:
        lines_in = (el.strip() for el in file)
        planet = dict()
        for el in lines_in:
            if el:
                k, v = el.split(' = ')
                planet[k] = v
            else:
                yield planet
                planet = dict()
        yield planet

# Нестандартное решение
'''
Если вместо фильтрующей функции func передать значение None, 
то каждый элемент последовательности будет проверен на соответствие значению True. 
Если элемент в логическом контексте возвращает значение False, 
то он не будет добавлен в результирующий итератор.
'''
def txt_to_dict():
    with open('planets.txt', encoding='utf-8') as file:
        fl_lines = filter(None, map(str.rstrip, file))  # Убираем пустые строки
        planets = zip(*[fl_lines] * 4)  # кортеж с четырьмя элементами из генераторов
        # ('Name = Mercury', 'Diameter = 4879.4', 'Mass = 3.302×10^23', 'OrbitalPeriod = 0.241')
        yield from (dict(el.split(' = ') for el in item) for item in planets)


planets = txt_to_dict()
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))

# planets = txt_to_dict()
print(*planets)


#  10.7-8
"""
Реализуйте генераторную функцию unique(), которая принимает один аргумент:
iterable — итерируемый объект
Функция должна возвращать генератор, 
порождающий последовательность элементов итерируемого объекта iterable без дубликатов.
"""
# Хорошее решение
def unique(iterable):
    yield from dict.fromkeys(iterable)
    # yield from {el: None for el in iterable}


# Примитивное решение
def unique(iterable):
    res = []
    [res.append(el) for el in iterable if el not in res]
    yield from res


# Вариант
def unique(iterable):
    res = set()
    for el in iterable:
        if el not in res:
            yield el
            res.add(el)


numbers = [1, 2, 2, 3, 4, 5, 5, 5]
print(*unique(numbers))
# 1 2 3 4 5

data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')
print(*unique(data))
# J H F G S K D R I Y T E O W P Q L M N B V C X A


#  10.7-9
"""
Реализуйте генераторную функцию stop_on(), которая принимает два аргумента в следующем порядке:
iterable — итерируемый объект
obj — произвольный объект
Функция должна возвращать генератор, 
порождающий последовательность элементов итерируемого объекта iterable до тех пор, 
пока не будет достигнут элемент, равный obj. 
Если итерируемый объект iterable не содержит ни одного элемента, равного obj, 
генератор должен породить все элементы iterable.
"""
def stop_on(iterable, obj):
    for el in iterable:
        if el == obj:
            break
        yield el

# Хорошее решение
def stop_on(iterable, obj):
    it = iter(iterable)
    return iter(lambda: next(it), obj)  # второй аргумент в iter(source, sentinel=None) останавливает итератор

# Нестандартное решение
stop_on = lambda iterable, obj: iter(iter(iterable).__next__, obj)


numbers = [1, 2, 3, 4, 5]
print(*stop_on(numbers, 4))
# 1 2 3

iterator = iter('beegeek')
print(*stop_on(iterator, 'a'))
# b e e g e e k


#  10.7-10
"""
Реализуйте генераторную функцию with_previous(), которая принимает один аргумент:
iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность кортежей, 
каждый из которых содержит очередной элемент итерируемого объекта iterable, а также предшествующий ему элемент:
(<очередной элемент>, <предыдущий элемент>)
Для первого элемента предыдущим считается значение None.
"""
def with_previous(iterable):
    prev = None
    for el in iterable:
        yield el, prev
        prev = el


numbers = [1, 2, 3, 4, 5]
print(*with_previous(numbers))
# (1, None) (2, 1) (3, 2) (4, 3) (5, 4)


iterator = iter('stepik')
print(*with_previous(iterator))
# ('s', None) ('t', 's') ('e', 't') ('p', 'e') ('i', 'p') ('k', 'i')


#  10.7-11
"""
Реализуйте генераторную функцию pairwise(), которая принимает один аргумент:
iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность кортежей, 
каждый из которых содержит очередной элемент итерируемого объекта iterable, а также следующий за ним элемент:
(<очередной элемент>, <следующий элемент>)
Для последнего элемента следующим считается значение None
"""
def pairwise(iterable):
    data = iter(iterable)
    current = next(data, None)
    while current is not None:
        current, follow = next(data, None), current
        yield follow, current


numbers = [1, 2, 3, 4, 5]
print(*pairwise(numbers))
# # (1, 2) (2, 3) (3, 4) (4, 5) (5, None)

iterator = iter('stepik')
print(*pairwise(iterator))
# ('s', 't') ('t', 'e') ('e', 'p') ('p', 'i') ('i', 'k') ('k', None)


#  10.7-12
"""
Реализуйте генераторную функцию around(), которая принимает один аргумент:
iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность кортежей, 
каждый из которых содержит очередной элемент итерируемого объекта iterable, 
а также предыдущий и следующий за ним элементы:
(<предыдущий элемент>, <очередной элемент>, <следующий элемент>)
Для первого элемента предыдущим считается значение None, 
для последнего элемента следующим считается так же значение None
"""
def around(iterable):
    data = iter(iterable)
    prev = None
    current = next(data, None)
    foll = next(data, None)

    while current is not None:
        yield prev, current, foll
        prev, current, foll = current, foll, next(data, None)


# Неудачное решение
def around(iterable):
    it = tuple(iterable)  # теряется смысл генераторов
    yield from zip((None, *it), it, (*it[1:], None))


numbers = [1, 2, 3, 4, 5]
print(*around(numbers))
# (None, 1, 2) (1, 2, 3) (2, 3, 4) (3, 4, 5) (4, 5, None)

iterator = iter('hey')
print(*around(iterator))
# (None, 'h', 'e') ('h', 'e', 'y') ('e', 'y', None)

print(list(around(set())))  # []
print(around({}))  # <generator object around at 0x00000269A89DFF40>
