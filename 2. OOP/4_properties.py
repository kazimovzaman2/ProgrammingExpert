# class Person:
#     def __init__(self, name):
#         self.name = name  # public
#         self._salary = 0  # private

#     @property
#     def salary(self):
#         return round(self._salary)

#     @salary.setter
#     def salary(self, salary):
#         if salary < 0:
#             raise ValueError('Salary must be positive')
#         self._salary = salary

#     # salary = property(get_salary, set_salary)


# p = Person('Bob')
# p.salary = 100.111
# print(p.salary)


class Time:
    def __init__(self, second):
        self._second = second

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, second):
        if second < 0 or second > 60:
            raise ValueError('Second must be positive')
        self._second = second


t = Time(10)
t.second = 59
