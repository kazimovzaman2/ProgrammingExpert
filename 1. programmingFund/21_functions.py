# def new_range(stop, start=0):
#     x = start
#     while x < stop:
#         print(x)
#         x += 1

# new_range(10)


# def return_values(x, y):
#     return x+1, y+1
# x, y = return_values(1, 2)
# print(x, y)


# def remove_char(base, chars=""):
#     new_string = base
#     for char in chars:
#         new_string = new_string.replace(char, "")
#     return new_string

# result = remove_char("hello world", "le")
# print(result)


def sum_lists(list1, list2):

    def sum_list(lst):
        total = 0
        for num in lst:
            total += num

        return total

    list1_sum = sum_list(list1)
    list2_sum = sum_list(list2)
    return list1_sum, list2_sum


sum1, sum2 = sum_lists([1, 2, 3], [4, 5, 6])
print(sum1, sum2)
