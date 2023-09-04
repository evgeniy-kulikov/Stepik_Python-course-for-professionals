# 2.2 Повторяем основные конструкции языка Python. Часть 2
""""""


# Test 01
"""
На вход программе подаются 
3 натуральных числа :
d1, d2, d3 - длины дорожек, каждое на отдельной строке:
d1 - длина дорожки, соединяющая дом и первый магазин
d2 - длина дорожки, соединяющая дом и второй магазин
d3 - длина дорожки, соединяющая магазины
Найти минимальное расстояние, которое придётся пройти , чтобы посетить оба магазина и вернуться домой.

Input:  10
        10
        45
Output: 40
"""
d1, d2, d3 = (int(input()) for _ in range(3))
v1 = 2 * (d1 + d2)
v2 = 2 * (d1 + d3)
v3 = 2 * (d2 + d3)
v4 = d1 + d2 + d3
print(min(v1, v2, v3, v4))

# Вариант
# Двойная сумма двух самых коротких путей должна быть меньше суммы всех трех, иначе сумма трех
lst = sorted([int(input()) for _ in range(3)])
if sum(lst[:2]) * 2 < sum(lst):
    print(sum(lst[:2]) * 2)
else:
    print(sum(lst))


# Test 02
"""
В русском и английском языках есть буквы, которые выглядят одинаково. 
Вот список английских букв "AaBCcEeHKMOoPpTXxy", 
а вот их русские аналоги "АаВСсЕеНКМОоРрТХху". 
Напишите программу, которая для трёх букв из данных списков букв определяет, 
русские они, английские или и те и другие (смесь русских и английских букв).

На вход программе подаются три буквы из указанных в условии наборов букв, каждая на отдельной строке.

вывести:
ru - если все три буквы русские
en - если все три буквы английские
mix - если среди букв есть как русские, так и английские
"""

letters = [input() for _ in range(3)]
ru = 'АаВСсЕеНКМОоРрТХху'
en = 'AaBCcEeHKMOoPpTXxy'
cnt = 0

for el in letters:
    if el in en:
        cnt += 1

if cnt == 0:
    print('ru')
elif cnt == 3:
    print('en')
else:
    print('mix')


# Вариант преподавателя
langs = ['ru', 'mix', 'mix', 'en']
en = 'AaBCcEeHKMOoPpTXxy'
inx = sum(input() in en for _ in range(3))
print(langs[inx])


# Вариант через функцию all()
letters = [input() for _ in range(3)]
if all(map(lambda x: x in 'АаВСсЕеНКМОоРрТХху', letters)):
    print('ru')
elif all(map(lambda x: x in 'AaBCcEeHKMOoPpTXxy', letters)):
    print('en')
else:
    print('mix')


# Вариант через функцию ord()
# английский алфавит в таблице символов Unicode находятся в диапазоне от 65 до 121 включительно
# русский алфавит в таблице символов Unicode находятся в диапазоне от 1040 до 1093 включительно
letters = [ord(input()) for _ in range(3)]
if max(letters) <= 121:
    print('en')
elif min(letters) >= 1040:
    print('ru')
else:
    print('mix')


# Test 03
"""
Переворатор
https://stepik.org/lesson/569749/step/3?unit=564263
Дана последовательность натуральных чисел от 1 до n включительно. 
Напишите программу, которая сначала располагает в обратном порядке 
часть элементов этой последовательности от элемента с номером X до элемента с номером Y, 
а затем от элемента с номером A до элемента с номером B.

Input:  9 2 5 6 9
Output: 1 5 4 3 2 9 8 7 6
"""
n, x, y, a, b = list(map(int, input().split()))
ls = list(map(int, range(1, n + 1)))
ls[x - 1:y] = ls[x - 1:y][::-1]
ls[a - 1:b] = ls[a - 1:b][::-1]
[print(el, end=' ') for el in ls]

# Вариант преподавателя
n, x, y, a, b = [int(i) for i in input().split()]
nums = list(range(1, n + 1))
nums[x - 1:y] = reversed(nums[x - 1:y])
nums[a - 1:b] = reversed(nums[a - 1:b])
print(*nums)


# Test 04
"""
Дана последовательность неотрицательных целых чисел. 
Напишите программу, которая выводит те числа, которые встречаются в данной последовательности более одного раза.
Числа должны быть расположены в порядке возрастания и не должны повторяться.

Input:  4 8 0 3 4 2 0 3
Output: 0 3 4
"""
# ls_num = list(map(int, input().split()))
# ls = [el for el in set(ls_num) if ls_num.count(el) > 1]
# print(*sorted(ls))


