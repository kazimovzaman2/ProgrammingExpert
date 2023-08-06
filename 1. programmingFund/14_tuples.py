x = (1, 2, 3, (1, 2), True, [])
y = (3, 5)
z = 6, 7, 8  # this is tuples too
p = (1, )  # one element tuple


count = x.count(1)
index = x.index(1)
contains = 1 in x
x[3][0]

combined = x + y
combined = x * 3


x = (1, 2, 3)
y = (x[0], 4, x[2])  # change the tuple
