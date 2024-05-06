#  9.2 Встроенные функции
""""""

# Функция eval()
"""
Функция eval() выполняет строку-выражение, переданную ей в качестве обязательного аргумента, 
и возвращает результат выполнения этой строки. 
Аргумент функции:
expression — строка-выражение, которую требуется исполнить.

Выражения, передаваемые в качестве аргумента функции eval(), 
имеют доступ ко всем встроенным функциям Python.

Но не все языковые конструкции являются выражениями (expression). 
Операторами, которые нельзя использовать в качестве выражений, являются, например:
while, for, if, def, import, class, raise и т.д.
"""
expression = '7 + 10'
result = eval(expression)

print(type(result))     # <class 'int'>
print(result)           # 17


num = 17
eval('if num == 10: print(num)')  # SyntaxError: invalid syntax


#  С помощью функции eval() можно парсить объекты,
#  то есть преобразовывать из строки в реальные Python объекты.
list_data = eval("['Python', 'C#', 'Java']")
tuple_data = eval('(1, 2, 3, 4, 5)')
dict_data = eval("{1: 'January', 2: 'February'}")


# Функция exec()
"""
Функция exec(), в отличие от eval(), принимает блок кода и выполняет его, возвращая значение None. 
Аргумент функции:
code — строка, представляющая собой корректный блок кода

!!!  функция exec() именно выполняет переданный блок кода и всегда возвращает значение None

Блок кода, передаваемый в качестве аргумента функции exec(), 
имеет доступ ко всем встроенным функциям Python.
"""
code = '''a = 10
b = 20
print(a + b)'''
exec(code)  # 30


code = '100 + 10*7 - 14'
result = exec(code)
print(result)  # None


"""   *   *   *   Task   *   *   *   """


#  9.2-1
"""
hash_as_key()
Реализуйте функцию hash_as_key(), которая принимает один аргумент:
objects — список хешируемых объектов
Функция должна возвращать словарь, ключом в котором является хеш-значение объекта из списка objects, 
а значением — сам объект. Если хеш-значения некоторых объектов совпадают, их следует объединить в список.
"""
from collections import defaultdict

def hash_as_key(obj: list):
    dt = defaultdict(list)
    for el in obj:
        dt[hash(el)] += [el]
    for el in dt:
        if len(dt[el]) == 1:
            dt[el] = dt[el][0]
    return dict(dt)


# Без defaultdict
def hash_as_key(obj: list):
    dt = dict()
    for el in obj:
        dt[hash(el)] = dt.get(hash(el), []) + [el]
    for el in dt:
        if len(dt[el]) == 1:
            dt[el] = dt[el][0]
    return dt

data = [-1, -2, -3, -4, -5]
print(hash_as_key(data))


#  9.2-2
"""
Напишите программу, которая принимает на вход 
корректный непустой список, корректный непустой кортеж или корректное множество произвольной длины, 
и выполняет следующее:
- если введен список, выводит его последний элемент
- если введен кортеж, выводит его первый элемент
- если введено множество, выводит количество его элементов
"""
data = eval(input())

if isinstance(data, list):
    print(data[-1])
elif isinstance(data, tuple):
    print(data[0])
else:
    print(len(data))


# Нестандартное решение
dt = {list: 'data[-1]', tuple: 'data[0]', set: 'len(data)'}
data = eval(input())
print(eval(dt[type(data)]))


#  9.2-3
"""
Математические выражения
Напишите программу, которая принимает на вход произвольное количество строк, 
содержащих корректные математические выражения, и выводит значение наибольшего из них.
Input:  1 + 2 + 3
        2 * 8
        10 * 10 - 1
Output: 99
"""
import sys

data = [eval(el.strip()) for el in sys.stdin]
print(max(data))

# Короче
print(max(eval(el.strip()) for el in sys.stdin))


#  9.2-4
"""
Минимум и максимум
https://stepik.org/lesson/645394/step/22?unit=641995
Input:  2*x**2 + 5*x + 7
        -1 5
Output: Минимальное значение функции 2*x**2 + 5*x + 7 на отрезке [-1; 5] равно 4
        Максимальное значение функции 2*x**2 + 5*x + 7 на отрезке [-1; 5] равно 82
"""
fan = input()
a, b = map(int, input().split())

res = sorted([eval(fan) for x in range(a, b + 1)])
print(f'Минимальное значение функции {fan} на отрезке [{a}; {b}] равно {res[0]}')
print(f'Максимальное значение функции {fan} на отрезке [{a}; {b}] равно {res[-1]}')


# Вариант
import sys
data = [el.strip() for el in sys.stdin]
fan = data[0]
a, b = map(int, data[1].split())

res = sorted([eval(fan) for x in range(a, b + 1)])
print(f'Минимальное значение функции {fan} на отрезке [{a}; {b}] равно {res[0]}')
print(f'Максимальное значение функции {fan} на отрезке [{a}; {b}] равно {res[-1]}')




