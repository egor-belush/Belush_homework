name = input('Введите имя: ')
text = "Юзер с именем <имя> заходил на сайт в 15:00"
result = text.replace('<имя>', name)
print(result)