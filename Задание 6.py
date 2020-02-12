def my_func (work):
    work = work.title()
    return work
my_list = []
my_list.extend(input('Введите слова через пробел').split())
for el in my_list:
        print(my_func(el), end=" ")