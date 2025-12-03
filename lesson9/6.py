"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""

temp_data = {"day1": 18, "day2": 22, "day3": 7, "day4": 11, "day5": 14}

# Сортировка по возрастанию температуры
ascending = dict(sorted(temp_data.items(), key=lambda item: item[1]))
print("По возрастанию:", ascending)

# Сортировка по убыванию температуры
descending = dict(sorted(temp_data.items(), key=lambda item: item[1], reverse=True))
print("По убыванию:   ", descending)