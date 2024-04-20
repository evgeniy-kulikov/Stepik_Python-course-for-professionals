# 6.5 Тип данных defaultdict
""""""

"""
Функция defaultdict() принимает в качестве аргумента тип элемента по умолчанию. 
Таким образом, для ключей, к которым происходит обращение, 
словарь defaultdict поставит в соответствие дефолтный элемент данного типа:

для int – число 0
для float – число 0.0
для bool – значение False
для str – пустая строка ''
для list – пустой список []
для tuple – пустой кортеж ()
для set – пустое множество set()
для dict – пустой словарь {}
"""
from collections import defaultdict

data = defaultdict(int)       # создаем словарь со значением по умолчанию 0

data['name'] = 'Tom'
data['age'] = 23

print(data['salary'])   # 0
print(data)             # defaultdict(<class 'int'>, {'name': 'Tom', 'age': 23, 'salary': 0})

"""
Помимо первого аргумента – типа элемента по умолчанию – можно передать второй аргумент: словарь, 
на основании которого будет создан defaultdict.
"""
from collections import defaultdict

info = defaultdict(int, {'name': 'Tom', 'age': 23})

print(info['name'])     # Tom
print(info['salary'])   # 0
print(info)             # defaultdict(<class 'int'>, {'name': 'Tom', 'age': 23, 'salary': 0})


"""
Также допустимы все способы, которые используются при создании обычных словарей, 
а именно передача именованных аргументов или итерируемого объекта, 
содержащего пары ключ-значение (например, список кортежей).
"""
from collections import defaultdict

info1 = defaultdict(int, name='Tom', age=32)
info2 = defaultdict(int, [('name', 'Tom'), ('age', 32)])

print(info1)    # defaultdict(<class 'int'>, {'name': 'Tom', 'age': 23, 'salary': 0})
print(info2)    # defaultdict(<class 'int'>, {'name': 'Tom', 'age': 23, 'salary': 0})


"""
при создании словаря defaultdict мы можем указать только именованные аргументы, 
но не можем указать только итерируемый объект с парами ключ-значение (или словарь).
"""
from collections import defaultdict

info3 = defaultdict(name='Tom', age=23)
print(info3)     # defaultdict(None, {'name': 'Tom', 'age': 23})

info4 = defaultdict([('name', 'Tom'), ('age', 23)])
print(info4)    # TypeError: first argument must be callable or None


"""
При создании defaultdict словаря можно указывать 
не только тип данных для значений по умолчанию, но и любую функцию, 
не принимающую аргументов и возвращающую некоторое дефолтное значение.
"""
from collections import defaultdict

def get_default():
    return 'any value', 10

info = defaultdict(get_default, {'name': 'Tom', 'age': 23})
print(info['name'])     # Tom
print(info['salary'])   # ('any value', 10)



info = defaultdict(lambda: 'any value', {'name': 'Tom', 'age': 23})
print(info['name'])     # Tom
print(info['salary'])   # 'any value'


"""
Функцию, которая возвращает значение по умолчанию для отсутствующих ключей, 
можно явно менять через атрибут default_factory
"""
from collections import defaultdict

data = defaultdict(int)
print(data['salary1'])  # 0

data.default_factory = list
print(data['salary2'])  # []

data.default_factory = float
print(data['salary3'])  # 0.0


"""   *   *   *   Task   *   *   *   """


#  6.5-1
"""
https://stepik.org/lesson/590035/step/19?unit=584967
Input:  data
Output: Books: $7969
        Courses: $2991
        Merch: $4083
        Tutorials: $373
"""
from collections import defaultdict

data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061),
        ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041),
        ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729),
        ('Tutorials', 977), ('Books', 656)]

res = defaultdict(int)

for el in data:
        res[el[0]] += el[1]

for el in sorted(res.items()):
        print(f"{el[0]}: ${el[1]}")


#  6.5-2
"""
https://stepik.org/lesson/590035/step/20?unit=584967
Input:  staff
Output: Accounting: 17
        Developing: 7
        Marketing: 13
        Sales: 13
"""
from collections import defaultdict

staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'),
         ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'),
         ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'),
         ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'),
         ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'),
         ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'),
         ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'),
         ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'),
         ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'),
         ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'),
         ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'),
         ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'),
         ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'),
         ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'),
         ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'),
         ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'),
         ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]

res = defaultdict(int)

for el in staff:
    res[el[0]] += 1

for el in sorted(res.items()):
    print(f"{el[0]}: {el[1]}")


#  6.5-3
"""
https://stepik.org/lesson/590035/step/21?unit=584967
Input:  staff_broken
Output: Accounting: Aaron Ferguson, Ann Bell, Brenda Davis, Casey Jenkins, Craig Wood, ..., Steven Diaz
        Developing: Arlene Gibson, Deborah George, Joyce Rivera, Miguel Norris, Nicole Watts, ..., Wilma Woods
        Marketing: Andrew Clark, Bernice Ramos, Billy Lloyd, Carol Peters, Charles Bailey, ..., Sam Davis
        Sales: Alicia Mendoza, Charlotte Cox, Chester Fernandez, Connie Reid, Evelyn Martin, ..., Robert Barnes

"""
from collections import defaultdict

staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'),
                ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'),
                ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'),
                ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'),
                ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'),
                ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'),
                ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'),
                ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'),
                ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'),
                ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'),
                ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'),
                ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'),
                ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'),
                ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'),
                ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'),
                ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'),
                ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'),
                ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'),
                ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'),
                ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'),
                ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'),
                ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'),
                ('Accounting', 'Dale Houston')]

res = defaultdict(set)

for el in staff_broken:
    res[el[0]].add(el[1])

for el in sorted(res.items()):
    print(f"{el[0]}:", ', '.join(sorted(tuple(el[1]))))


#  6.5-4
"""
Функция wins()
https://stepik.org/lesson/590035/step/22?unit=584967
Input:  result
Output: Дима -> Артур
        Тимур -> Артур Дима
"""
from collections import defaultdict

def wins(pairs) -> dict:
    res = defaultdict(set)
    for el in pairs:
        res[el[0]].add(el[1])
    return res


def wins(pairs) -> dict:
    res = defaultdict(set)
    for winner, loser in pairs:
        res[winner].add(loser)
    return res

# result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])
#
# for winner, losers in sorted(result.items()):
#     print(winner, '->', *sorted(losers))


#  6.5-5
"""
flip_dict()
https://stepik.org/lesson/590035/step/23?unit=584967
{'a': [1, 2], 'b': [3, 1], 'c': [2]}
преобразовать (меняем ключ-значения)
{1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']}
Input:  *
Output: *
"""
from collections import defaultdict

def flip_dict(dict_of_lists: dict) -> dict:
    res = defaultdict(list)
    for key, val in dict_of_lists.items():
        for el in val:
            res[el].append(key)
            # res[el] += [key]
    return res

# print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))
# defaultdict(<class 'list'>, {1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']})


#  6.5-6
"""
best_sender()
https://stepik.org/lesson/590035/step/24?unit=584967
Реализуйте функцию best_sender(), которая принимает два аргумента в следующем порядке:

messages — список сообщений
senders — список имен отправителей
Функция должна определять отправителя, имеющего наибольшее количество слов, 
и возвращать его имя. Если таких отправителей несколько, 
следует вернуть имя того, чье имя больше в лексикографическом сравнении.
Input:  *
Output: *
"""
from collections import defaultdict

def best_sender(messages, senders):
    res = defaultdict(int)
    for i, el in enumerate(senders):
        res[el] += len(messages[i].split())
    users = sorted(res.items(), key=(lambda x: (x[1], x[0])))
    return users[-1][0]


# def best_sender(messages : list, senders : list) -> str:
#     res = defaultdict(int)
#     for el in range(len(senders)):
#         res[senders[el]] += len(messages[el].split())
#     users = sorted(res.items(), key=lambda x: (x[1], x[0]), reverse=True)
#     return users[0][0]

# messages = ['hi', 'hello', 'how r u', 'i am okay', 'how r u', 'i am okay too thanks']
# senders = ['Anri', 'Dima', 'Anri', 'Dima', 'Dima', 'Anri']
#
# print(best_sender(messages, senders))

