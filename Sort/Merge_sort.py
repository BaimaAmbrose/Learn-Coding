def merge_sort(items, comp=lambda x, y: x < y):
    return _merge_sort(items, comp)


def _merge_sort(items, comp):
    if len(items) < 2:
        return items
    mid = len(items) // 2
    leftItems = _merge_sort(items[:mid], comp)
    rightItems = _merge_sort(items[mid:], comp)
    return mergesort(leftItems, rightItems, comp)


def mergesort(leftItems, rightItems, comp):
    item = []
    index1, index2 = 0, 0
    while index1 < len(leftItems) and index2 < len(rightItems):
        if comp(leftItems[index1], rightItems[index2]):
            item.append(leftItems[index1])
            index1 += 1
        else:
            item.append(rightItems[index2])
            index2 += 1
    item += leftItems[index1:]
    item += rightItems[index2:]
    return item


items = [34, 73, 14, 5, 2, 88, 65, 90, 13]
print(merge_sort(items))
