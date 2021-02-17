filename = 'payroll.txt'
min_wage = 20000
total_salary = 0
try:
    with open(filename, encoding='utf-8') as myfile:
        mylist = myfile.readlines()
except:
    print('Something went wrong')
print('The following employees receive less than 20,000:', end='\n')
for employee in mylist:
    name, salary = employee.split()
    try:
        salary = float(salary)
    except:
        continue
    if salary < min_wage:
        print(name, end='\n')
    total_salary += salary

print(f'Average salary is:', round(total_salary / len(mylist), 2))
