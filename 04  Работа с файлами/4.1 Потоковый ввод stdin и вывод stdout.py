# 4.1 Потоковый ввод stdin и вывод stdout
""""""

### Потоковый ввод

"""
С помощью потока ввода (sys.stdin) 
можно в одну строчку кода прочитать весь пользовательский ввод в список.
"""
import sys

data = [line.strip() for line in sys.stdin]

data = list(map(str.strip, sys.stdin))



"""
Методы read() и readlines()

можно считать все строки из итератора (с сохранением символов перевода строки) в список 
с помощью метода readlines()
символ перехода на новую строку (\n) сохраняется в считанных строках.
"""
import sys

data = sys.stdin.readlines()


### Потоковый вывод
import sys

sys.stdout.write(str(17))     # преобразуем данные в строку






"""   *   *   *   Task   *   *   *   """



#  4.1-1
"""
На вход программе подается произвольное количество строк.
вывести все введенные строки, предварительно расположив в каждой строке все символы в обратном порядке.
"""
import sys

data = sys.stdin.readlines()
for el in data:
    print(el.strip()[::-1])

# Короче
import sys
print('\n'.join(el.strip()[::-1] for el in sys.stdin.readlines()))


#  4.1-2
"""
подается произвольное количество строк, в каждой строке записана дата в ISO формате (YYYY-MM-DD).
вывести единственное число — количество дней 
между максимальной и минимальной датами введенной последовательности.
Input:  2022-06-15
        2022-06-12
        2022-06-16
        2022-06-30
Output: 18
"""
import sys
from datetime import datetime

data = [datetime.strptime(el.strip(), '%Y-%m-%d') for el in sys.stdin]
res = (max(data) - min(data)).days
print(res)


# Вариант
import sys
from datetime import date

dates = [date(*map(int, d.split('-'))) for d in sys.stdin]
print((max(dates) - min(dates)).days)


# Нестандартное решение
# https://timeweb.com/ru/community/articles/chto-takoe-faylovyy-deskriptor-prostymi-slovami
from datetime import date
dates = [date(*map(int, d.split('-'))) for d in open(0)]
print((max(dates) - min(dates)).days)

#  4.1-3
"""
На вход программе подается произвольное количество строк, в каждой строке записано натуральное число — 
количество носков, которые вытащил один из игроков.
Программа должна определить победителя в игре, 
(побеждает тот, кто сделав последний ход, вытащил четное количество), и вывести его имя.
Игроки Анри и Дима. Первый ход делает Анри.
Input:  2
        58
Output: Дима
"""
import sys

data = sys.stdin.readlines()
if len(data) % 2:
    print('Дима' if int(data[-1]) % 2 else 'Анри')
else:
    print('Анри' if int(data[-1]) % 2 else 'Дима')

# Развернутое решение
data = sys.stdin.readlines()
if len(data) % 2:
    if int(data[-1]) % 2:
        print('Дима')
    else:
        print('Анри')
else:
    if int(data[-1]) % 2:
        print('Анри')
    else:
        print('Дима')


#  4.1-4
"""
Дан список чисел, каждое из которых — рост очередного ученика.
Определить рост самого низкого и самого высокого учеников, 
а также средний рост среди всех учеников.

Полученные результаты должны быть выведены в следующем формате:
Рост самого низкого ученика: <рост самого низкого ученика>
Рост самого высокого ученика: <рост самого высокого ученика>
Средний рост: <средний рост среди всех учеников>
Если на вход программе ничего не подается, то она должна выводить текст "нет учеников"
Input:  185
        170
        190
        155
        175
Output: Рост самого низкого ученика: 155
        Рост самого высокого ученика: 190
        Средний рост: 175.0
"""
import sys
from statistics import mean

data = list(map(int, sys.stdin.readlines()))

if len(data):
    data.sort()
    print(f"Рост самого низкого ученика: {data[0]}\n"
          f"Рост самого высокого ученика: {data[-1]}\n"
          f"Средний рост: {mean(data)}")
else:
    print("нет учеников")


#  4.1-5
"""
Дан блок кода на языке Python. Определить количество строк в данном коде, 
которые содержат в себе только комментарии. 
Если в строке помимо комментария имеется что-то еще, то такую строку учитывать не нужно.
Input:  
Output: 
"""
import sys

res = [el[0] == "#" for el in map(str.strip, sys.stdin)]
# Варианты
res = [el.lstrip()[0] == "#" for el in sys.stdin]
res = [el.lstrip()[0] == "#" for el in open(0)]
res = [el.lstrip().startswith('#') for el in sys.stdin]
print(sum(res))


#  4.1-6
"""
Дан блок кода на языке Python. Удалить все строки в данном коде, 
которые содержат в себе только комментарии. 
Если в строке помимо комментария имеется что-то еще, 
то такую строку учитывать не нужно.

Output: 
Вывести введенный блок кода, 
предварительно удалив из него все строки которые содержат в себе только комментарии.
"""
import sys

data = sys.stdin.readlines()
res = [el for el in data if not el.lstrip().startswith("#")]
[print(el.rstrip('\n')) for el in res]


#  4.1-7
"""
https://stepik.org/lesson/520159/step/16?unit=512678
Input:  
Output: 
"""
import sys

data = [el.strip().split(' / ') for el in sys.stdin.readlines()]
cat = data[-1][0]
res = [el for el in data[:-1] if el[1] == cat]
res.sort(key=lambda x: (x[2], x[0]))
[print(el[0]) for el in res]


#  4.1-8
"""
На вход программе подается произвольное количество строк (две или более), 
в каждой строке записана дата в формате DD.MM.YYYY
Программа должны вывести текст:
ASC, если даты в введенной последовательности расположены строго в порядке возрастания
DESC, если даты в введенной последовательности расположены строго в порядке убывания
MIX, если даты в введенной последовательности расположены ни в порядке возрастания, ни в порядке убывания
Input:  14.06.2022
        20.06.2022
        21.06.2022
Output: ASC
"""
import sys
from datetime import datetime

data = [datetime.strptime(el.strip(), "%d.%m.%Y") for el in sys.stdin.readlines()]

if all(data[el] < data[el + 1] for el in range(len(data) - 1)):
    print('ASC')
elif all(data[el] > data[el + 1] for el in range(len(data) - 1)):
    print('DESC')
else:
    print('MIX')


#  4.1-9
"""
На вход программе подается произвольное количество строк (не менее трёх), 
в каждой строке записано натуральное число — очередной член последовательности.
Программа должна вывести текст:
- Арифметическая прогрессия, если введенная последовательность чисел является арифметической прогрессией
- Геометрическая прогрессия, если введенная последовательность чисел является геометрической прогрессией
- Не прогрессия, если введенная последовательность чисел не является прогрессией
Input:  2
        4
        8   
Output: Геометрическая прогрессия
"""
import sys

# num = [int(el.strip()) for el in sys.stdin.readlines()]
num = list(map(int, sys.stdin.read().split('\n')))
a = num[1] - num[0]
g = num[1] / num[0]
if all((num[el + 1] - num[el]) == a for el in range(len(num) - 1)):
       print('Арифметическая прогрессия')
elif all((num[el + 1] / num[el]) == g for el in range(len(num) - 1)):
       print('Геометрическая прогрессия')
else:
       print('Не прогрессия')

