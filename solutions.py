""" Полезные решения"""
"""сортировка списка по длине строкового элемента"""
ls = ['dddd', 'a', 'bb', 'ccc']
ls_sort_len = sorted(ls, key=len)
# ['a', 'bb', 'ccc', 'dddd']
ls_sort_reverse = sorted(ls, key=len, reverse=True)
# ['dddd', 'a', 'bb', 'ccc']


""" Двухмерный список в одномерный """

lst_2d = [['1', '2', '3'], ['a', 'b', 'c'], ['*', '=', '%']]

lst_1d = [el for row in lst_2d for el in row]
# lst_1d = [el for row in lst_2d
#           for el in row]
print(lst_1d)
# ['1', '2', '3', 'a', 'b', 'c', '*', '=', '%']

lst_1d = []
for row in lst_2d:
    for el in row:
        lst_1d.append(el)
print(lst_1d)
# ['1', '2', '3', 'a', 'b', 'c', '*', '=', '%']



# метод calendar.shufutinskiy() всегда возвращает 3 сентября
"""
>>> import calendar
... import random
... import locale
>>> locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
'ru_RU.UTF-8'
>>> year = random.randint(1993, 9999)
>>> month = random.randint(1, 12)
>>> calendar.shufutinskiy(year, month)
3 сентября



import calendar
import locale
import random

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

year = random.randint(1993, 9999)
print(calendar.shufutinskiy(year))

#  3 сентябряimport calendar
import locale
import random

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

year = random.randint(1993, 9999)
print(calendar.shufutinskiy(year))

#  3 сентября
"""