while True:
    n = int(input('Введите положительное число >>> '))
    if 0 <= n < 10:
        nn = n + n * 10
        nnn = nn + n * 100
        print(n + nn + nnn)
        break
    elif n >= 10:
        nn = n + n * 100
        nnn = nn + n * 10000
        print(n + nn + nnn)
        break
    else:
        print('Нужно было ввести положительное число')
