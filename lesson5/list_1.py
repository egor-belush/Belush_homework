'''
Дан произвольный список. Вывести на экран в обратном порядке. 
Задачу решить 2мя способами. 
'''

my_list = [1, 2, 3, 4, 5,]

reversed_list = my_list.copy()
reversed_list.reverse()

print(f"Первый способ: {my_list[::-1]}")
print(f"Второй способ: {reversed_list}")