text = "Это тестовая <start>строка для изучения<end> строковых операций"
start_pos = text.find("<start>") + len("<start>")
end_pos = text.find("<end>")
result = text[start_pos:end_pos]
print(result)