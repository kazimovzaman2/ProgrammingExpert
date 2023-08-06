lst = [1, 2, 3, 4, 5, True, False]

# for i in range(len(lst)):
#     print(lst[i])


# for element in lst:
#     print(element)


# for i, element in enumerate(lst):
#     print(i, element)


# lst = [1, 2, 3, 4, 52, 1, 3, 4, 4]

# for num in lst:
#     if num == 4:
#         continue
#         # break
#     print(num)


# for i in range(10):
#     for j in range(10):
#         print(i, j)


# lst = [[1, 2], [3, 4], [5, 6], [7, 8]]

# for i in range(len(lst)):
#     interior_lst = lst[i]

#     for j in range(len(interior_lst)):
#         print(interior_lst[j])


# st = "hello world!"
# for i, char in enumerate(st):
#     if char == "w":
#         print(i)


# numbers = []
# for i in range(3):
#     num = input("add number: ")
#     numbers.append(num)

# print(numbers)

words = ("hello", "world", "!")
target = "world"
found = False

for word in words:
    if word == target:
        print("found")
        found = True
        break
else:
    print("not found")
