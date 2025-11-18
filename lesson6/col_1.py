"""
Запросить трижды ввод наименования товаров и их цену через пробел. 
"пример: 
>>>яблоко 10"
>>>груша 15
>>>малина 20
    
    - создать из введенных данных словарь где ключ это наименование, а цена значение
    - запросить имя товара, найти его в словаре, и вывести его цену, увеличенную на 15%. 
    - вывести сумму всех товаров

"""

products = {}

# Трижды запрашиваем ввод данных
for i in range(3):
    data = input(f"Введите товар и цену {i+1}: ").split()
    name = data[0]
    price = float(data[1])
    products[name] = price

print("\nСозданный словарь:")
print(products)

search_product = input("\nВведите имя товара для поиска: ")

# Находим товар и выводим цену +15%
if search_product in products:
    original_price = products[search_product]
    increased_price = original_price * 1.15
    print(f"Цена товара '{search_product}' с увеличением на 15%: {increased_price:.2f}")
else:
    print(f"Товар '{search_product}' не найден в словаре")

# Выводим сумму всех товаров
total_sum = sum(products.values())
print(f"\nСумма всех товаров: {total_sum:.2f}")