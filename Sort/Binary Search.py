def binary_search(items, key):
    starts, ends = 0, len(items) - 1
    while starts <= ends:
        mid = (starts + ends) // 2
        if key > items[mid]:
            starts = mid + 1
        elif key < items[mid]:
            ends = mid - 1
        else:
            return mid
    return -1


items = [1, 2, 4, 6, 7, 8, 12, 24]
print(binary_search(items, 5))
