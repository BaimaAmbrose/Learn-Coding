def complex_bubble_sort(items, comp=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items) - 1):
        swap = False
        for j in range(i, len(items) - i - 1):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swap = True
        if swap:
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swap = True
        if not swap:
            break
    return items


items = [32, 62, 47, 8, 6, 43, 24, 16, 54, 76, 25]
print(complex_bubble_sort(items))
