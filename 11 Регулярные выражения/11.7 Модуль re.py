# 11.7 Модуль re.
""""""


"""   *   *   *   Task   *   *   *   """


#  11.07-1
"""
https://stepik.org/lesson/680265/step/10?unit=678923
В переменной article определить:
- количество строк, которые начинаются со слова Stepik (в произвольном регистре);
- количество строк, которые оканчиваются тремя точками ... или восклицательным знаком !.
Вывести два соответствующих числа, каждое на отдельной строке.
Input:  article
Output: 4
        6
"""
article = '''Stepik (до августа 2016 года Stepic) — это образовательная платформа и конструктор онлайн-курсов!

Первые образовательные материалы были выпущены на Stepik 3 сентября 2013 года.
В январе 2016 года Stepik выпустил мобильные приложения под iOS и Android. В 2017 году разработаны мобильные приложения для изучения ПДД в адаптивном режиме для iOS и Android...

На октябрь 2020 года на платформе зарегистрировано 5 миллионов пользователей!
Stepik позволяет любому зарегистрированному пользователю создавать интерактивные обучающие уроки и онлайн-курсы, используя видео, тексты и разнообразные задачи с автоматической проверкой и моментальной обратной связью. 

Проект сотрудничает как с образовательными учреждениями, так и c индивидуальными преподавателями и авторами.  
Stepik сегодня предлагает онлайн-курсы от образовательных организаций, а также индивидуальных авторов!

Система автоматизированной проверки задач Stepik была использована в ряде курсов на платформе Coursera, включая курсы по биоинформатике от Калифорнийского университета в Сан-Диего и курс по анализу данных от НИУ «Высшая школа экономики»...

Stepik также может функционировать как площадка для проведения конкурсов и олимпиад, среди проведённых мероприятий — отборочный этап Олимпиады НТИ (2016—2020) (всероссийской инженерной олимпиады школьников, в рамках программы Национальная технологическая инициатива), онлайн-этап акции Тотальный диктант в 2017 году, соревнования по информационной безопасности StepCTF-2015...'''

import re

reg1 = r'(?i)(^stepik)'
reg2 = r'(?m)([.]{3}|!)'

match_1 = re.finditer(reg1, article, flags=re.M)
match_2 = re.finditer(reg2, article)

print(len(list(match_1)), len(list(match_2)), sep="\n")


# Вариант
import re

pattern_start = r"(^stepik)"
pattern_end = r"([.]{3}|!)"
match_start = re.finditer(pattern_start, article, flags=re.I | re.M)
match_end = re.finditer(pattern_end, article, flags=re.I | re.M)
print(len(list(match_start)), len(list(match_end)), sep="\n")


#  11.07-2
"""
Подслова
https://stepik.org/lesson/680265/step/11?unit=678923
программа принимает на вход строку текста и некоторое слово и определяет, 
сколько раз данное слово встречается как подслово в введенном тексте.
"""
from re import findall

text, word = input(), input()

reg = rf'\B({word})\B'
print(len(findall(reg, text)))


#  11.07-3
"""
Слова
https://stepik.org/lesson/680265/step/12?unit=678923
программа принимает на вход строку текста и некоторое слово и определяет, 
сколько вхождений данного слова содержится в введенном тексте.
"""
from re import findall

text, word = input(), input()

reg = rf'\b({word})\b'
print(len(findall(reg, text)))


#  11.07-4
"""
Одинаковые и разные 🍕
https://stepik.org/lesson/680265/step/13?unit=678923
Определить, сколько раз введенное слово встречается в тексте, 
учитывая его Британско-Американское написание, 
и вывести полученный результат
Input:  Gseze
        Gzeze Gsese Gseze Gzese
Output: 2
"""
from re import findall

word, text = input(), input()
match = findall(fr'(?i)\b({word[:-2]}(se|ze))\b', text)
print(len(match))


#  11.07-5
"""
Одинаковые и разные ☕️
https://stepik.org/lesson/680265/step/14?unit=678923
Британия сохранила использование сочетания букв our в своих словах, 
в то время как Америка отказалась от буквы u и использует лишь or.
Определить, сколько раз введенное слово встречается в тексте, 
учитывая его Британско-Американское написание, 
и вывести полученный результат
Input:  hour
        a lot of Hour or hor
Output: 2
"""
from re import findall

