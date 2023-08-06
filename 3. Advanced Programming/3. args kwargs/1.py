# def sum_items(p1, p2, a, b, c):
#     print(a,b,c)
#     return a + b + c

# args = [1,2]
# kwargs = {"a": 1, "b": 2, "c": 3}
# x = sum_items(*args, **kwargs)
# print(x)




# values = [1,2,3, 4, 5, 6, 7, 8, 9, 10]
# print(*values)




def test(p1, *args, **kwargs):
    print(p1, args, kwargs)

values = [1,2,3, 4, 5, 6, 7, 8, 9, 10]
kwargs = {"a": 1, "b": 2, "c": 3}
test(1, *values, **kwargs)
