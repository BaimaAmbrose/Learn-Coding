def bubble_sort(items):
    for i in range(len(items) - 1):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


items = [34, 73, 14, 5, 2, 88, 65, 90, 13]
print(bubble_sort(items))
