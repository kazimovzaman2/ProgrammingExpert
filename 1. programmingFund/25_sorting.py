# lst = [2, 3, 5, 1, 4]
# lst.sort(reverse=True)
# print(lst)


def sort_second_index(item):
    return item[1]


lst = [[1, 2], [3, 4], [5, 6], [-1, 5], [0, 0]]
lst.sort(key=sort_second_index)
print(lst)
