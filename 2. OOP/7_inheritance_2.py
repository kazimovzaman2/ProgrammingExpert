# class A:
#     def __init__(self):
#         print("A")


# class B:
#     def __init__(self):
#         print("B")


# class C(A, B):
#     def __init__(self):
#         super().__init__()


# c = C()
# print(isinstance(c, A))


# Run and then crash
class Duck:
    def swim(self):
        print("Swiming duck")

    def fly(self):
        print("Flying duck")


class Whale:
    def swim(self):
        print("Swiming whale")


animal = [Duck(), Duck(), Whale()]

for animal in animal:
    animal.swim()
    animal.fly()
