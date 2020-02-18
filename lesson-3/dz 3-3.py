def sum_of_max(a, b, c):
    num_list = sorted([a, b, c], reverse=True)
    return num_list[0]+num_list[1]


print(sum_of_max(9, 20, 15))
