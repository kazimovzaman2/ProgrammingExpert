# with open("file2.txt", "r+") as file:
#     score = file.read()
#     new_score = int(score) + 1
#     file.seek(0)
#     file.write(str(new_score))


# with open("file2.txt", "r+") as file:
#     for i, line in enumerate(file):
#         print(line, end="")
#         if i == 2:
#             break



with open("file2.txt", "r+") as file:
    print(file.read(2))