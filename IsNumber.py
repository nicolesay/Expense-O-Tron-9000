def IsNumber():
    i_amount = 0
    while True:
        try:
            i_amount += float(input('Enter Amount of Transaction > '))
            return i_amount
        except ValueError:
            print('Must be a Number!')
            continue