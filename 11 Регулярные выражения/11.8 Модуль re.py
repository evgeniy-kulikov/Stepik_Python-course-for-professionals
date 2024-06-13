# 11.8 Модуль re.
""""""


"""   *   *   *   Task   *   *   *   """


#  11.08-1
"""
Функция normalize_jpeg()
https://stepik.org/lesson/680266/step/9?unit=678924
Реализуйте функцию normalize_jpeg(), которая принимает один аргумент:
filename — название файла, имеющее расширение jpeg или jpg, 
которое может быть записано буквами произвольного регистра
Функция должна возвращать новое название файла с нормализованным расширением — jpg
"""
from re import sub

def normalize_jpeg(filename):
    reg = r'(?i)\.jpe?g$'
    return sub(reg, r'.jpg', filename)


print(normalize_jpeg('stepik.jPeG'))
# stepik.jpg

print(normalize_jpeg('mountains.JPG'))
# mountains.jpg

print(normalize_jpeg('windows11.jpg'))
# windows11.jpg

print(normalize_jpeg('jpg.jPg.Jpg.JPG'))
# jpg.jPg.Jpg.jpg


#  11.08-2
"""
Функция normalize_whitespace()
https://stepik.org/lesson/680266/step/10?unit=678924
Реализуйте функцию normalize_whitespace(), которая принимает один аргумент:
string — произвольная строка
Функция должна заменять все множественные пробелы в строке string на единственный пробел 
и возвращать полученный результат.
Input:  *
Output: *
"""
from re import sub

def normalize_whitespace(string):
    reg = r'\s{2,}'
    return sub(reg, r' ', string)


print(normalize_whitespace('AAAA                A                AAAA'))
# AAAA A AAAA

print(normalize_whitespace('Тут нет лишних пробелов'))
# Тут нет лишних пробелов

print(normalize_whitespace('Тут   н   е   т     л   и     шних пробелов     '))
# Тут н е т л и шних пробелов


#  11.08-3
"""
Ключевые слова
https://stepik.org/lesson/680266/step/11?unit=678924
На вход программе подается строка.
В введенном тексте заменить все ключевые слова (в любом регистре) на строку <kw> и вывести полученный результат.

import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
from re import sub, I
import keyword

def rep_kw(word):
    s = word.group()
    if s.lower() in [i.lower() for i in keyword.kwlist]:
        return '<kw>'
    return s

res = sub(r'(?i)\w+', rep_kw, input())
# res = sub(r'\b(\w+)\b', rep_kw, input(), flags=I)
print(res)


# Нестандартное решение
import re
import keyword

keys = '|'.join(keyword.kwlist)
print(re.sub(fr"\b({keys})\b", r'<kw>', input(), flags=re.I))

# True, assert, as, false, or, Import
# <kw>, <kw>, <kw>, <kw>, <kw>, <kw>

# True or False - that's the question
# <kw> <kw> <kw> - that's the question

# True and False - that is the question
# <kw> <kw> <kw> - that <kw> the question


#  11.08-4
"""
Первые буквы
https://stepik.org/lesson/680266/step/12?unit=678924
Напишите программу, которая меняет местами первые две буквы в каждом слове, 
состоящем из двух или более букв.
"""
from re import sub

# Ожидаемое решение по теме
res = sub(r'\b(\w)(\w)', r'\2\1', input())
print(res)


# Примитивное решение
def rev(word):
    s = word.group()
    if len(s) >= 2:
        return s[1] + s[0] + s[2:]
    return s

res = sub(r'\w+', rev, input())
print(res)


# This is Python
# hTis si yPthon
#
# Hi, everyone. Lets start a lesson!
# iH, veeryone. eLts tsart a elsson!



#  11.08-5
"""
Умножение строк
https://stepik.org/lesson/680266/step/13?unit=678924
Назовем умножением строки на число запись в формате n(string), 
где n — неотрицательное целое число, 
а string — строка, которая должна быть записана n раз. 
Раскрытием умножения будем считать развернутый вариант данной записи, 
например, строка ti2(Be)3(Ge) после раскрытия в ней всех умножений будет иметь вид tiBeBeGeGeGe.
Напишите программу, которая раскрывает все умножения в тексте и выводит полученный результат.
 Гарантируется, что умножение в подаваемой строке всегда записано корректно, то есть строго в формате n(string)
"""
from re import subn

st = input()
cnt = 1
reg = r'(\d+)\((\w*)\)'

def fanc(obj):
    return obj.group(2) * int(obj.group(1))

while cnt:
    st, cnt = subn(reg, fanc, st)
print(st)


# Короче
from re import subn

st = input()
cnt = 1
reg = r'(\d+)\((\w*)\)'

while cnt:
    st, cnt = subn(r'(\d+)\((\w*)\)', lambda m: m[2] * int(m[1]), st)
print(st)


# hello3(world)hi
# helloworldworldworldhi

# 0(s)he0(be)lie0(ve)d
# helied

# bbbb10(2(a))bbb
# bbbbaaaaaaaaaaaaaaaaaaaabbb

# hi2(priv3(d3(i)dd)qq)b0(pr)qwqdd
# hiprivdiiidddiiidddiiiddqqprivdiiidddiiidddiiiddqqbqwqdd

# hhhhhh
# hhhhhh


#  11.08-6
"""
Повторяющиеся слова 🌶️
https://stepik.org/lesson/680266/step/14?unit=678924
В введенной строке заменить все повторяющиеся рядом стоящие слова на одно слово и вывести полученный результат.
* Программа должна быть чувствительной к регистру, то есть, например, слова python и Python считаются различными.
"""
from re import sub

reg = r'(\b\w+\b)(\W+\1\b)+'

print(sub(reg, r'\1', input()))

# beegeek,beegeek,beegeek! python python.. Python.. stepik?stepik?stepik
# beegeek! python.. Python.. stepik

# hi, hi, hi, hello, hello, HELLO, HELLO, HELLO, HELLO, hello!
# hi, hello, HELLO, hello!

# wow Wow wow WOW
# wow Wow wow WOW


#  11.08-7
"""
Комментарии 🌶️🌶️
https://stepik.org/lesson/680266/step/15?unit=678924
На вход программе подается произвольное число строк, представляющих собой Python код.
Программа должна удалить все комментарии из введенного кода согласно условию задачи и вывести полученный результат.
Input:  *
Output: *
"""
import re
import sys

regex = r'\n#.*?$|' \
        r'\s*""".*?"""|' \
        r'\n? *#.*?$'

s = sys.stdin.read()
print(re.sub(regex, '', s, flags=re.S | re.M))


# Вариант
import re
import sys

text = sys.stdin.read()
# text = re.sub(re.compile('^ *\"\"\"[\w \n]*\"\"\"[\n]', re.MULTILINE), "", text)
# text = re.sub(r'^ *#.*[\n]', "", text, flags=re.MULTILINE)
# text = re.sub(r" *#.*$", "", text, flags=re.MULTILINE)
# print(text)

patterns = [r"(^ *\"\"\"[\w \n]*\"\"\"[\n])", r"(^ *#.*[\n])", r"( *#.*$)"]
for pattern in patterns:
    for match in re.finditer(pattern, text, flags=re.MULTILINE):
        s = match.group()
        text = text.replace(s, " ")
print(text)



