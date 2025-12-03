
"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial():
    n = 0
    result = 1
    
    while True:
        n += 1
        result *= n
        yield result


factorial_gen = factorial()

print("Нажмите Enter для получения следующего значения факториала.")
print("Введите 'стоп' для завершения.")

while True:
    user_input = input("> ")
    
    if user_input.lower() == 'стоп':
        print("Завершение работы.")
        break
    
    try:
        value = next(factorial_gen)
        print(f"next(factorial_gen) -> {value}")
    except StopIteration:
        print("Генератор завершил работу.")
        break