def my_func(a, b, c):
    if a >= b and b >= c:
        result = a + b
        return result
    elif a > b and b <= c:
        result = a + c
        return result
    else:
        result = b + c
        return result


a = int(input('Введите a'))
b = int(input('Введите b'))
c = int(input('Введите c'))
print(my_func(a=a, b=b, c=c))
