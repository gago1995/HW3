mylist = []
summa = 0
summa_break = 0
while True:
    mylist.extend(input('Введите числа через пробел для выхода нажмите N ').split())
    if 'N' in mylist:
        mylist = mylist [:mylist.index('N')]
        mylist = [int(x) for x in mylist]
        summa_break = sum(mylist)
        break
    else:
        try:
            mylist = [int(x) for x in mylist]
            summa = summa + sum(mylist)
            print(f'Сумма: {summa}')
            mylist = []
        except ValueError:
            print("Вы ввели не число! или ошиблись с символом выхода, введите заново")
print(f'Сумма: {summa + summa_break}')