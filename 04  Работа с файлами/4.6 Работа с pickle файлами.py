# 4.6 Работа с pickle файлами
""""""

"""
Преобразование переменных программы (Python-объектов) в формат для хранения называется «сериализацией», 
а обратное преобразование — «десериализацией».
"""

"""
Функция dump() модуля pickle 
принимает сериализуемый Python объект, сериализует его в бинарный, Python-зависимый формат, 
используя протокол pickle, и сохраняет его в открытый для записи бинарный файл.
"""
import pickle

obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}

with open('file.pkl', 'wb') as file:
    pickle.dump(obj, file)


"""
Функция load() модуля pickle 
принимает файловый объект, читает из него сериализованные данные, десериализует их в Python-объект 
и возвращает полученный Python-объект.
"""
import pickle

with open('file.pkl', 'rb') as file:     # используется файл полученный на предыдущем шаге
    obj = pickle.load(file)
    print(obj)
    print(type(obj))
# {'Python': 1991, 'Java': 1995, 'C#': 2002}
# <class 'dict'>


"""
Функция dumps() модуля pickle 
выполняет такую же сериализацию, как и функция dump(). 
Но вместо того чтобы сохранять сериализованные данные в открытый для записи бинарный файл, 
она просто возвращает эти сериализованные данные.

ип данных bytes — это неизменяемые последовательности отдельных байтов. 
Синтаксис для байтовых литералов в основном такой же, как и для строковых литералов, 
за исключением того, что добавляется префикс b
"""
import pickle

obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
binary_obj = pickle.dumps(obj)

print(binary_obj)
print(type(binary_obj))
# b'\x80\x03}q\x00(X\x06\x00\x00\x00Pythonq\x01M\xc7\x07X\x04\x00\x00\x00Javaq\x02M\xcb\x07X\x02\x00\x00\x00C#q\x03M\xd2\x07u.'
# <class 'bytes'>


"""
Функция loads() модуля pickle 
выполняет такую же десериализацию, как и функция load(). 
Но вместо того чтобы принимать файловый объект, она принимает объект типа bytes, 
содержащий сериализованные данные.
"""
import pickle

obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
binary_obj = pickle.dumps(obj)

new_obj = pickle.loads(binary_obj)

print(new_obj)
# {'Python': 1991, 'Java': 1995, 'C#': 2002}


# объекты obj и new_obj равны (имеют одинаковое содержимое), однако объекты не являются идентичными
import pickle

obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
binary_obj = pickle.dumps(obj)
new_obj = pickle.loads(binary_obj)

print(obj == new_obj)  # True
print(obj is new_obj)  # False (проверка на идентичность)


"""   *   *   *   Task   *   *   *   """


#  4.6-1
"""
Найдите и исправьте ошибки, допущенные в приведенной ниже программе, 
чтобы она сериализовала словарь dogs и записала результат в файл dogs.pkl.
"""
# import pickle
# dogs = {'Ozzy': 2, 'Filou': 7, 'Luna': 4, 'Skippy': 11, 'Barco': 13, 'Balou': 10, 'Laika': 15}
# with open('dogs.pkl', mode='rt') as file:
#     pickle.dumps(dogs, file)


import pickle

dogs = {'Ozzy': 2, 'Filou': 7, 'Luna': 4, 'Skippy': 11, 'Barco': 13, 'Balou': 10, 'Laika': 15}

with open('dogs.pkl', mode='wb') as file:
    pickle.dump(dogs, file)


#  4.6-2
"""
На вход программе в первой строке подается название pickle файла, 
в котором содержится единственная сериализованная функция. 
Далее подается произвольное количество строк, 
каждая из которых содержит позиционный аргумент для этой функции.
Программа должна вызвать функцию из указанного pickle файла со всеми введенными строковыми аргументами, 
и вывести возвращаемое значение функции. Причем аргументы должны быть переданы в том порядке, 
в котором они были введены.
"""
import pickle
import sys

file_name, *args = (el.strip() for el in sys.stdin)

with open(file_name, 'rb') as file_in:
    new_func = pickle.load(file_in)  # создание объекта-функции из файла

print(new_func(*args))


#  4.6-3
"""
Реализуйте функцию filter_dump(), которая принимает три аргумента в следующем порядке:
* filename — название pickle файла, например, data.pkl
* objects — список произвольных объектов
* typename — тип данных
Функция должна создавать pickle файл с названием filename, 
который содержит сериализованный список только тех объектов из списка objects, тип которых равен typename
"""
import pickle

def filter_dump(filename, objects, typename):
    with open(filename, 'wb') as file:
        lst = [el for el in objects if type(el) == typename]
        pickle.dump(lst, file)


#  4.6-4
"""
Контрольная сумма
https://stepik.org/lesson/584474/step/15?unit=579234
"""
import pickle

file_name = input()
num = int(input())

with open(file_name, 'rb') as file:
    key = num
    val = pickle.load(file)
    if type(val) == dict:
        check = sum(el for el in val.keys() if type(el) == int)
    else:
        lst = list(el for el in val if type(el) == int)
        check = min(lst, default=0) * max(lst, default=0)  # default=0  - если значений нет
    if key == check:
        print('Контрольные суммы совпадают')
    else:
        print('Контрольные суммы не совпадают')

