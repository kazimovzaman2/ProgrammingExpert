# class Car:
#     number_of_cars = 0

#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#         Car.number_of_cars += 1

#     @classmethod
#     def update_number_of_cars(cls):
#         cls.number_of_cars = 5
#         print('runs')


# c1 = Car("Ford", "Edge")
# c2 = Car("Mazda", "3")

# Car.update_number_of_cars()

# print(c1.number_of_cars)
# print(c2.number_of_cars)
# print(Car.number_of_cars)


class Circle:
    pi = 3.14

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** 2)

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.pi * radius

    @classmethod
    def get_area_and_perimetre(cls, radius):
        return cls.area(radius), cls.perimeter(radius)


print(Circle.get_area_and_perimetre(4))
