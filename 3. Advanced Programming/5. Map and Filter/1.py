import math

lst = [[1,2,3], [4,5,6], [1,2,3], [3,4]]
# new_lst = list(map(lambda x: sum(x), lst))
# print(new_lst)

# new_lst = filter(lambda x: len(x) > 2, lst)
# print(new_lst)
# for el in new_lst:
#     print(el)

new_lst = filter(lambda y: y% 2 ==0, map(lambda x: sum(x), lst))
print(list(new_lst))

