# 6.6 Тип данных OrderedDict
""""""

"""
Тип OrderedDict является подтипом типа dict, сохраняющий порядок, 
в котором пары "ключ-значение" вставляются в словарь. 
Когда мы перебираем объект типа OrderedDict, его элементы перебираются в исходном порядке. 
Если мы обновим значение существующего ключа, то порядок останется неизменным. 
Если мы удалим элемент и вставим его снова, то этот элемент будет добавлен в конец словаря.

Тип OrderedDict будучи подтипом dict наследует все методы, предоставляемые обычным словарем. 
При этом в OrderedDict также есть дополнительные методы:  popitem()  и  move_to_end()
"""

"""
Методу move_to_end() можно передать два аргумента:
key (обязательный аргумент) – ключ, который идентифицирует перемещаемый элемент
last (необязательный аргумент) – логическое значение (тип bool), 
которое определяет, в какой конец словаря мы перемещаем элемент, 
значение True (по умолчанию) перемещает элемент в конец, значение False – в начало
"""


"""
Метод popitem() по умолчанию удаляет элементы с конца словаря.
Если методу popitem() передать необязательный аргумент last=False, 
то он начнет удалять и возвращать элементы с конца в начало словаря
При last=True (по умолчанию)  - наоборот
"""
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)

print(numbers.popitem(last=False))  # ('one', 1)
print(numbers)  # OrderedDict([('two', 2), ('three', 3)])

numbers.move_to_end('two')
print(numbers)  # OrderedDict([('three', 3), ('two', 2)])


"""   *   *   *   Task   *   *   *   """


#  6.6-1
"""
Вам доступен словарь data. Дополните приведенный ниже код, 
чтобы он вывел данный словарь, расположив его элементы в обратном порядке.
"""
from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

print(OrderedDict(reversed(data.items())))

# Вариант
for key in list(data):
    data.move_to_end(key, last=False)
print(data)


#  6.6-2
"""
Вывести словарь "data", расположив его элементы по следующему правилу: 
первый, последний, второй, предпоследний, третий, и так далее.
Input:  data = OrderedDict(key1='value1', key2='value2', key3='value3', key4='value4')
Output: OrderedDict([('key1', 'value1'), ('key4', 'value4'), ('key2', 'value2'), ('key3', 'value3')])
"""
from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

# Переборка "data" постепенным перебрасыванием в конец нужных элементов
saved_keys = tuple(data.keys())  # кортеж из ключей "data" служит для нужной сортировки
for n in range(len(saved_keys) // 2):
    data.move_to_end(saved_keys[n])
    data.move_to_end(saved_keys[-(n + 1)])
print(data)


# В "new_data" перетаскиваем в нужном порядке элементы из "data" (в конце он становиться пустым).
new_data = OrderedDict()
flag = False
for _ in tuple(data):
    key, val = data.popitem(last=flag)
    new_data[key] = val
    flag = not flag
print(data | new_data)



#  6.6-3
"""
Функция должна сортировать словарь ordered_dict:
по ключам, если by_values имеет значение False
по значениям, если by_values имеет значение True
Если два элемента словаря имеют равные значения, то следует сохранить их исходный порядок следования.
Input:  переданный в функцию словарь можно отсортировать, 
        то есть он не содержит ключи, имеющие разные типы, 
        а также значения, имеющие разные типы.
Output:  Функция должна изменять переданный словарь, а не возвращать новый.
"""

from collections import OrderedDict

# В аргумент by_values по сути передается 0 или 1. Эти целые значения и используются в ключе сортировки.
def custom_sort(ordered_dict, by_values=False) -> None:
    for key, value in sorted(ordered_dict.items(), key=lambda x: x[by_values]):
        ordered_dict.move_to_end(key)


data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)
# OrderedDict([('Anabel', 17), ('Brian', 40), ('Carol', 16), ('Dustin', 29)])

# data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
# custom_sort(data, by_values=True)
# ('Mercury', 1) ('Venus', 2) ('Earth', 3) ('Mars', 4)

# data = OrderedDict(a=11, b=2, c=34, d=4, e=59, f=600, g=7)
# custom_sort(data, by_values=False)
# ('a', 11) ('b', 2) ('c', 34) ('d', 4) ('e', 59) ('f', 600) ('g', 7)

print(data)
