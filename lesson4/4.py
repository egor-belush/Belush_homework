s = "имя: Дмитрий, фамилия: Иванов, возраст: 18"
a = s.split(',')
name = a[0].split(':')[1].strip()
surname = a[1].split(':')[1].strip()
age = a[2].split(':')[1].strip()
print(f'- {name}\n- {surname}\n- {age}')