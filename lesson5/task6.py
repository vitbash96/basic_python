import re
mydict = {}

with open('task6.txt', encoding='utf-8') as myfile:
    mylist=myfile.readlines()
for el in mylist:
    key, rest = el.split(':')
    mydict[key] = rest
for key, value in mydict.items():
    mydict[key] = re.findall(r'\d+', value)
    mydict[key] = [int(i) for i in mydict[key]]
    mydict[key] = sum(value for value in mydict[key])
print(mydict)