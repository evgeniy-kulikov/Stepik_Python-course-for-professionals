""" Полезные решения"""
"""сортировка списка по длине строкового элемента"""
ls = ['dddd', 'a', 'bb', 'ccc']
ls_sort_len = sorted(ls, key=len)
# ['a', 'bb', 'ccc', 'dddd']
ls_sort_reverse = sorted(ls, key=len, reverse=True)
# ['dddd', 'a', 'bb', 'ccc']