# Вариант преподавателя
ls_num = [int(i) for i in input().split()]
ls = filter(lambda i: ls_num.count(i) > 1, set(ls_num))
print(*sorted(ls))


# Test 05
"""
https://stepik.org/lesson/569749/step/5?thread=solutions&unit=564263
Максимальная группа
Дана последовательность натуральных чисел от 1 до n включительно. 
Напишите программу, которая группирует все числа данной последовательности по сумме их цифр 
и определяет длину группы, содержащей наибольшее количество чисел.
Input:  Запишем последовательность чисел от 1 до 20
Output: (1,10), (2,11,20), (3,12),(4,13), (5,14),(6,15), (7,16), (8,17), (9,18), (19)
        3
"""

n = int(input())  # 20
ls = list(map(str, range(1, n + 1)))
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
ls_sum = [sum(map(int, list(el))) for el in ls]  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]
ls_cnt = [ls_sum.count(el) for el in set(ls_sum)]  # [2, 3, 2, 2, 2, 2, 2, 2, 2, 1]
print(max(ls_cnt))  # 3


# Вариант через словарь
n = int(input())
d = {}

for i in range(1, n + 1):
    s = sum([int(el) for el in str(i)])
    d[s] = d.get(s, 0) + 1
# {1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 1}
print(max(d.values()))


# Test 06
"""
Трудности перевода
https://stepik.org/lesson/569749/step/6?unit=564263
Input:  6
        испанский, португальский, эсперанто, французский
        французский, испанский, эсперанто
        португальский, эсперанто, французский, испанский
        французский, английский, болгарский, испанский, эсперанто
        эсперанто, английский, русский, испанский, французский
        python, испанский, эсперанто, латышский, польский, французский
Output: испанский, французский, эсперанто

Output: Сериал снять не удастся
"""
n = int(input())
lang_in = [input().split(', ') for _ in range(n)]
lang_total = [el for row in lang_in for el in row]
res = set([el for el in lang_total if lang_total.count(el) == n])
if res:
    print(', '.join(sorted(res)))
else:
    print('Сериал снять не удастся')

# Вариант преподавателя
n = int(input())
langs = set(input().split(', '))
for _ in range(n - 1):
    langs &= set(input().split(', '))

if langs:
    print(*sorted(langs), sep=', ')
else:
    print('Фильм снять не удастся')


# Вариант
n = int(input())
l = [set(input().split(', ')) for _ in range(n)]  # список 'n' множеств
intersect = set.intersection(*l)  # пересечение 'n' множеств (общее для всех)
if intersect:
    print(*sorted(intersect), sep=', ')
else:
    print('Сериал снять не удастся')


# Test 7
"""
Напишите программу, которая находит все схожие слова для заданного слова. 
Слова называются схожими, если имеют одинаковое количество и расположение гласных букв. 
При этом сами гласные могут различаться.
На вход программе подается одно слово, записанное в первой строке, 
затем натуральное число n — количество слов для сравнения и n строк со словами.
Программа должна вывести все схожие слова для заданного слова, сохранив их исходный порядок следования.
    Примечание 1. После последней гласной в начальном и проверяемом слове может быть любое количество согласных.
    Примечание 2. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е)
    и 21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).
Input:  машина
        8
        сеть
        машинист
        дорога
        урок
        работа
        аксиома
        железо
        ветеран
Output: машинист
        дорога
        работа
        железо
        ветеран
"""

str_vov = 'ауоыиэяюёе'
word_idx = [i for i, s in enumerate(input()) if s in str_vov]  # [1, 3, 5]
ls = [input() for _ in range(int(input()))]  # ['сеть', 'машинист', 'дорога', 'урок', 'работа', 'аксиома', 'железо', 'ветеран']

def get_world(world: str, lst: list) -> bool:
    cnt = 0
    for s in world:
        if s in str_vov:
            cnt += 1
    if cnt == len(lst):
        for idx in lst:
            if world[idx] in str_vov:
                cnt -= 1
    return not cnt

res = [print(el, end='\n') for el in ls if get_world(el, word_idx)]


# Вариант преподавателя
vowels = 'ауоыиэяюёе'
pattern = [i for i, c in enumerate(input()) if c in vowels]  # [1, 3, 5]


for _ in range(int(input())):
    word = input()
    if [i for i, c in enumerate(word) if c in vowels] == pattern:
        print(word)


