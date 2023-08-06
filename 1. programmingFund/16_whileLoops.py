# x = 0
# while x < 5:
#     x += 1
#     print(x)


# num = input("enter a number: ")
# while not num.isdigit():
#     num = input("enter a number: ")


# while True:
#     num = input("enter a number: ")
#     if num.isdigit():
#         break


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
# resutl = 0
# i = 0
# while resutl < 9 and i < len(lst):
#     num = lst[i]
#     resutl += num
#     i += 1
#     print(num)


lst = [1, 2, 3, 4, 5, -2, 6, 7, 8, 9, -1]
i = 0
while i < len(lst):
    if lst[i] == -2:
        print('found')
        break
    i += 1
else:
    print('not found')
