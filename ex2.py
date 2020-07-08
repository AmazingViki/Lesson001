userdata = int(input('Введите количество секунд >>> '))
hours = userdata // 3600
min = (userdata - hours * 3600) // 60
sec = userdata % 60
print(f'{hours}:{min}:{sec}')
