x = [1, 2, 3, 4, 5, "Hello"]

x.append("last element")
length = len(x)

# returns the index of the first occurrence of the element
index = x.index("Hello")


# removes the first occurrence of the element
x.remove(1)


list_contain_5 = 5 in x
list_contain_5 = x.count(5) > 0


print(list_contain_5)


# combine two lists
a = [1, 2, 3]
b = [4, 5, 6]
combined = a + b
x.extend(b)


# muliti dimensional lists

lst = [[1, 2, []], [4, 5, 6], [7, 8, 9]]
