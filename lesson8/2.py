'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''

def rectangle_calculation(side_a, side_b, calculate_area=True):
    
    if calculate_area:
        # Вычисляем площадь: a * b
        return side_a * side_b
    else:
        # Вычисляем периметр: 2 * (a + b)
        return 2 * (side_a + side_b)


if __name__ == "__main__":
    # Тестовые данные
    a = 5
    b = 3
    
    # Площадь (по умолчанию)
    print(f"Площадь прямоугольника {a}x{b}: {rectangle_calculation(a, b)}")
    
    # Периметр
    print(f"Периметр прямоугольника {a}x{b}: {rectangle_calculation(a, b, False)}")
    
    # указание параметра для площади
    print(f"Площадь: {rectangle_calculation(a, b, calculate_area=True)}")
    
    # Дополнительные примеры
    print(f"Площадь 4x7: {rectangle_calculation(4, 7)}")
    print(f"Периметр 4x7: {rectangle_calculation(4, 7, False)}")