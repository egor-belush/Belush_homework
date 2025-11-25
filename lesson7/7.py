"""
Запросить любое число не менее 10. 
Вывести на экран сумму квадратов каждой цифры составляющей это число. 
Например: дано 236 => 2*2 + 3*3 + 6*6 = 49 

"""


# Запрашиваем число
while True:
    try:
        number = int(input("Введите число не менее 10: "))
        if number >= 10:
            break
        else:
            print("Ошибка: число должно быть не менее 10")
    except ValueError:
        print("Ошибка: введите целое число")

# Вычисляем сумму квадратов
total = 0
for digit_char in str(number):
    digit = int(digit_char)
    total += digit * digit

print(f"Сумма квадратов цифр числа {number} равна: {total}")