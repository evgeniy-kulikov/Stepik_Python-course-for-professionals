#  7.2 Обработка исключений


"""   *   *   *   Task   *   *   *   """


#  7.2-1
"""
"""
blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
              {'Likes': 13, 'Comments': 2, 'Shares': 1},
              {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
              {'Comments': 4, 'Shares': 2},
              {'Photos': 8, 'Comments': 1, 'Shares': 1},
              {'Photos': 3, 'Likes': 19, 'Comments': 3}]

total_likes = 0

for post in blog_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        total_likes -= 1

# for post in blog_posts:
#     total_likes += post['Likes']

print(total_likes)


#  7.2-2
"""
"""
food = ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except IndexError:
        fifth.append('_')

# for x in food:
#     fifth.append(x[4])

print(fifth)


#  7.2-3
"""
ZeroDivisionError
Input:  *
Output: *
"""
numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

remainders = []

for number in numbers:
    try:
        remainders.append(36 % number)
    except ZeroDivisionError:
        pass
        # continue

# for number in numbers:
#     remainders.append(36 % number)

print(remainders)


#  7.2-4
"""
Only numbers
На вход программе подается неопределенное количество строк (хотя бы одна), 
каждая из которых содержит произвольное значение.
вывести сумму всех введенных чисел (тип int и float), 
а затем на следующей строке — количество введенных нечисловых значений.
Input:  10
        10
Output: 20
        0
"""
import sys
data = list(map(str.strip, sys.stdin))
res, bag = 0, 0

for el in data:
    try:
        res += int(el)
    except (ValueError, TypeError):
        try:
            res += float(el)
        except (ValueError, TypeError):
            bag += 1

print(res, bag, sep='\n')



import sys
data = list(map(str.strip, sys.stdin))
res, bag = 0, 0

for el in data:
    if el.isdecimal():
        res += int(el)
    else:
        try:
            res += float(el)
        except (ValueError, TypeError):
            bag += 1

print(res, bag, sep='\n')

