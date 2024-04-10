#  4.4 Работа с json файлами
""""""

"""
Python-объект --> json      сериализация
json --> Python-объект      десериализация

Python-объект --> json трока        dumps()
json трока --> Python-объект        loads()

Python-объект --> файл с json данными        dump()
файл с json данными --> Python-объект        load()
"""



"""
Модуль json
Преобразование переменных программы (Python-объектов) 
в формат для хранения называется «сериализацией», 
а обратное преобразование — «десериализацией». 
В Python для сериализации и десериализации в формат json есть модуль, который так и называется — json.
"""

"""
Функция dumps()
Для сериализации данных в json строку используется функция dumps() из модуля json. 
Для того, чтобы сериализовать данные с ее помощью, 
достаточно передать в нее аргументом любой сериализуемый Python объект. 
Так как json — текстовый формат, то сериализация в него
это по сути преобразование данных в строку.
"""
import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow'}
json_data = json.dumps(data)  # сериализуем словарь data в json строку

"""
Функция dump()
В отличие от функции dumps(), которая преобразует (сериализует) Python объект в json строку, 
функция dump() записывает переданный Python объект в файл.
"""
import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow'}
with open('countries.json', 'w') as fl:
    json.dump(data, fl)
# создает и сохраняет в файл информацию из словаря data в json формате (в одну строку без форматирования).
# {"name": "Russia", "phone_code": 7, "capital": "Moscow"}

"""
Функции записи dumps() и dump() имеют необязательные аргументы indent, sort_keys и separators
- indent        задает отступ от левого края (по умолчанию indent=None  без отступов)
- sort_keys     задает сортировку ключей в результирующем json (по умолчанию sort_keys=False)
- separators    задает кортеж, состоящий из двух элементов (item_separator, key_separator), 
                которые представляют разделители для элементов и ключей.  
                По умолчанию аргумент имеет значение (', ', ': ')
- skipkeys      игнорировать неправильные ключи (по умолчанию skipkeys=False)
- ensure_ascii  использование Unicode (по умолчанию ensure_ascii=True - символы не ascii будут заменены на коды)
"""
import json

data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow'}
json_data = json.dumps(data, indent=3, separators=(';', ' = '))
print(json_data)
"""
{
   "name" = "Russia";
   "phone_code" = 7;
   "capital" = "Moscow"
}
"""


"""
Функция loads()
Для десериализации данных нужно использовать функцию loads(). 
Ее аргумент — это строка с данными в формате json
"""
import json

json_data = '{"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB"}'
data = json.loads(json_data)
print(type(data))
print(data)
# <class 'dict'>
# {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow'}


"""
Функция load()
В отличие от функции loads(), которая в качестве аргумента принимает строку с данными в формате json, 
функция load() принимает файловый объект и возвращает его десериализованное содержимое.
"""


"""   *   *   *   Task   *   *   *   """


#  4.4-1
"""
Дополните приведенный ниже код, чтобы он вывел содержимое словаря countries, 
расположив его элементы в лексикографическом порядке ключей, 
указав в качестве разделителя элементов "," 
(запятая без пробела), в качестве разделителя пар ключ-значение — строку  " - " 
(пробел дефис пробел), а в качестве отступов — три пробела.
"""
import json

countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
             'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
             'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
             'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

# sort_dict = dict(sorted(countries.items()))
# json_dict = json.dumps(sort_dict, indent=3, separators=(',', ' - '))
# print(json_dict)

json_dict = json.dumps(countries, sort_keys=True, indent=3, separators=(',', ' - '))
print(json_dict)


#  4.4-2
"""
Дополните приведенный ниже код, чтобы он преобразовал словарь words в строку в формате JSON, 
пропуская пары, которые имеют недопустимые ключи, 
и присвоил полученный результат переменной data_json
"""
import json

words = {
         frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
         "travel": "trævl",
         ("hello", "world"): ("həˈləʊ", "wɜːld"),
         "moonlight": "muːn.laɪt",
         "sunshine": "ˈsʌn.ʃaɪn",
         ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
         "adventure": "ədˈventʃər",
         "beautiful": "ˈbjuːtɪfl",
         frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
         "bicycle": "baisikl",
         ("pilot", "fly"): ("pailət", "flai")
        }

data_json = json.dumps(words, skipkeys=True)


#  4.4-3
"""
доступны словари club1, club2 и club3, содержащие данные о различных футбольных клубах. 
Дополните приведенный ниже код, чтобы он объединил данные словари в список 
и записал полученную структуру данных в файл data.json, 
указав в качестве отступов три символа пробела.
"""
import json

club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
         "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}

club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
         "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}

club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
         "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}

ls = [club1, club2, club3]

with open('data.json', 'w') as fl:
    json.dump(ls, fl, indent=3)


#  4.4-4
"""
программа, должна преобразовать словарь specs в строку в формате JSON и вывести ее с отступами в три пробела, 
не заменяя кириллические символы на их коды. В программе допущена ошибка. Найдите и исправьте ее.
Input:  *
Output: *
"""
import json

