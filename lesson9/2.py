'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''

def factorial(n):
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


try:
    num = int(input("Введите число для вычисления факториала: "))
    print(f"{num}! = {factorial(num)}")
except ValueError as e:
    print(f"Ошибка: {e}")