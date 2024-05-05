# 8.4 Рекурсия
""""""

# Рекурсивный обход коллекций

"""
Задача 1. 
Дан список, элементами которого могут быть только строки или аналогичные списки, 
содержащие строки и вложенные списки. 
Необходимо вывести все строки из данного списка и из всех вложенных, 
разделив пробелом.
"""
def get_all_str(data):
    if type(data) == str:
        print(data, end=' ')            # базовый случай
    if type(data) == list:
        for i in data:
            get_all_str(i)              # рекурсивный случай

numbers = ['1', ['2', '3', ['4'], ['5', ['6', '7']]]]
get_all_str(numbers)
# 1 2 3 4 5 6 7


"""
Задача 2. 
Дан словарь произвольной вложенности, то есть значениями в словаре могут быть другие словари. 
Необходимо определить значение, которое соответствует заданному ключу, и вернуть его. 
При этом гарантируется, что такой ключ имеется в словаре, причем он единственный. 
"""


def find_key(data, key):
    if key in data:
        return data[key]  # базовый случай

    for v in data.values():
        if type(v) == dict:
            value = find_key(v, key)  # рекурсивный случай
            if value is not None:
                return value

info = {'name': 'Alyson',
        'surname': 'Hannigan',
        'birthday': {'day': 24, 'month': 'March', 'year': 1974},
        'family': {'parents': {'mother': 'Emilie Posner', 'father': 'Alan Hannigan'}}}

print(find_key(info, 'year'))       # 1974
print(find_key(info, 'father'))     # Alan Hannigan


# Настройка глубины рекурсии в Python

# Получить значение по умолчанию для максимальной глубины рекурсии можно
# с помощью функции getrecursionlimit() из модуля sys
from sys import getrecursionlimit

limit = getrecursionlimit()
print(limit)  # 1000


# Можно явно установить значение максимальной глубины рекурсии.
# Для этого используется функция setrecursionlimit() из модуля sys
import sys

limit = sys.getrecursionlimit()
print(limit)        # 1000

sys.setrecursionlimit(6000)
new_limit = sys.getrecursionlimit()
print(new_limit)        # 6000


"""   *   *   *   Task   *   *   *   """


#  8.4-1
"""
Функция recursive_sum()
Реализуйте recursive_sum() с использованием рекурсии, которая принимает один аргумент:
nested_lists — список, элементами которого являются целые числа или списки, 
элементами которых, в свою очередь, также являются либо целые числа, либо списки; 
вложенность может быть произвольной

Функция должна вычислять сумму всех чисел во всех списках и возвращать полученный результат. 
Если список nested_lists пуст, функция должна вернуть число  0

Input:  my_list = [1, [4, 4], 2, [1, [2, 10]]]
        print(recursive_sum(my_list))
Output: 24
"""
def recursive_sum(data):
    cnt = 0
    if type(data) == int:
        cnt += data
    if type(data) == list:
        for el in data:
            cnt += recursive_sum(el)
    return cnt

my_list = [1, [4, 4], 2, [1, [2, 10]]]
# my_list = [[], [[]]]
print(recursive_sum(my_list))


#  8.4-2
"""
Функция linear()
Линеаризация — это процесс преобразования списка, 
который может содержать несколько уровней вложенных списков, 
в список, содержащий все те же элементы без какой-либо вложенности:
[1, [2, 3], [4, [5, 6, [7, 8, 9]]]]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

Реализуйте linear() с использованием рекурсии, которая принимает один аргумент:
nested_lists — список, элементами которого являются целые числа или списки, 
элементами которых, в свою очередь, также являются либо целые числа, либо списки; 
вложенность может быть произвольной
Функция должна возвращать новый список, 
представляющий собой линеаризованный список nested_lists
Input:  my_list = [3, [4], [5, [6, [7, 8]]]]
        print(linear(my_list))
Output: [3, 4, 5, 6, 7, 8]
"""
def linear(ls: list):
    res = []
    if type(ls) == int:
        res += [ls]
    elif type(ls) == list:
        for el in ls:
            res += linear(el)
    return res

my_list = [3, [4], [5, [6, [7, 8]]]]
print(linear(my_list))


#  8.4-3
"""
Реализуйте функцию get_value(), которая принимает два аргумента в следующем порядке:

- nested_dicts — словарь, содержащий в качестве значений произвольные объекты или словари, 
  которые, в свою очередь, так же содержат в качестве значений произвольные объекты или словари; 
  вложенность может быть произвольной
- key — хешируемый объект

Функция должна определять значение, 
которое соответствует ключу key в словаре nested_dicts или в одном из его вложенных словарей, 
и возвращать полученный результат.
Input:  data = {'first_name': 'Tom', 'last_name': 'Cruise', 'birthday': {'day': 24, 'month': 'May', 'year': 1974}}
        print(get_value(data, 'birthday'))
Output: {'day': 24, 'month': 'May', 'year': 1974}
"""


def get_value(dt: dict, key):
    if key in dt:
        return dt[key]  # базовый случай

    for el in dt.values():
        if type(el) == dict:
            val = get_value(el, key)  # рекурсивный случай
            if val is not None:
                return val


data = {'first_name': 'Tom', 'last_name': 'Cruise', 'birthday': {'day': 24, 'month': 'May', 'year': 1974}}
print(get_value(data, 'birthday'))

