# 4.2 Работа с csv файлами
""""""

"""
Формат CSV
CSV (от англ. Comma-Separated Values — значения, разделённые запятыми) — текстовый формат, 
предназначенный для представления табличных данных. 
Строка таблицы соответствует строке текста, 
которая содержит одно или несколько полей, разделенных запятыми 
(пробелов после запятой быть не должно !!!).
Разделителем записей был выбран символ новой строки, а разделителем полей — символ запятой.
"""

with open('products.csv', encoding='utf-8') as file:
    data = file.read()
    for line in data.splitlines():
        print(line.split(','))
# ['keywords', 'price', 'product_name']
# ['Садовый стул', '1699', 'ВЭДДО']
# ['Садовый стул', '2999', 'ЭПЛАРО']
# ['Садовый стол', '1999', 'ТЭРНО']
# ['Настил', '1299', 'РУННЕН']
# ['Стеллаж', '1299', 'ХИЛЛИС']

# Для построчного разделения текста удобно использовать строковый метод splitlines(), вместо метода split('\n')
with open('products.csv', encoding='utf-8') as file:
    data = file.read()
    table = [el.split(',') for el in data.splitlines()]

# Доступ к конкретной ячейке таблицы
print(table[7][1])


# отсортировать товары по цене и напечатать 3 самых дешевых товаров.
with open('products.csv', encoding='utf-8') as file:
    data = file.read()
    table = [r.split(',') for r in data.splitlines()]
    del table[0]  # удаляем заголовок
    table.sort(key=lambda el: int(el[1]))
    for line in table[:3]:
        print(line)
# ['Кружка', '39', 'СТЕЛЬНА']
# ['Ситечко', '59', 'ИДЕАЛИСК']
# ['Ситечко', '199', 'САККУННИГ']

"""
Если поле содержит запятые, то это поле должно быть заключено в двойные кавычки.

keywords,price,product_name
"Садовый стул, стул для дачи",1699,ВЭДДО
Садовый стол,1999,ТЭРНО
"Складной стол, обеденный стол",7499,ЭПЛАРО
"Кружка, сосуд, стакан с ручкой",39,СТЕЛЬНА
Молочник,299,ВАРДАГЕН
"""


"""     Модуль csv      """
# В данном модуле есть два основных объекта: reader и writer,
# созданные, чтобы читать и создавать csv файлы соответственно.

import csv

with open('products.csv', encoding='utf-8') as file:
    rows = csv.reader(file)  # создаем объект reader, который дает доступ к построчному итератору
    for row in rows:
        print(row)
# ['keywords', 'price', 'product_name']
# ['Садовый стул', '1699', 'ВЭДДО']
# ['Садовый стул', '2999', 'ЭПЛАРО']
# ['Садовый стол', '1999', 'ТЭРНО']
# ['Складной стол', '7499', 'ЭПЛАРО']
# ['Настил', '1299', 'РУННЕН']

# Удобство отображения информации
import csv

with open('products.csv', encoding='utf-8') as file:
    rows = csv.reader(file)
    for keywords, price, name in rows:
        print(f'Товар: {keywords}, цена: {price}, название: {name}')
# Товар: keywords, цена: price, название: product
# Товар: Садовый стул, цена: 1699, название: ВЭДДО
# Товар: Садовый стул, цена: 2999, название: ЭПЛАРО
# Товар: Садовый табурет, цена: 1699, название: ЭПЛАРО

"""
При создании reader объекта мы можем его настраивать, указывая:

аргумент delimiter — односимвольная строка, используемая для разделения полей, 
по умолчанию имеет значение ','

аргумент quotechar — односимвольная строка, используемая для кавычек в полях, 
содержащих специальные символы, по умолчанию имеет значение '"'.
"""


