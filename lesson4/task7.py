from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)


tmp = True
while tmp:
    try:
        a = input('Enter a number:')
        a = int(a)
        print([el for el in fact(a)])
        tmp = False
    except:
        print('Wrong input!')
