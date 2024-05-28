""" Полезные решения"""

"""Двойной уровень вложенности ключей создаваемого словаря"""
data = {'k_out_1': "a", 'k_in_1': "b", "k_ls": 1}
res = dict()

for el in data:
    res.setdefault(el['k_out_1'], {}).setdefault(el['k_in_1'], [])
    res[el['k_out_1']][el['k_in_1']] += [el['k_ls']]

res = {'k_out_1': {'k_in_1': [1]}}


"""получить первую пару ключ-значение словаря"""
data = {'k_1': "v_1", 'k_2': "v_1"}
key_val = next(iter(data.items()))
print(f'{key_val[0]}: {key_val[1]}')


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
"""


# Конструкция zip(*[iter(iterable)] * n)
x = iter([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(*zip(x, x, x))
# (1, 2, 3) (4, 5, 6) (7, 8, 9)