specs = {
         'Модель': 'AMD Ryzen 5 5600G',
         'Год релиза': 2021,
         'Сокет': 'AM4',
         'Техпроцесс': '7 нм',
         'Ядро': 'Cezanne',
         'Объем кэша L2': '3 МБ',
         'Объем кэша L3': '16 МБ',
         'Базовая частота': '3900 МГц'
        }

# specs_json = json.dumps(specs, ensure_ascii=True)
specs_json = json.dumps(specs, ensure_ascii=False, indent=3)
print(specs_json)


#  4.4-5
"""
Реализуйте функцию is_correct_json(), которая принимает один аргумент:
string — произвольная строка
Функция должна возвращать True, если строка string удовлетворяет формату JSON, 
или False в противном случае.
"""
import json

def is_correct_json(string):
    try:
        json.loads(string)
    except json.JSONDecodeError:
        return False
    return True

# data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
# data = 'number = 17'
# print(is_correct_json(data))


#  4.4-6
"""
Элементы JSON
Вывести все пары ключ-значение введенного объекта, 
разделяя ключ и значение двоеточием, каждую на отдельной строке. 
Если значением ключа является список, то все его элементы должны быть выведены через запятую.
"""
import json
import sys

data = json.loads(sys.stdin.read())

for k, v in data.items():
    if isinstance(v, list):  # if type(v) == list
        v = ', '.join(map(str, v))
    print(f'{k}: {v}')

# Короче
for k, v in data.items():
    print(f'{k}: {", ".join(map(str, v)) if type(v) == list else v}')


#  4.4-7
"""
Разные типы
https://stepik.org/lesson/623073/step/7?unit=618703
Input:  data.json
Output: updated_data.json
"""
import json

with open('data.json', mode='r', encoding='utf-8') as fl_in, \
        open('updated_data.json', mode='w', encoding='utf-8') as fl_out:
    data = json.load(fl_in)

    while None in data:
        data.remove(None)

    for idx, el in enumerate(data):
        if isinstance(el, str):
            data[idx] += '!'
        elif type(el) in (int, float):
            data[idx] += 1
        elif type(el) is bool:
            data[idx] = not el
        elif isinstance(el, list):
            data[idx] *= 2
        elif isinstance(el, dict):
            el['newkey'] = None

    while None in data:
        data.remove(None)

    json.dump(data, fl_out)


#  4.4-8
"""
Написать программу, которая объединяет два данных JSON-объекта в один JSON-объект, 
причем если пары из первого и второго объектов имеют совпадающие ключи, 
то значение следует взять из второго объекта. 
Полученный JSON-объект программа должна записать в файл
Input:  data1.json, data2.json
Output: data_merge.json
"""
import json

with open('data1.json', encoding='utf-8') as fl_1, open('data2.json', encoding='utf8') as fl_2, \
        open('data_merge.json', 'w') as fl_out:
    # Короче
    # json.dump(json.load(fl_1) | json.load(fl_2), fl_out)

    # Развернуто
    dt_1 = json.load(fl_1)
    dt_2 = json.load(fl_2)
    dt_1.update(dt_2)
    json.dump(dt_1, fl_out, indent=3)


#  4.4-9
"""
Написать программу, которая добавляет в каждый JSON-объект из данного списка все недостающие ключи, 
присваивая этим ключам значение null. 
Ключ считается недостающим, если он присутствует в каком-либо другом объекте, но отсутствует в данном. 
Программа должна создать список с обновленными JSON-объектами и записать его в файл updated_people.json
Input:  people.json
Output: updated_people.json
"""
import json

with open('people.json', encoding='utf8') as fl_in, \
        open('updated_people.json', 'w') as fl_out:
    data = json.load(fl_in)
    all_key = set()
    [all_key.update(el.keys()) for el in data]

    for el in data:
        for k in all_key:
            if k not in el:
                el.setdefault(k, None)

    # for el in data:
    #     el |= dict.fromkeys(all_key - el.keys())

    json.dump(data, fl_out, indent=3)


#  4.4-10
"""
файл countries.json, содержит список JSON-объектов c информацией о странах и исповедуемых в них религиях:
Каждый объект из этого списка содержит два атрибута:
country — страна
religion — исповедуемая религия

Написать программу, которая создает единственный JSON-объект, 
имеющий в качестве ключа название религии, 
а в качестве значения — список стран, в которых исповедуется данная религия. 
Input:  countries.json
Output: religion.json
"""
import json
from collections import defaultdict, Counter

with open('countries.json', encoding='utf8') as fl_in, \
        open('religion.json', 'w') as fl_out:
    data = json.load(fl_in)
    res = defaultdict(list)
    for el in data:
        res[el['religion']] += [el['country']]
    json.dump(res, fl_out, indent=3)


