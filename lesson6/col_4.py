
cena = {
    'a': 10,
    'b': 20, 
    'c': 30,
    'd': 40
}

fraza = input("Введите кодовую фразу из 5 символов (только a,b,c,d): ")

# Проверяем что фраза состоит из 5 символов
if len(fraza) != 5:
    print("Ошибка: фраза должна быть из 5 символов!")
else:
    # Считаем общее количество очков
    vsego_ochkov = 0
    
    for bukva in fraza:
        if bukva in cena:
            vsego_ochkov += cena[bukva]
        else:
            print(f"Ошибка: символ '{bukva}' не разрешен!")
            vsego_ochkov = 0
            break
    
    if vsego_ochkov > 0:
        print(f"Общее количество очков: {vsego_ochkov}")