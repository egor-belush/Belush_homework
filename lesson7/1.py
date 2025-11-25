"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.

"""

print("Введите оценки ученика (для завершения введите 0):")

total = 0    # Сумма оценок
count = 0    # Количество оценок

while True:
    try:
        grade = int(input("Оценка: "))
        
        if grade == 0:
            break
        
        if grade < 1 or grade > 10:
            print("Ошибка: оценка должна быть от 1 до 10")
            continue
        
        total += grade
        count += 1
        
    except ValueError:
        print("Ошибка: введите целое число")

if count > 0:
    average = total / count
    print(f"\nВсего оценок: {count}")
    print(f"Сумма оценок: {total}")
    print(f"Средний балл: {average:.2f}")
else:
    print("\nНе введено ни одной оценки")