"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""

users = [
    {"name": "Иван", "login": "ivanov", "password": "123"},
    {"name": "Мария", "login": "masha", "password": "qwerty123"},
    {"name": "Алексей", "login": "alex", "password": "pass"},
    {"name": "Ольга", "login": "olya", "password": "password123"},
    {"name": "Петр", "login": "peter", "password": "1234"},
    {"name": "Анна", "login": "anna", "password": "ann"}
]

# Фильтруем пользователей с паролем менее 5 символов
weak_passwords = list(filter(lambda user: len(user["password"]) < 5, users))

print("Пользователи со слабыми паролями (<5 символов):")
for user in weak_passwords:
    print(f"Имя: {user['name']}, Логин: {user['login']}, Пароль: {user['password']}")