filename = 'task5.txt'
tmp = True
while tmp:
    try:
        userinput = str(input("Enter some numbers separated by a space:"))
        check = [float(i) for i in userinput.split()]
        tmp = False
    except:
        print('Wrong input')
with open(filename, 'w', encoding='utf-8') as myfile:
    myfile.write(userinput)
with open(filename, encoding='utf-8') as myfile:
    tmp = myfile.read()
    mynumbers = [float(i) for i in tmp.split()]
print(f'The sum of the entered numbers is: {sum(mynumbers)}')
