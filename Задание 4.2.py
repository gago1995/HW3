def my_func(x, y):
    n = 2
    y = abs(y)
    result = 1/x
    while n <= y:
        result = result*(1/x)
        n = n + 1
        continue
    return result
x = int(input('Введите положительное число'))
if x <= 0:
    print('Вы ввели отрицательное число или 0, нужно положительное')
else:
    y = int(input('Введите отрицательную степень число'))
    if y >= 0:
        print('Степень должна быть отрицательной и не должна быть 0')
    else:
        print(round(my_func(x,y), 10))