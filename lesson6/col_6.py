'''
Запросить 3 раза строку из нескольких чисел через пробел
    - вывести все уникальные числа по возрастанию
    - вывести числа которые есть в каждой строке
    -* вывести числа которые есть только в одной из трех строк
    
    выполнить без циклов и условий
    
    пример:
    >>> 1 2 11 22
    >>> 1 2 22 33
    >>> 1 2 33 44


    1) 1 2 11 22 33 44
    2) 1 2
    3) 11 44
    
'''

line1 = input().split()
line2 = input().split()
line3 = input().split()

# Преобразуем в множества чисел
set1 = set(map(int, line1))
set2 = set(map(int, line2))
set3 = set(map(int, line3))

# 1) Все уникальные числа по возрастанию
all_unique = sorted(set1 | set2 | set3)
print("1)", *all_unique)

# 2) Числа которые есть в каждой строке
common_all = sorted(set1 & set2 & set3)
print("2)", *common_all)

# 3) Числа которые есть только в одной из трех строк
only_in_one = sorted(
    (set1 - set2 - set3) | 
    (set2 - set1 - set3) | 
    (set3 - set1 - set2)
)
print("3)", *only_in_one)

