with open("file.txt", "r") as file:
    line1 = file.readlines()[0]
    print([line1.strip()])
