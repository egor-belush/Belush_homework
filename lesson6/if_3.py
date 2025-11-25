'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

# Находим наибольшее число
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"Наибольшее число: {largest}")