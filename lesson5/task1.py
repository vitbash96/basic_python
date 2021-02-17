filename = 'task1.txt'
while True:
    a = input('Enter arbitrary line (if empty or space - exit): ')
    if a == '' or a.isspace():
        break
    try:
        with open(filename, 'a', encoding='utf-8') as myfile:
            myfile.write(f'{a}\n')
    except:
        print('Something went wrong')
        break
