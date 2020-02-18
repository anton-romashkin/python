source_list = [2, 4, 6, 4, 5, 12, 4, 112, 67, 33]
new_list = [source_list[i] for i in range(1, len(source_list)) if source_list[i] > source_list[i - 1]]
print(new_list)
