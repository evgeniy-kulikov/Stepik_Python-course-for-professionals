#  6.10 Тип данных ChainMap
""""""

"""
Атрибут maps

Объект ChainMap хранит все объединяемые словари во внутреннем списке. 
Этот список доступен через атрибут maps и может быть изменен. 
Порядок словарей в списке maps соответствует порядку, 
в котором словари были указаны при создании объекта ChainMap

Атрибут maps можно использовать для обработки абсолютно всех значений во всех словарях.

Тип данных ChainMap удобен в том случае, 
когда мы уже имеем некоторую коллекцию с большим количеством словарей 
и нам требуется производить поиск по всем словарям одновременно.
"""
from collections import ChainMap

dt1 = {'dogs': 3, 'cats': 9}
dt2 = {'dogs': 2, 'cats': 7, 'tigers': 3}

pets = ChainMap(dt1, dt2)

print(pets)  # ChainMap({'dogs': 3, 'cats': 9}, {'dogs': 2, 'cats': 7, 'tigers': 3})
print(pets.maps)  # [{'dogs': 3, 'cats': 9}, {'dogs': 2, 'cats': 7, 'tigers': 3}]

pets.maps.reverse()
print(pets)  # ChainMap({'dogs': 2, 'cats': 7, 'tigers': 3}, {'dogs': 3, 'cats': 9})

pets.maps[0]['dogs'] = 10
print(pets)  # ChainMap({'dogs': 10, 'cats': 7, 'tigers': 3}, {'dogs': 3, 'cats': 9})


"""
Метод new_child(m=None) возвращает НОВЫЙ объект ChainMap(), содержащий новый словарь m, 
за которым следуют все словари текущего объекта:

если указан словарь m, то он вставляется первым в списке существующих словарей текущего объекта ChainMap
если m не указан, то используется пустой словарь, который также вставляется первым

Примечание: Вызов метода d.new_child() эквивалентен вызову ChainMap({}, *d.maps)
"""
dt1 = {'dogs': 3, 'cats': 9}
dt2 = {'hamster': 2, 'pig': 7}

pets = ChainMap(dt1, dt2)
print(pets)  # ChainMap({'dogs': 3, 'cats': 9}, {'hamster': 2, 'pig': 7})

all_pets = pets.new_child()
print(all_pets)  # ChainMap({}, {'dogs': 3, 'cats': 9}, {'hamster': 2, 'pig': 7})

birds = {'parrot': 4, 'canary': 5}
all_pets = pets.new_child(birds)
print(all_pets)  # ChainMap({'parrot': 4, 'canary': 5}, {'dogs': 3, 'cats': 9}, {'hamster': 2, 'pig': 7})

"""
Атрибут parents возвращает НОВЫЙ объект ChainMap, 
содержащий все словари, кроме первого. Это полезно для пропуска первого словаря при поиске ключей.
Примечание: Обращение к атрибуту d.parents эквивалентно вызову ChainMap(*d.maps[1:])
"""
dear_pets = all_pets.parents
print(dear_pets)  # ChainMap({'dogs': 3, 'cats': 9}, {'hamster': 2, 'pig': 7})


"""   *   *   *   Task   *   *   *   """


#  6.10-1
"""
Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:

chainmap — объект типа ChainMap, элементами которого являются словари
key — произвольный объект
Функция должна возвращать множество, 
элементами которого являются все значения по ключу key из всех словарей в chainmap. 
Если ключ key отсутствует в chainmap, функция должна вернуть пустое множество.
Input:  tests_3096397_01.zip
        https://github.com/python-generation/Professional/blob/main/Module_6/Module_6.10/Module_6.10.13/input.txt
Output: https://github.com/python-generation/Professional/blob/main/Module_6/Module_6.10/Module_6.10.13/output.txt
"""
from collections import ChainMap

def get_all_values(data: object, key: str) -> set:
    res = set()
    for el in data.maps:
        if key in el.keys():
            res.add(el[key])
    return res

#  Короче
def get_all_values(data: object, key: str) -> set:
    return set(el[key] for el in data.maps if key in el.keys())

# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# result = get_all_values(chainmap, 'name')
# print(*sorted(result))



#  6.10-2
"""
Реализуйте функцию deep_update(), которая принимает три аргумента в следующем порядке:

chainmap — объект типа ChainMap, элементами которого являются словари
key — хешируемый объект
value — произвольный объект
Функция должна изменять все значения по ключу key во всех словарях в chainmap на value. 
Если ключ key отсутствует в chainmap, функция должна добавить пару key: value в первый словарь.
Input:  tests_3096398_02.zip
        https://github.com/python-generation/Professional/blob/main/Module_6/Module_6.10/Module_6.10.14/input.txt
Output: https://github.com/python-generation/Professional/blob/main/Module_6/Module_6.10/Module_6.10.14/output.txt
"""
from collections import ChainMap

def deep_update(obj: object, key, val):
    data = obj.maps
    if key in obj.keys():
        for el in data:
            if key in el.keys():
                el[key] = val
    else:
        data[0].update({key: val})

# chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
# deep_update(chainmap, 'name', 'Dima')
# print(chainmap)
# ChainMap({'city': 'Moscow'}, {'name': 'Dima'}, {'name': 'Dima'})


#  6.10-3
"""
Реализуйте функцию get_value(), которая принимает три аргумента в следующем порядке:

chainmap — объект типа ChainMap, элементами которого являются словари
key — произвольный объект
from_left — булево значение, по умолчанию равное True
Функция должна возвращать значение по ключу key из chainmap, причем:

если from_left имеет значение True, поиск ключа в chainmap должен происходить от первого словаря к последнему
если from_left имеет значение False, поиск ключа в chainmap должен происходить от последнего словаря к первому
Если ключ key отсутствует в chainmap, функция должна вернуть значение None.

Input:  tests_3096396_03
        https://github.com/python-generation/Professional/blob/main/Module_6/Module_6.10/Module_6.10.15/input.txt
Output: https://github.com/python-generation/Professional/blob/main/Module_6/Module_6.10/Module_6.10.15/output.txt
"""
from collections import ChainMap

def get_value(obj, key, from_left=True):
    data = obj.maps
    if from_left:
        for el in data:
            if key in el.keys():
                return el[key]
    for el in data[::-1]:
        if key in el.keys():
            return el[key]


# Короче
def get_value(obj, key, from_left=True):
    data = obj.maps
    for el in data if from_left else data[::-1]:
    # for el in data if from_left else reversed(data):
        if key in el:
            return el[key]

# chainmap = ChainMap({'age': 20}, {'city': 'Moscow'}, {'name': 'Anri', 'age': 20}, {'name': 'Timur', 'age': 29})
# print(get_value(chainmap, 'name'))  # Anri