#  4.4-11
"""
Спортивные площадки
https://stepik.org/lesson/623073/step/11?unit=618703
Input:  playgrounds.csv
Output: addresses.json
"""
import csv
import json

with open('playgrounds.csv', encoding='utf-8') as fl_in, \
        open('addresses.json', 'w', encoding='utf-8') as fl_out:
    data = csv.DictReader(fl_in, delimiter=';')
    res = dict()

    for el in data:
        res.setdefault(el['AdmArea'], {}).setdefault(el['District'], [])
        res[el['AdmArea']][el['District']] += [el['Address']]

    json.dump(res, fl_out, ensure_ascii=False, indent=3)


#  4.4-12
"""
Студенты курса
https://stepik.org/lesson/623073/step/12?unit=618703
Input:  students.json
Output: data.csv
"""
import csv
import json

with open('students.json', encoding='utf-8') as fl_in, \
        open('data.csv', 'w', encoding='utf-8', newline='') as fl_out:
    data = json.load(fl_in)
    res = []
    for el in data:
        if el['age'] >= 18 and el['progress'] >= 75:
            res += [(el['name'], el['phone'])]

    writer = csv.writer(fl_out)
    writer.writerow(['name', 'phone'])
    res.sort(key=lambda x: x[0])
    [writer.writerow([el[0], el[1]]) for el in res]


#  4.4-13
"""
Бассейны
https://stepik.org/lesson/623073/step/13?unit=618703
Input:  pools.json
Output: *
"""

import json
from datetime import time

with open('pools.json', encoding='utf-8') as fl_in:
    data = json.load(fl_in)
    res = []
    for el in data:
        start, end = el['WorkingHoursSummer']['Понедельник'].split('-')
        if time.fromisoformat(start) <= time(10) and time.fromisoformat(end) >= time(12):
            res += [(el['DimensionsSummer']['Length'], el['DimensionsSummer']['Width'], el['Address'])]
if res:
    res.sort(key=lambda x: (-x[0], -x[1]))
print(f'{res[0][0]}x{res[0][1]}', res[0][2], sep='\n')


#  4.4-14
"""
Результаты экзамена
https://stepik.org/lesson/623073/step/14?unit=618703
Input:  exam_results.csv
Output: best_scores.json
"""
import csv
import json
from datetime import time

with open('exam_results.csv', encoding='utf-8') as fl_in, \
        open('best_scores.json', 'w', encoding='utf-8', newline='') as fl_out:
    data = csv.reader(fl_in)
    title = next(data)
    title[2] = 'best_score'

    dt_in = dict()
    for el in data:  # формируем словарь со всеми данными
        dt_in.setdefault((el[4], el[0], el[1]), [])
        dt_in[(el[4], el[0], el[1])] += [(int(el[2]), el[3])]

    for el in dt_in:  # сортируем/отрезаем значения. Сортируем ключи
        val = dt_in.get(el)
        if len(val) > 1:
            val.sort(key=lambda x: (x[0], x[1]), reverse=True)
            dt_in[el] = [val[0]]
    dt_sort = dict(sorted(dt_in.items()))

    ls_res = list()  # собираем в списке элементы-словари
    for k, v in dt_sort.items():
        val = [k[1], k[2], v[0][0], v[0][1], k[0]]
        ls_res.append(dict(zip(title, val)))

    json.dump(ls_res, fl_out, indent=3)


#  4.4-15
"""
Общественное питание
https://stepik.org/lesson/623073/step/15?unit=618703
Input:  food_services.json
Output: *
"""
import json
from collections import defaultdict

dt_place = defaultdict(int)
dt_chain = defaultdict(int)

with open('food_services.json', encoding='utf-8') as fl:
    data = json.load(fl)
    for el in data:
        dt_place[el['District']] += 1
        dt_chain[el['OperatingCompany']] += 1

    place_sort = dict(sorted(dt_place.items(), key=lambda x: -x[1]))
    chain_sort = dict(sorted(dt_chain.items(), key=lambda x: -x[1]))

    place = next(iter(place_sort.items()))  # получить первую пару ключ-значение словаря
    print(f'{place[0]}: {place[1]}')

    for el in chain_sort.items():
        if el[0]:  # сли ключ не пустая строка
            print(f'{el[0]}: {el[1]}')
            break


#  4.4-16
"""
Общественное питание - 2
https://stepik.org/lesson/623073/step/16?unit=618703
Input:  food_services.json
Output: *
"""
import csv
from datetime import time
import json
from collections import defaultdict

dt_type = defaultdict(list)

with open('food_services.json', encoding='utf-8') as fl:
    data = json.load(fl)
    for el in data:
        dt_type[el['TypeObject']] += [(el.get('SeatsCount'), el.get('Name'))]

    dt_sort = dict(sorted(dt_type.items(), key=lambda x: x))
    for k, v in dt_sort.items():
        v.sort(key=lambda x: -x[0])
        print(f'{k}: {v[0][1]}, {v[0][0]}')


