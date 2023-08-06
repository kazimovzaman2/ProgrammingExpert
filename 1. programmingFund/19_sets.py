# x = {1, 2}

# x.add(6)
# x.remove(1)
# x.clear()
# length = len(x)

# contains = 1 in x

# y = {2, 3}
# z = x.union(y)
# z = x | y

# x = {1, 2, 3}
# y = {1, 2, 4}

# z = y.intersection(x)
# z = y & x

# z = x.difference(y)
# z = x - y

# z = x.symmetric_difference(y)
# z = x ^ y

# x.update(y)

# x.difference_update(y)
# x.symmetric_difference_update(y)

# print(x.issubset(y))
# print(x <= y)
# print(y.issuperset(x))
# print(y >= x)


# x = [1, 2, 3, 4, 5, 623, 2, 23, 3,]
# set_x = list(set(x))

# print(set_x)


numpers = set()

while True:
    num = int(input('Enter a number: '))

    if num in numpers:
        break

    numpers.add(num)