"""
Чтение данных с помощью DictReader
В модуле csv есть специальный объект DictReader, 
который поддерживает создание объекта-словаря на основе названий столбцов. 
С помощью DictReader объекта мы можем обращаться к полям не по индексу, а по названию.


Пусть содержимое файла products.csv имеет вид (в качестве разделителя выбран символ ';'):

keywords;price;product
"Садовый стул, стул для дачи";1699;ВЭДДО
Садовый стул;2999;ЭПЛАРО
Садовый табурет;1699;ЭПЛАРО
Садовый стол;1999;ТЭРНО
"""
import csv

with open('products.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';', quotechar='"')
    for row in rows:
        print(row)
# {'keywords': 'Садовый стул, стул для дачи', 'price': '1699', 'product': 'ВЭДДО'}
# {'keywords': 'Садовый стул', 'price': '2999', 'product': 'ЭПЛАРО'}
# {'keywords': 'Садовый табурет', 'price': '1699', 'product': 'ЭПЛАРО'}
# {'keywords': 'Садовый стол', 'price': '1999', 'product': 'ТЭРНО'}


# # отсортировать товары по цене и напечатать 3 самых дорогих  товаров.
import csv

with open('products.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';', quotechar='"')
    expensive = sorted(rows, key=lambda item: int(item['price']), reverse=True)
    for record in expensive[:3]:
        print(record)
# {'keywords': 'Складной стол, обеденный стол', 'price': '7499', 'product': 'ЭПЛАРО'}
# {'keywords': 'Садовый стул', 'price': '2999', 'product': 'ЭПЛАРО'}
# {'keywords': 'Садовый стол', 'price': '1999', 'product': 'ТЭРНО'}


"""     Запись данных с помощью writer      """

# Для записи данных в csv файл можно использовать специальный writer объект.

import csv

columns = ['first_name', 'second_name', 'class_number', 'class_letter']
data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Артур', 'Харисов', 10, 'В']]

with open('students.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)                 # запись заголовков
    for row in data:                         # запись строк
        writer.writerow(row)

# создает файл students.csv с содержимым:
# first_name,second_name,class_number,class_letter
# Тимур,Гуев,11,А
# Руслан,Чаниев,9,Б
# Артур,Харисов,10,В


"""   *   *   *   Task   *   *   *   """


#  4.2-1
"""
Исправить код, чтобы результатом работы программы были строки:
['name', 'grade']
['Timur', '100']
['Ruslan', '97']

Input:  файл grades.csv
"""
# import csv
#
# with open('grades.csv', encoding='utf-8') as csv_file:
#     # считываем содержимое файла
#     text = csv_file.read()
#     # создаем reader объект и указываем в качестве разделителя символ ;
#     rows = csv.reader(text, delimiter=';')
#     # выводим каждую строку
#     for row in rows:
#         print(row)

import csv

with open('grades.csv', encoding='utf-8') as csv_file:
    rows = csv.reader(csv_file, delimiter=';')
    for row in rows:
        print(row)


#  4.2-2
"""
Исправить код, чтобы программа создала файл writing_test.csv, имеющий следующее содержание:

first_col,second_col
value1,value2
Output:  файл writing_test.csv
"""
# import csv
#
# with open('writing_test.csv', 'w', encoding='utf-8') as csv_file:
#     # создаем writer объект и указываем названия столбцов
#     writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
#     # записываем первую строку с названиями столбцов
#     writer.writeheader()
#     # записываем строку с данными
#     writer.writerow({'key1': 'value1', 'key2': 'value2'})


import csv

with open('writing_test.csv', 'w', encoding='utf-8', newline='') as csv_file:
    # создаем writer объект и указываем названия столбцов
    writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
    # записываем первую строку с названиями столбцов
    writer.writeheader()
    # записываем строку с данными
    writer.writerow({'first_col': 'value1', 'second_col': 'value2'})


#  4.2-3
"""
https://stepik.org/lesson/518491/step/12?thread=solutions&unit=510939
Напишите программу, которая выводит названия тех товаров, цена на которые уменьшилась. 
Товары должны быть расположены в своем исходном порядке, каждый на отдельной строке.
Input:  файл sales.csv
"""
import csv

with open('sales.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    for row in rows:
        if int(row['new_price']) < int(row['old_price']):
            print(row['name'])

# Лишнее создание списка (ведь сортировка не нужна...)
with open('sales.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';', quotechar='"')
    res = filter(lambda el: int(el['new_price']) < int(el['old_price']), rows)
    for row in res:
        print(row['name'])



#  4.2-4
"""
Средняя зарплата
https://stepik.org/lesson/518491/step/13?unit=510939
Напишите программу, которая упорядочивает компании по возрастанию средней зарплаты ее сотрудников 
и выводит их названия, каждое на отдельной строке. Если две компании имеют одинаковые средние зарплаты, 
они должны быть расположены в лексикографическом порядке их названий.
Input:  файл salary_data.csv
"""
import csv
from collections import defaultdict
from statistics import mean


group_dict = defaultdict(list)

with open('salary_data.csv', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=';')
    for el in data:
        group_dict[el['company_name']] += [int(el['salary'])]
for el in group_dict:
    group_dict[el] = mean(group_dict[el])
sort_group = sorted(group_dict.items(), key=lambda el: (el[1], el[0]))
[print(el[0]) for el in sort_group]


#  4.2-5
"""
Сортировка по столбцу
https://stepik.org/lesson/518491/step/14?unit=510939
Напишите программу, которая сортирует содержимое данного файла по указанному столбцу. 
Причем данные должны быть отсортированы в порядке возрастания чисел, если столбец содержит числа, 
и в лексикографическом порядке слов, если столбец содержит слова.
Input:  файл deniro.csv
"""
import csv

with open('deniro.csv', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=',')
    res = [el for el in data]

q = int(input()) - 1

if res[0][q].isdigit():
    res.sort(key=lambda el: int(el[q]))
else:
    res.sort(key=lambda el: el[q])

for el in res:
    print(','.join(el))



#  4.2-6
"""
Функция csv_columns()
https://stepik.org/lesson/518491/step/15?unit=510939
Input:  *
Output: *
"""
import csv
from collections import defaultdict

def csv_columns(file):
    res = defaultdict(list)
    with open(file, encoding='utf-8') as f:
        data = csv.DictReader(f, delimiter=',')
        for row in data:
            for key in row:
                res[key] += [row[key]]
    return dict(res)


# Вариант через setdefault
def csv_columns(filename):
    res = dict()
    with open(filename, encoding='utf-8') as f:
        data = csv.DictReader(f, delimiter=',')
        for row in data:
            for key, val in row.items():
                res.setdefault(key, []).append(val)
    return res

# print(csv_columns('data.csv'))


#  4.2-7
"""
Популярные домены
https://stepik.org/lesson/518491/step/16?unit=510939
Input:  data.csv
Output: domain_usage.csv
"""
import csv

with open('data(domen).csv', encoding='utf-8', mode='r') as f:
    domen = dict()
    data = csv.DictReader(f, delimiter=',')
    for row in data:
        domen.setdefault(row['email'].split('@')[1], 0)
        domen[row['email'].split('@')[1]] += 1

res = [(k, v) for k, v in domen.items()]
res.sort(key=lambda el: (el[1], el[0]))

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['domain', 'count'])
    for row in res:
        writer.writerow(row)

# через DictWriter
# with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.DictWriter(file, delimiter=',',  fieldnames=['domain', 'count'])
#     for dom, cnt in res:
#         writer.writerow({'domain': dom, 'count': cnt})



#  4.2-8
"""
Wi-Fi Москвы
https://stepik.org/lesson/518491/step/17?unit=510939
Input:  wifi.csv
Output: *
"""
import csv
from collections import defaultdict

with open('wifi.csv', encoding='utf-8', mode='r') as f:
    res = defaultdict(int)
    data = csv.DictReader(f, delimiter=';')
    for row in data:
        res[row['district']] += int(row['number_of_access_points'])
res = [(k, v) for k, v in res.items()]
for k, v in sorted(res, key=lambda el: (-el[1], el[0])):
    print(f'{k}: {v}')


# Через dict()
import csv

with open('wifi.csv', encoding='utf-8', mode='r') as f:
    res = dict()
    data = csv.DictReader(f, delimiter=';')
    for row in data:
        res.setdefault(row['district'], 0)
        res[row['district']] += int(row['number_of_access_points'])
res = [(k, v) for k, v in res.items()]
for k, v in sorted(res, key=lambda el: (-el[1], el[0])):
    print(f'{k}: {v}')


#  4.2-9
"""
Последний день на Титанике
https://stepik.org/lesson/518491/step/18?unit=510939
Input:  titanic.csv
Output: *
"""
import csv

with open('titanic.csv', encoding='utf-8', mode='r') as f:
    data = csv.reader(f, delimiter=';')
    next(data)
    male, female = [], []
    for row in data:
        if row[0] == '1' and float(row[3]) < 18:
            if row[2] == 'male':
                male.append(row[1])
            else:
                female.append(row[1])
print(*male, *female, sep='\n')
# male.extend(female)
# print(*male, sep='\n')




#  4.2-10
"""
Лог-файл
https://stepik.org/lesson/518491/step/19?unit=510939
Input:  name_log.csv
Output: *
"""
import csv
from collections import defaultdict
from datetime import datetime as dt

with open('name_log.csv', encoding='utf-8', mode='r') as file_in:
    data = csv.reader(file_in)
    title = next(data)

    res = defaultdict(list)
    for row in data:
        res[row[1]] += [[row[0], row[2]]]

with open('new_name_log.csv', encoding='utf-8', mode='w', newline='') as file_out:
    writer = csv.writer(file_out)
    writer.writerow(title)
    for k, v in sorted(res.items()):
        v.sort(key=lambda el: dt.strptime(el[1], '%d/%m/%Y %H:%M'), reverse=True)
        writer.writerow([v[0][0], k, v[0][1]])


# Короче
import csv
from datetime import datetime as dt

with open('name_log.csv', 'r', encoding='utf-8') as file_in, \
        open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file_out:

    data = csv.reader(file_in)
    title = next(data)

    res = {row[1]: row for row in sorted(data, key=lambda el: dt.strptime(el[2], '%d/%m/%Y %H:%M'))}

    writer = csv.writer(file_out)
    writer.writerow(title)
    for k, v in sorted(res.items()):
        writer.writerow(v)


#  4.2-11
"""
Проще, чем кажется
https://stepik.org/lesson/518491/step/20?unit=510939
"""
import csv

# только на одних свойствах и методах списка...
def condense_csv(file_name,id_name):
    with open(file_name, encoding='utf-8', mode='r') as file_in:
        data = csv.reader(file_in)
        ls = [el for el in data]
        size_obj = 0
        for el in ls:
            if el[0] == ls[0][0]:
                size_obj += 1
            else:
                break
        title = [id_name, *[ls[el][1] for el in range(size_obj)]]

    with open('condensed.csv', encoding='utf-8', mode='w', newline='') as file_out:
        writer = csv.writer(file_out)
        writer.writerow(title)
        for el in range(0, len(ls) - size_obj + 1, size_obj):
            writer.writerow([ls[el][0], *[ls[el + i][-1] for i in range(size_obj)]])


# Вариант.  obj_dict = {объект: [значения атрибутов объекта]}
def condense_csv(filename, id_name):
    with open(filename, "r", encoding="utf-8") as file_in:
        data = csv.reader(file_in)
        title = [id_name]  # + атрибуты
        obj_dict = {}  # объект: [значения атрибутов объекта]
        # {'ball': ['purple', '4', "it's round"], 'cup': ['blue', '1', 'none']}
        for row in data:
            if row[1] not in title:
                title.append(row[1])
            obj_dict[row[0]] = obj_dict.get(row[0], []) + [row[-1]]

    with open("condensed.csv", "w", encoding="utf-8", newline='') as file_out:
        writer = csv.writer(file_out)
        writer.writerow(title)
        for obj in obj_dict:
            writer.writerow([obj, *obj_dict[obj]])




#  4.2-12
"""
Возрастание классов
https://stepik.org/lesson/518491/step/21?unit=510939
Input:  student_counts.csv
Output: sorted_student_counts.csv
"""
import csv

with open('student_counts.csv', encoding='utf-8') as file_in, \
        open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file_out:
    data = csv.DictReader(file_in)
    title = data.fieldnames  # чтение исходного заголовка
    # 3-х и 4-х символьные значения сортируются в лексикографическом порядке
    title = [title[0]] + sorted(title[1:], key=lambda x: (len(x), x))  # формирование сортированного заголовка

    data_out = csv.DictWriter(file_out, fieldnames=title)
    data_out.writeheader()  # запись сортированного заголовка
    for row in data:
        data_out.writerow(row)  # запись строк
        # (в словаре по отсортированным ранее ключам (строка заголовка) меняются привязанные к ним значения)


# Только используя работу со списком
with open('student_counts.csv', encoding='utf-8') as file_in, \
        open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file_out:
    data = csv.reader(file_in)
    ls = [el for el in data]
    ls_title = list(enumerate(ls[0][1:], 1))
    ls_title.sort(key=lambda x: (len(x[1]), x[1]))
    title = [(0,)]
    title.extend(ls_title)
    # [(0,), (25, '1-А'), (6, '1-Б'),...(27, '11-В')] первый элемент в кортежах - первоначальный индекс элемента строки

    ls_sort = []
    for row in ls:
        row_sort = [None] * len(title)
        for el in range(len(row)):
            row_sort[el] = row[title[el][0]]
        ls_sort.extend([row_sort])  # собираем отсортированные строки

    writer = csv.writer(file_out)
    for el in ls_sort:
        writer.writerow(el)


# Только работа со списком (транспонирование матрицы)
with open("student_counts.csv", "r", encoding="utf-8") as file_in:
    with open('sorted_student_counts.csv', 'w', encoding="utf-8", newline='') as file_out:
        data = list(csv.reader(file_in))
        transpose = list(zip(*data))
        transpose = [transpose[0], *sorted(transpose[1:], key=lambda x: (len(x[0]), x[0]))]
        res = list(zip(*transpose))  # собираем отсортированные строки

        writer = csv.writer(file_out)
        writer.writerows(res)


#  4.2-13
"""
Голодный студент
https://stepik.org/lesson/518491/step/22?unit=510939
Input:  prices.csv
"""
import csv

# Работаем со строкой - словарем csv.DictReader
with open('prices.csv', 'r', encoding='utf-8') as file:
    lst = []
    data = csv.DictReader(file, delimiter=';')
    for row in data:
        shop = row.pop('Магазин')  # извлекаем/присваиваем ключ-значение "Магазин": "Название магазина"
        good = min(sorted(row), key=lambda x: int(row.get(x, 0)))  # Находим продукт с минимальной ценой
        price = row[good]  # Получаем цену продукта с минимальной ценой
        lst.append((shop, good, price))
    shop, prod, price = sorted(lst, key=lambda x: (x[2], x[1], x[0]))[0]
    print(prod, shop, sep=': ')


# Работа с 2-х мерным списком
with open("prices.csv", "r", encoding="utf-8") as file:
    data = list(csv.reader(file, delimiter=';'))
    ls_min = [(data[0][1], data[1][0], data[1][1])]
    val_min = int(data[1][1])
    for row in range(1, len(data)):
        for col in range(1, len(data[0])):
            if int(data[row][col]) < val_min:
                val_min = int(data[row][col])
                ls_min.clear()
                ls_min.append((data[0][col], data[row][0], data[row][col]))
            elif int(data[row][col]) == val_min:
                ls_min.append((data[0][col], data[row][0], data[row][col]))
    ls_min.sort(key=lambda x: (x[0], x[1]))
    print(f'{ls_min[0][0]}: {ls_min[0][1]}')
