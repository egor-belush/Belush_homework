num = int(input('Введите число: '))
num1 = (num // 1000)        
num2 = (num // 100) % 10  
num3 = (num // 10) % 10   
num4 = num % 10           
print(f'Тысячи -', num1,'\n', 'Сотни -', num2, '\n', 'Десятки -', num3, '\n', 'Единицы -', num4, )