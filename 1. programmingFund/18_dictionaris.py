# x = {1: 1, 2: 3, 3: 3}

# contains = 1 in x

# values = x.values()
# keys = x.keys()
# items = x.items()


# x = {2: 1, 3: 3}
# for key, value in x.items():
#     print(key, value)


# x = {2: 1, 3: 3}
# x[4] = x.get(4, 0) + 1   # get if key exists, create and give 0
# print(x)


# characters = {}
# string = "hello world"

# for chr in string:
#     characters[chr] = characters.get(chr, 0) + 1

# print(characters)


# counts = {}

# while True:
#     num = input("number (enter q to quit): ")

#     if num == "q":
#         break
#     elif not num.isdigit():
#         print("invalid input")
#         continue

#     num = int(num)
#     counts[num] = counts.get(num, 0) + 1

# print(counts)


# dictionary is more efficient than list
d = {"a": 1, "b": 1, "c": 2, "d": 1}
l = ["a", "b", "c", "d"]
