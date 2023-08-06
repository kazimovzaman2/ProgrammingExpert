# try:
#     2/0
#     int("aw")
# except Exception as e:
#     print('Exceprion! ', e)
# finally:
#     print('DOne')

# print("done`")


# raise ValueError("This is a error")


# num = input("Enter a number: ")
# if not num.isdigit():
#     raise ValueError("This is a error")

while True:
    num = input("Enter a number: ")
    try:
        num = float(num)
        break
    except ValueError as e:
        print("This is not a number")
