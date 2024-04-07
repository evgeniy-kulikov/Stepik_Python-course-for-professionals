# 11.1 Регулярные выражения
""""""

# 01
"""
Найти все телефонные номера, соответствующие следующим форматам:
7-ddd-ddd-dd-dd
8-ddd-dddd-dddd
где d — цифра от 0 до 9

Формат выходных данных
Программа должна в введенном тексте найти все телефонные номера, 
соответствующие форматам, указанным в условии задачи, 
и вывести их в том порядке, в котором они были найдены, 
каждый на отдельной строке.
Input:  Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911
Output: 7-919-667-21-19
        8-917-4864-1911
"""
import re

pattern = r'(?:(7-\d{3}-\d{3}-\d{2}-\d{2})|(8-\d{3}-\d{4}-\d{4}))'
string = input()

res = re.finditer(pattern, string)
for el in res:
    if el:
        print(el.group())


# решение без регулярки
string = input()
# string = 'Артур: +72-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 82-917-4864-1911'
ls_tel = ''.join([c if c in '0123456789-' else ' ' for c in string]).strip().split()
# ls_tel = ['72-919-667-21-19', '7-', '-', '-', '82-917-4864-1911']
for el in ls_tel:
    mask = el[0]+''.join(['0' if c.isdigit() else c for c in el[1:]])
    if mask in ['70-000-000-00-00', '80-000-0000-0000']:
        print(el)


# 02
"""
регулярное выражение, которому соответствует строка beegeek.
"""
regex = r'beegeek'


# 03
"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют последовательности формата xxx.xxx, где x — любой символ.
Input:  Hello.How are you today?
Output: llo.How
"""
regex = r'.{3}\..{3}'


# 04
"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют последовательности цифр, представляющие целые числа от 100 до 199 включительно.
Input:  150 + 1000 = 1150
Output: 150 100 115
"""
regex = r'1\d{2}'


# 05
"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют телефонные номера формата xxx-xxx-xxxx, где x — произвольная цифра.
Input:  Call me tonight: 415-441-9116, xxx-xxx-xx37
Output: 415-441-9116
"""
regex = r'\d{3}-\d{3}-\d{4}'
