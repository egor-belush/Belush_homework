'''
Запросить фразу состоящую минимум из трех слов. 
Сформировать фразу из этих слов в которой каждая буква слова, 
продублирована то количество раз, которое соответствует номеру позиции 
данной буквы в слове этой буквы. 
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

'''

while True:
    phrase = input("Введите фразу из минимум 3 слов: ").strip()
    words = phrase.split()
    
    if len(words) >= 3:
        break
    else:
        print("Ошибка: фраза должна содержать минимум 3 слова")

# Обрабатываем каждое слово
result_words = []
i = 0
while i < len(words):
    word = words[i]
    new_word = ""
    
    # Обрабатываем каждую букву в слове
    j = 0
    while j < len(word):
        letter = word[j]
        # Дублируем букву (j+1) раз
        k = 0
        while k < (j + 1):
            new_word += letter
            k += 1
        j += 1
    
    result_words.append(new_word)
    i += 1

# Формируем итоговую фразу
result_phrase = ""
i = 0
while i < len(result_words):
    result_phrase += result_words[i]
    if i < len(result_words) - 1:
        result_phrase += " "
    i += 1

# Выводим результат
print("\nИсходная фраза:", phrase)
print("Результат:     ", result_phrase)