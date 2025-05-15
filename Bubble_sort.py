def bubble_sort(items, comp=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        '''
        If no swaps occur during a certain pass,
        it means the list is already sorted,
        and the loop can be terminated early.
        '''
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items

items = [34, 73, 14, 5, 2, 88, 65, 90, 13]
print(bubble_sort(items))
