# 11.6 Модуль re
""""""


"""   *   *   *   Task   *   *   *   """


#  11.06-1
"""
Телефонные номера
https://stepik.org/lesson/680263/step/9?unit=678921
форматы:
<код страны>-<код города>-<номер>
<код страны> <код города> <номер>
в котором код страны и код города представлены последовательностями от одной до трех цифр включительно, 
а номер — последовательностью от четырех до десяти цифр включительно. 
Между кодом страны, кодом города и номером используется разделитель, 
которым служит либо символ дефис, либо пробел, 
причем одновременно оба вида разделителя в одном номере присутствовать не могут.

для каждого введенного телефонного номера вывести отдельно его код страны, код города и номер в следующем формате:
Код страны: <код страны>, Код города: <код города>, Номер: <номер>
Input:  1 877 2638277
        91-011-23413627
Output: Код страны: 1, Код города: 877, Номер: 2638277
        Код страны: 91, Код города: 011, Номер: 23413627
"""
import sys
from re import fullmatch

reg = r'(?P<country>^\d{1,3}\b)' \
      r'(?P<sep>\s|-)' \
      r'(?P<sity>\b\d{1,3}\b)' \
      r'(?P=sep)' \
      r'(?P<code>\b\d{4,10}\b)'

for el in list(map(str.strip, sys.stdin)):
    match = fullmatch(reg, el)
    if match:
        print(f"Код страны: {match.group('country')}, "
              f"Код города: {match.group('sity')}, "
              f"Номер: {match.group('code')}")


# Вариант
from sys import stdin
from re import search

reg = r'(?P<country>\d{1,3})' \
      r'(?P<sep>\s|-)' \
      r'(?P<sity>\d{1,3})' \
      r'(?P=sep)' \
      r'(?P<code>\d{4,10})'

for el in stdin:
    match = search(reg, el)
    if match:
        print(f"Код страны: {match.group('country')}, "
              f"Код города: {match.group('sity')}, "
              f"Номер: {match.group('code')}")


#  11.06-2
"""
Онлайн-школа BEEGEEK
https://stepik.org/lesson/680263/step/10?unit=678921
логин учетной записи определяется следующим образом:
- первым символом является символ нижнего подчеркивания _
- затем следуют одна или более цифр
- после записываются ноль или более латинских букв в произвольном регистре
- логин может иметь на конце необязательный символ нижнего подчеркивания _
Напишите программу, которая принимает произвольное количество строк и определяет, 
какие из них представляют собой корректный логин.
Input:  _123abc_
        _1abc_
        123abc
        _abc123
        _123abc__
Output: True
        True
        False
        False
        False
"""
from re import fullmatch
from sys import stdin

reg = r'(?i)_\d+[a-z]*_?'

for el in stdin:
    match = fullmatch(reg, el.strip())
    print(bool(match))

# Вариант
import sys
from re import fullmatch

reg = r'(?i)_\d+[a-z]*_?'
data = list(map(str.strip, sys.stdin))

for el in data:
    match = fullmatch(reg, el)
    print(bool(match))


#  11.06-3
"""
Одинаковые слоги
https://stepik.org/lesson/680263/step/11?unit=678921
из введенных слов вывести только те, которые состоят из двух одинаковых слогов. 
Слова должны быть расположены в своем исходном порядке, каждое на отдельной строке.
Input:  Python
        beebee
        PyPy
        portal
Output: beebee
        PyPy
"""
from re import fullmatch
from sys import stdin

reg = r'(\w+)\1'

for el in stdin:
    if fullmatch(reg, el.strip()):
        print(el.strip())


#  11.06-4
"""
Beegeek
https://stepik.org/lesson/680263/step/12?unit=678921
Подается произвольное количество строк, каждая из которых содержит набор произвольных символов.
вывести два числа:
— количество строк, в которых bee встречается в качестве подстроки не менее двух раз
— количество строк, в которых geek встречается в качестве слова хотя бы один раз
Input:  beebee bee
        beegeek
        bee geek bee
Output: 2
        1
"""
from re import search
from sys import stdin

bee = r'bee.*bee'
geek = r'\bgeek\b'
cnt_bee, cnt_geek = 0, 0

for el in stdin:
    if search(bee, el):
        cnt_bee += 1
    if search(geek, el):
        cnt_geek += 1

print(cnt_bee, cnt_geek, sep='\n')


#  11.06-5
"""
Популярность
https://stepik.org/lesson/680263/step/13?unit=678921
Ищем вхождения строки beegeek в нижнем регистре. Оценка:
в 3 балла, если она начинается и заканчивается строкой beegeek
в 2 балла, если она только начинается или только заканчивается строкой beegeek
в 1 балл, если она содержит строку beegeek только внутри
в 0 баллов, если она не содержит строку beegeek
Определить оценку строки путем суммирования баллов всех публикаций.
Input:  beebee bee
        beegeek
        bee geek bee
Output: 2
        1
"""
from re import search
from sys import stdin

cnt = 0
for el in stdin:
    if search(r'^(beegeek).*\1$', el):
        cnt += 3
    elif search(r'^(beegeek)|(beegeek)$', el):
        cnt += 2
    elif search(r'.+(beegeek).+', el):
        cnt += 1
print(cnt)

# Вариант
from re import match, search
from sys import stdin

reg = r'beegeek'
total = 0
for el in stdin:
    total += bool(match(reg, el))
    total += bool(search(r'beegeek$', el))
    total += bool(search(reg, el))
print(total)


#  11.06-6
"""
Уважение
https://stepik.org/lesson/680263/step/19?unit=678921
вывести True, если введенная строка начинается с:
- Здравствуйте
- Доброе утро
- Добрый день
- Добрый вечер
или False в противном случае.
Input:  здравствуйте, вы не заняты?
Output: True
"""
import re
text = input()

reg = r'здравствуйте|доброе утро|добрый день|добрый вечер'
print(bool(re.match(reg, text, re.I)))

# Вариант
from re import match

text = input()
reg = r'(?i)здравствуйте|доброе утро|добрый день|добрый вечер'
print(bool(match(reg, text)))


#  11.06-7
"""
Социальные сети
https://stepik.org/lesson/680263/step/20?unit=678921
Определить, в скольких публикациях содержится строка beegeek
Input:  *
Output: *
"""
from re import search
from sys import stdin

reg = r'(?i)beegeek'
cnt = 0

for el in stdin:
    if search(reg, el):
        cnt += 1
print(cnt)

# Короче
from re import search
from sys import stdin

reg = r'(?i)beegeek'
print(sum(bool(search(reg, el)) for el in stdin))
