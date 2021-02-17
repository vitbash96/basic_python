from itertools import count, cycle

a = str(input('input "c" for count or "l" for loop:')).lower()

if a != 'c' and a != 'l':
    print('Wrong input')
    quit()
elif a == 'c':
    tmp = True
    while tmp == True:
        try:
            a = int(input('Enter an integer to start count from:'))
            tmp = False
        except:
            print('Wrong input! Try again')
    tmp = True
    while tmp:
        try:
            b = int(input('Enter count:'))
            tmp = False
        except:
            print('Wrong input! Try again')
    for i in count(a):
        if i < a + b:
            print(i, end=' ')
        else:
            break
elif a == 'l':
    tmp = True
    while tmp:
        try:
            a = int(input('Enter a number of reps:'))
            tmp = False
        except:
            print('Wrong input! Try again')
            tmp = True
    count = 0
    for i in cycle((1, 2, 3)):
        if count < a * 3:
            print(i, end=' ')
            count += 1
        else:
            break
