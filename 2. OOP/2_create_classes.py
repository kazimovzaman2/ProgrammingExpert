# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person("Tim", 21)
# p2 = Person("Bill", 40)

# print(p1.name, p1.age)
# print(p2.name, p2.age)


# p1.name = "random"
# print(p1.name)


class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories


a = Fruit("Apple", 100)
a.color = "Red"

print(a.name)
