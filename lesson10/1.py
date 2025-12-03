'''
Добавить несколько черепах 
    - или сразу 
    * или в течении игры по одной через определенное количество кликов
    - на каждой забиндить клик через одну и туже функцию cath

'''

import turtle
import random

# Настройка экрана
screen = turtle.Screen()
screen.title("Ловля черепах")

# Счетчик кликов по экрану
click_count = 0

def catch(x, y):
    """Функция для обработки клика по черепахе"""
    # Находим черепаху, по которой кликнули
    for t in screen.turtles():
        if t.distance(x, y) < 20:  # Проверяем близость клика к черепахе
            t.hideturtle()  # Прячем черепаху
            t.clear()  # Очищаем следы
            break

def add_turtle_on_click(x, y):
    """Добавляет новую черепаху через определенное количество кликов"""
    global click_count
    click_count += 1
    
    # Добавляем новую черепаху каждые 3 кликов
    if click_count % 3 == 0:
        new_t = turtle.Turtle()
        new_t.shape("turtle")
        new_t.color(random.choice(["red", "green", "blue"]))
        new_t.penup()
        new_t.goto(random.randint(-200, 200), random.randint(-200, 200))
        new_t.onclick(catch)  # биндим функцию catch

# Создаем несколько черепах сразу
for _ in range(5):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(random.choice(["red", "green", "blue"]))
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.onclick(catch)  # биндим функцию catch

# Биндим клик по экрану для добавления черепах
screen.onclick(add_turtle_on_click)

turtle.mainloop()