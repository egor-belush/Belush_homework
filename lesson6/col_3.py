"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.

"""

d = {'one': 11, 'two': 22, 'hello': 'python', True: False}

# Показываем словарь с номерами
print("Текущий словарь:")
i = 1
for key in d:
    print(f"{i}. {key} -> {d[key]}")
    i += 1

# Запрашиваем номер элемента для удаления
nomer = int(input("\nВведите номер элемента для удаления: "))

# Находим ключ по номеру и удаляем
i = 1
udalit_key = None
for key in d:
    if i == nomer:
        udalit_key = key
        break
    i += 1

# Удаляем элемент
if udalit_key is not None:
    del d[udalit_key]
    print(f"Элемент с номером {nomer} удален!")
else:
    print("Такого номера нет!")

# Показываем обновленный словарь
print("\nОбновленный словарь:")
i = 1
for key in d:
    print(f"{i}. {key} -> {d[key]}")
    i += 1