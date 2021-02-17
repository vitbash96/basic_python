def show_big(somenumbers):
    finallist = []
    for i in range(1, len(somenumbers)):
        if somenumbers[i] > somenumbers[i - 1]:
            finallist.append(somenumbers[i])
    return finallist


original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(show_big(original_list))

### Alternative solution

print(list(original_list[i] for i in range(1, len(original_list)) if original_list[i] > original_list[i - 1]))
