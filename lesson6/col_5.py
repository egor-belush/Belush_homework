phrase = input("Введите фразу: ")

# 1. Подсчет уникальных символов
unique_chars = set(phrase)
print(f"Количество уникальных символов: {len(unique_chars)}")

# 2. Подсчет уникальных слов
# Приводим к нижнему регистру и разбиваем на слова
words = phrase.lower().split()
unique_words = set(words)
print(f"Количество уникальных слов: {len(unique_words)}")