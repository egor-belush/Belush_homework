"""
Запросить у пользователя год рождения и в соответствии с его возрастом 
охарактеризовать пользователя - 
ребенок, подросток, юноша, в расцвете сил, пожилой, старик.
"""

birth_year = int(input("Введите ваш год рождения: "))

# Получаем текущий год
from datetime import datetime
current_year = datetime.now().year

# Вычисляем возраст
age = current_year - birth_year

# Определяем возрастную категорию
if age < 0:
    category = "Вы еще не родились!"
elif age <= 12:
    category = "ребенок"
elif age <= 17:
    category = "подросток"
elif age <= 25:
    category = "юноша"
elif age <= 45:
    category = "в расцвете сил"
elif age <= 65:
    category = "пожилой"
else:
    category = "старик"

print(f"Ваш возраст: {age} лет")
print(f"Вы - {category}")