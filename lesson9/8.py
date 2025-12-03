'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''

data = [1, "hello", True, 3.14, "world", False, [1, 2, 3], None, "python", 42]

# Оставляем только строки
strings_only = list(filter(lambda x: isinstance(x, str), data))
print("Только строки:", strings_only)

# Оставляем только логический тип (bool)
bools_only = list(filter(lambda x: isinstance(x, bool), data))
print("Только логический тип:", bools_only)