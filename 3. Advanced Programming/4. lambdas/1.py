# func = lambda x, y, z = 0: print(x + y + z)
# func(1, 2, 4)


########

# def sorf_func(x):
#     return x[1]

# lst = [(1,2),  (5,-4), (3,4), (0,0)]
# lst.sort(key=lambda x: x[1])
# print(lst)

##########

mul = lambda x: lambda y: x * y

result = mul(2)
print(result(3))