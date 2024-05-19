#  9.9 Модуль functools
""""""


"""   *   *   *   Task   *   *   *   """


#  9.9-1
"""
Вам доступна уже реализованная функция send_email(), которая принимает три аргумента в следующем порядке:

name — имя email_address — адрес электронной почты 
text — содержание письма. 
Функция отправляет письмо пользователю с именем name на адрес email_address с содержанием text.

Реализуйте функцию to_Timur() с помощью функции partial(), которая принимает один аргумент:
text — содержание письма. 
Функция должна отправлять письмо пользователю с именем Тимур на адрес timyrik20@beegeek.ru с содержанием text.

Реализуйте функцию send_an_invitation() с помощью функции partial(), 
которая принимает два аргумента в следующем порядке:
name — имя 
email_address — адрес электронной почты 
Функция должна отправлять письмо на имя name и на адрес email_address со следующим содержанием:

Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....
"""

from functools import partial

def send_email(name, email_address, text):
    return f'В письме для {name} на адрес {email_address} сказано следующее: {text}'

to_Timur = partial(send_email, 'Тимур', 'timyrik20@beegeek.ru')

text = "Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут...."
send_an_invitation = partial(send_email, text=text)


#  9.9-2
"""
Напишите программу, которая принимает на вход произвольное количество английских слов 
и в каждом расставляет буквы в лексикографическом порядке.
Слова должны быть расположены в исходном порядке, каждое на отдельной строке.
Input:  tutorial
        pattern
        add
Output: ailorttu
        aenprtt
        add
"""
from functools import lru_cache
import sys

@lru_cache()
def teach_dima(word):
    return ''.join(sorted(word)).strip()

[print(teach_dima(el)) for el in sys.stdin.readlines()]


#  9.9-3
"""
Просто Дима 🙃
https://stepik.org/lesson/751476/step/25?unit=753330
Реализуйте функцию ways(), которая принимает один аргумент:
натуральное число n ≤ 100.
Функция должна возвращать единственное число — количество способов, которыми можно забраться на n-ую ступень. 
Путь начинается с первой ступени, подниматься можно исключительно на одну, три или четыре ступени.
"""
from functools import lru_cache

@lru_cache()
def ways(n):
    if n == 1:
        return 1
    elif n < 1:
        return 0
    else:
        return ways(n - 1) + ways(n - 3) + ways(n - 4)


print(ways(5))  # 4
print(ways(2))  # 1
print(ways(100))  # 256319508074468182850