word, text = input(), input()
if word.endswith("our"):
    word = word[:-3]
else:
    word = word[:-2]
match = findall(fr'(?i)\b({word}(our|or))\b', text)
print(len(match))

# Вариант
from re import findall

word, text = input(), input()
match = findall(fr'(?i)\b({word[:-2]}u?r)\b', text)
print(len(match))


#  11.07-6
"""
Функция abbreviate()
https://stepik.org/lesson/680265/step/15?unit=678923
Реализуйте функцию abbreviate(), которая принимает один аргумент:
phrase — фраза
Функция должна создавать из фразы phrase аббревиатуру в верхнем регистре и возвращать её.
* В аббревиатуре должны присутствовать как начальные буквы слов, 
  так и начальные буквы подслов, начинающихся с заглавной буквы, 
  например, JavaScript Object Notation -> JSON
"""
from re import finditer

def abbreviate(phrase):
    reg = r'(\b\w)|([A-Z])'
    res = finditer(reg, phrase)
    return ''.join(el.group().upper() for el in res)


print(abbreviate('javaScript object notation'))
# JSON

print(abbreviate('frequently asked questions'))
# # FAQ
#
print(abbreviate('JS game sec'))
# # JSGS


#  11.07-7
"""
HTML 🌶️
https://stepik.org/lesson/680265/step/16?unit=678923
найти во введенном фрагменте HTML-страницы все гиперссылки и вывести их составляющие:
адресные части и указатели, в следующем формате:
<адресная часть>, <указатель>
<адресная часть>, <указатель>
...
* Порядок следования данных об очередной гиперссылке должен совпадать 
  с порядком их следования в введенном фрагменте HTML-страницы.
Input:  <p><a href="https://stepik.org">Stepik</a></p>
        <p><a href="https://beegeek.ru"><b>BEEGEEK</b></a></p>
Output: https://stepik.org, Stepik
        https://beegeek.ru, <b>BEEGEEK</b>
"""
from re import findall
from sys import stdin

text = stdin.read()
reg = r'<a href="(.+)">(.+)</a>'

for address, pointer in findall(reg, text):
    print(f'{address}, {pointer}')


# Вариант
from re import findall
from sys import stdin

reg = r'<a href="(.+)">(.+)</a>'

for el in stdin.read().splitlines():
    for address, pointer in findall(reg, el):
        print(address, pointer, sep=", ")


#  11.07-8
"""
HTML 🌶️🌶️
https://stepik.org/lesson/680265/step/17?unit=678923
найти во введенном фрагменте HTML-страницы все атрибуты каждого тега.
Программа должна найти в введенном фрагменте HTML-страницы все теги 
и вывести их, указав для каждого соответствующие атрибуты. 
Теги вместе со всеми атрибутами должны быть расположены каждый на отдельной строке, в следующем формате:
<тег>: <атрибут>, <атрибут>, ...
* Теги, а также атрибуты тегов, должны быть расположены в лексикографическом порядке.
Input:  <p><a href="https://stepik.org">Stepik</a></p>
        <div class="catalog"><a href="https://stepik.org/catalog">Study hard. Teach harder</a></div>
Output: a: href
        div: class
        p:
"""
from re import findall
from sys import stdin

d = {}
for line in stdin.readlines():
    for tag, params in findall(r'<(\w+)(.*?)>', line):
        d.setdefault(tag, set()).update(findall(r'([\w-]+)=', params))

for key in sorted(d):
    print(f'{key}: {", ".join(sorted(d[key]))}')


# Вариант
from re import findall
from sys import stdin

d = {}
for line in stdin.read().splitlines():
    for text in findall(r'<[^/].*?>', line):
        tag = findall(r'(<\w+)', text)
        key = ''.join(tag)[1:]
        d.setdefault(key, set())

        for v in findall(r'([a-z-]*=)', text):
            d[key].add(v[:-1])


for k, v in sorted(d.items()):
    print(f"{k}: {', '.join(sorted(v))}")
