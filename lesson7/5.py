'''

Дан списк:
['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
Для каждого элемента в списке 
    - вывести на экран сначала номер элемента 
    - сам элемент 
    - символ данного элемента, соответствующий номеру его позиции в списке. 
Образец:
1 - qwertyu - q
2 - asdfggh - s
3 - zxcvbnm - c
и так далее...


'''

words = ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']

# Проходим по каждому элементу списка
for i in range(len(words)):
    
    word = words[i]  # Получаем текущее слово
    character = word[i]  # Получаем символ, соответствующий номеру позиции в списке
    
    # Выводим результат (i+1 потому что нумерация с 1)
    print(f"{i+1} - {word} - {character}")