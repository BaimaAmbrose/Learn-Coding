def liner_seearch(items, key):
    for index, item in enumerate(items):  ## enumerate() iterates over both the index and the value of the list at the same time.
        if item == key:
            return index, item
    return -1


items = [2, 4, 1, 5, 7, 5, 8]
key = 1
print(liner_seearch(items, key))
