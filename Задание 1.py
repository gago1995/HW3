def my_func (x, y):
    return x / y
x = float(input('Введите число: '))
y = float(input('Введите число на которое поделить 1 число: '))
try:
    print('Результат деления: ', my_func(x, y))
except ZeroDivisionError:
    print('На ноль делить нельзя')