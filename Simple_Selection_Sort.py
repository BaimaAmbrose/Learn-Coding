def select_sort(items): ## Simple Selection Sort
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if items[min_index] > items[j]:
                items[min_index], items[j] = items[j], items[min_index]
    return items
items = [1, 5, 3, 32, 65, 12, 7, 3, 2, 7, 45, ]
print(select_sort(items))