"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев


"""

def format_fio(full_name, reverse_order=False):

    # Разделяем строку на части
    parts = full_name.split()
    
    # Проверяем, что введены все три компонента
    if len(parts) != 3:
        raise ValueError("ФИО должно содержать фамилию, имя и отчество через пробел")
    
    surname, name, patronymic = parts
    
    # Формируем инициалы
    initials = f"{name[0]}.{patronymic[0]}."
    
    # Возвращаем в зависимости от порядка
    if reverse_order:
        return f"{initials}{surname}"
    else:
        return f"{surname} {initials}"


# Примеры использования
if __name__ == "__main__":
    # Тестовые данные
    test_name = "Николаев Иван Сергеевич"
    
    # Стандартный формат
    print(format_fio(test_name))  # Николаев И.С.
    
    # Обратный формат
    print(format_fio(test_name, reverse_order=True))  # И.С.Николаев
    
    # Еще примеры
    print(format_fio("Иванов Петр Васильевич"))  # Иванов П.В.
    print(format_fio("Иванов Петр Васильевич", True))  # П.В.Иванов
    
    # Пример с обработкой ошибки
    try:
        print(format_fio("Петров Иван"))  # Вызовет ошибку
    except ValueError as e:
        print(f"Ошибка: {e}")