# # Test 8
"""
Корпоративная почта 
https://stepik.org/lesson/569749/step/8?unit=564263
Input:  6
        ivan-petrov@beegeek.bzz
        petr-ivanov@beegeek.bzz
        ivan-petrov1@beegeek.bzz
        ivan-ivanov@beegeek.bzz
        ivan-ivanov1@beegeek.bzz
        ivan-ivanov2@beegeek.bzz
        3
        ivan-ivanov
        petr-petrov
        petr-ivanov
Output:     ivan-ivanov3@beegeek.bzz
            petr-petrov@beegeek.bzz
            petr-ivanov1@beegeek.bzz
"""

"""
timyr-guev@beegeek.bzz
timyr-guev1@beegeek.bzz
anri-tabuev1@beegeek.bzz
"""

old_lst = [input() for _ in range(int(input()))]
new_lst = [input() for _ in range(int(input()))]

for el in new_lst:
    cnt = 1
    if el + '@beegeek.bzz' not in old_lst:
        old_lst.append(el + '@beegeek.bzz')
        print(el + '@beegeek.bzz')
    else:
        while el + str(cnt) + '@beegeek.bzz' in old_lst:
            cnt += 1
        else:
            old_lst.append(el + str(cnt) + '@beegeek.bzz')
            print(el + str(cnt) + '@beegeek.bzz')


# Вариант преподавателя
digits, names = '0123456789', []

for _ in range(int(input())):
    name, _ = input().split('@')
    names.append(name)

for _ in range(int(input())):
    name = input()
    cnt = 1
    while name in names:
        name = name.rstrip(digits) + str(cnt)
        cnt += 1
    names.append(name)
    print(f'{name}@beegeek.bzz')

# Test 9
"""
Файлы в файле
https://stepik.org/lesson/569749/step/9?unit=564263
сервис для сравнения текстов:
http://text.num2word.ru/

"""
# Через словари
dct = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3}  # размерности
with open('files.txt', 'r', encoding='utf-8') as file:
    d_name = {}  # {расширение: [имена файлов]}
    d_size = {}  # {расширение: суммарный объем}
    for f in file:
        a, b, x, y = f.replace('.', ' ').split()  # abc.csv 22 KB -> a='abc', b='csv', x='22', y='KB'
        d_name.setdefault(b, []).append('.'.join([a, b]))
        d_size[b] = d_size.get(b, 0) + int(x) * dct[y]

    for el in sorted(d_name):
        print(*sorted(d_name[el]), sep='\n')  # печать группы файлов (с сортировкой)
        print('-' * 10)
        idx = 0
        while d_size[el] // 1024 > 0:
            d_size[el] /= 1024
            idx += 1  # нахождение размерности для данной группы файлов
        print('Summary:', round(d_size[el]), ['B', 'KB', 'MB', 'GB'][idx], end="\n\n")


# Длинное решение
def sum_weights(weights: list) -> str:
    """
    Перевод всех размеров файлов в наименьшую ед. измерения (B)
    - Суммирование ед. измерения
    - Постепенный перевод во всё большие ед. измерения по математическому округлению.
    - Таким образом определяется итоговый вес всех файлов этой группы
    """
    total = [0, 'B']
    # Перевод в Байты с суммированием
    for weight in weights:
        if weight[1] == 'B':
            total[0] += int(weight[0])
        elif weight[1] == 'KB':
            total[0] += int(weight[0]) * 1024
        elif weight[1] == 'MB':
            total[0] += int(weight[0]) * 1024 ** 2
        elif weight[1] == 'GB':
            total[0] += int(weight[0]) * 1024 ** 3
    # Перевод Байт в большую меру
    if total[0] >= 1024:
        total[0] = round(total[0] / 1024)
        total[1] = 'KB'
    if total[0] >= 1024:
        total[0] = round(total[0] / 1024)
        total[1] = 'MB'
    if total[0] >= 1024:
        total[0] = round(total[0] / 1024)
        total[1] = 'GB'
    return f'{total[0]} {total[1]}'


extensions_d = dict()  # Словарь. Ключ - расширение, Значение - список файлов

with open('files.txt', 'r', encoding='utf-8') as f:
    for line in f:  # Чтение всего файла по строкам
        line = line.rstrip()
        ext = line[line.find('.'):line.find(' ')]  # получить расширение файла
        extensions_d.setdefault(ext, []).append(line)

weights = []  # Веса (общий размер файлов) в текущей группе
keys_order = sorted(extensions_d.keys())  # Сортированный список расширений

for key in keys_order:
    extensions_d[key] = sorted(extensions_d[key])
    for value in extensions_d[key]:
        print(value[:value.find(' ')])  # Вывод файла без веса
        weights.append(value[value.find(' ') + 1::].split())  # Сохранение веса файла
    print("-" * 10)
    print(f'Summary: {sum_weights(weights)}', end="\n\n")
    weights = []  # Сброс накопленных весов
