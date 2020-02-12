def my_func(x, y):
    result = x ** y
    return result
x = int(input('Введите положительное число: '))
if x <= 0:
    print('Вы ввели отрицательное число или 0, нужно положительное.')
else:
    y = int(input('Введите отрицательную степень число: '))
    if y >= 0:
        print('Степень должна быть отрицательной.')
    else:
        print(round(my_func(x,y), 10))