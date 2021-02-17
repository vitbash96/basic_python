def remove_rep(numbers):
    newlist = [i for i in numbers if numbers.count(i) < 2]
    return newlist


source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(remove_rep(source_list))