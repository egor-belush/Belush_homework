'''
Дан список
['samsung', 'lg', 'xerox', 'bosch']
Удалить элемент с именем 'xerox'
Добавить элемент на 2 место 'indesit'

'''

companies = ['samsung', 'lg', 'xerox', 'bosch']
print("Исходный список:", companies)

companies.remove('xerox')
print("После удаления 'xerox':", companies)

companies.insert(1, 'indesit')
print("После добавления 'indesit' на 2 место:", companies)