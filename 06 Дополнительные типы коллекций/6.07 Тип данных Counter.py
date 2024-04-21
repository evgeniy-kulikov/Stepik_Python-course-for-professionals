#  6.7 Тип данных Counter
""""""

"""
Тип Counter является подтипом типа dict, 
специально разработанный для подсчета хешируемых объектов в Python. 
Counter хранит объекты в качестве ключей, а их количество — в качестве значений.
"""
from collections import Counter

counter = Counter('mississippi')    # создаем счетчик на основе строки
print(counter)                      # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})


# можем создавать объекты типа Counter, явно указывая начальные значения количества объектов.
counter1 = Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
counter2 = Counter(i=4, s=4, p=2, m=1)
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

"""
Counter, будучи подтипом типа dict, наследует все методы, предоставляемые обычным словарем. 
При этом вызов метода fromkeys() всегда будет приводить к возникновению ошибки:
NotImplementedError: Counter.fromkeys() is undefined.  Use Counter(iterable) instead.
"""
from collections import Counter
counter = Counter.fromkeys('mississippi', 2)  # NotImplementedError

"""
Для изменения объектов типа Counter мы можем использовать метод update(). 
Реализация данного метода не заменяет значения как у обычных словарей (тип dict), 
а суммирует существующие значения. 
При этом для новых объектов метод update() создает новые пары ключ: количество

!!!  особенность метода update() при работае с типом Counter. 
Складываются значения переданного объекта с изменяемым, а не наоборот  !!!
"""
from collections import Counter

cnt = Counter(a=5, b=7)
cnt.update(b=3)     # Counter({'b': 10, 'a': 5})

cnt_up = Counter({1: 'a', 2: 'b'})
cnt_up.update({1: 'ww', 2: 'uu'})  # Counter({1: 'wwa', 2: 'uub'})


"""
Доступ к элементам и итерирование по Counter словарям работает так же, как и у обычных словарей. 
Мы можем перебирать ключи напрямую или можем использовать словарные методы items(), keys() и values().

Для удаления всех элементов из Counter словаря используется метод clear()
"""

"""
Объекты типа Counter можно сравнивать между собой. 
Равные объекты имеют одинаковое количество элементов и содержат равные элементы (ключ: количество)
"""
from collections import Counter

counter1 = Counter({'i': 4, 's': 4, 'p': 2})
counter2 = Counter(s=4, i=4, p=2)
print(counter1 == counter2)  # True



"""   *   *   *   Task   *   *   *   """

#  6.7-1
"""
Список files, содержит названия различных файлов. 
Вывести все расширения файлов, присутствующие в списке files, 
указав для каждого количество файлов с данным расширением. 
Расширения должны быть расположены в лексикографическом порядке
"""
from collections import Counter

files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
         'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
         'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
         'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
         'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
         'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
         'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
         'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
         'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
         'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
         'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
         'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
         'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']

# res = Counter([el.split('.')[-1] for el in files])
res = Counter(map(lambda el: el.split('.')[-1], files))
for el in sorted(res.items()):
    print(f"{el[0]}: {el[1]}")
    # csv: 5
    # exe: 12
    # jpeg: 7
    # ...
    # zip: 4


#  6.7-2
"""
Реализуйте функцию count_occurences(), которая принимает два аргумента в следующем порядке:
word — слово
words — последовательность слов, разделенных пробелом
Функция должна определять, сколько раз слово word встречается в последовательности words,
и возвращать полученный результат.
"""
from collections import Counter

def count_occurences(word: str, words: str) -> int:
    cnt = Counter(words.lower().split())
    return cnt[word.lower()]

# word = 'Se'
# words = 'se sdsf sds SE sdfsdg Se dhgf gfd asd se'
# print(count_occurences(word, words))  # 4


#  6.7-3
"""
На вход программе подается последовательность товаров, разделенных запятой без пробелов.
вывести все введенные товары, указывая для каждого, 
сколько раз он встречается в данной последовательности. 
Товары должны быть расположены в лексикографическом порядке, каждый на отдельной строке, 
в следующем формате:  <товар>: <количество>
"""
from collections import Counter

# лимон,лимон,лимон,груша,банан,банан,киви,киви,киви,киви

goods = Counter(input().split(','))
for k, v in sorted(goods.items()):
    print(f"{k}: {v}")


#  6.7-4
"""
А сколько стоит курс?
https://stepik.org/lesson/590120/step/18?unit=585064
Input:  лимон,лимон,лимон,груша,банан,банан,киви,киви,киви,киви
Output: банан: 5387 UC x 2 = 10774 UC
        груша: 5422 UC x 1 = 5422 UC
        киви : 4316 UC x 4 = 17264 UC
        лимон: 5418 UC x 3 = 16254 UC
"""
from collections import Counter

def get_unicode(word: str) -> int:
    return sum(map(ord, filter(str.isalpha, word)))
    # return sum(ord(el) for el in word if el.isalpha())

goods = Counter(input().split(','))
left = max(len(el) for el in goods)
for k, v in sorted(goods.items()):
    num = get_unicode(k)
    print(f"{k.ljust(left)}: {num} UC x {v} = {num * v} UC")



#  6.7-5
"""
The Zen of Python
https://stepik.org/lesson/590120/step/19?unit=585064
Input:  *
Output: *
"""
from collections import Counter

with open('pythonzen.txt', encoding='utf-8') as file:
    cnt = Counter(filter(str.isalpha, file.read().lower()))
for el in sorted(cnt):
    print(f"{el}: {cnt[el]}")


# Вариант
cnt = Counter()
with open('pythonzen.txt', encoding='utf-8') as file:
    for el in file.read():
        if el.isalpha():
            cnt.update(el.lower())
for k, v in sorted(cnt.items()):
    print(f"{k}: {v}")

