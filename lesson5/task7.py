from json import dumps

infile = 'task7.txt'
outfile = 'task7.json'
mydict = [{}, {}]
with open(infile, encoding='utf-8') as myfile:
    lines = myfile.readlines()
for line in lines:
    name, type, revenue, expenses = line.split()
    mydict[0][type + ' ' + name] = float(revenue) - float(expenses)
mydict[1]['Mean Profit'] = round(sum(profit for i, profit in mydict[0].items() if profit > 0) / len(mydict[0]), 2)
print(mydict)
with open(outfile, 'w', encoding='utf-8') as myfile:
    myfile.write(dumps(mydict))