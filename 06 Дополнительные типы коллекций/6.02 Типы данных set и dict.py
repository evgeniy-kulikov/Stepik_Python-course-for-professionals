# 6.2 Типы данных set и dict
""""""


"""   *   *   *   Task   *   *   *   """


#  6.2-1
"""

Input:  *
Output: *
"""
# Стандартный вариант
from string import ascii_lowercase as alphabet

d = dict(zip(alphabet, input()))
letter = input().lower()

for el in letter:
    if el in d:
        print(d[el], end='')
    else:
        print(el, end='')

# Стандартный вариант (короче)
from string import ascii_lowercase as alphabet

d = dict(zip(alphabet, input()))
for el in input().lower():
    print(d.get(el, el), end='')


# Применение словаря соответствия с помощью строкового метода maketrans()
# https://docs-python.ru/tutorial/operatsii-tekstovymi-strokami-str-python/metod-str-maketrans/

from string import ascii_lowercase as alphabet

d = dict(zip(alphabet, input()))
letter = input().lower()
conversion = letter.maketrans(d)
print(letter.translate(conversion))


# Короче (без словаря)
from string import ascii_lowercase as alphabet

conversion = str.maketrans(alphabet, input())
print(input().lower().translate(conversion))



