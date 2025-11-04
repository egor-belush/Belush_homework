number = input("Введите число: ")
num = int(number)
result = f"{num:,}".replace(",", " ")
print(result)