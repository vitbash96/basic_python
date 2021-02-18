in_filename = 'task4.txt'
out_filename = 'task4out.txt'
out = []
translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open(in_filename, encoding='utf-8') as myfile:
    lines = myfile.readlines()
    for line in lines:
        if line != '\n':
            out.append(line.split(' — '))
    for i, k in enumerate(out):
        for j, a in enumerate(k):
            if a in translator:
                out[i][j] = translator[a]

with open(out_filename, 'w') as outfile:
    for list in out:
        if len(list) == 2:
            list = [''.join(f'{list[0]} - {list[1]}')]
            for string in list:
                outfile.write(string + '\n')

