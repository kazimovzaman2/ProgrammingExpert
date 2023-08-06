# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.age = None

#     def say_hello(self):
#         print(f"Hello, {self.name}")

#     def set_age(self, age):
#         self.age = age

#     def get_age(self):
#         return self.age


# p1 = Person("John")
# p1.set_age(20)
# print(p1.get_age())


class Counter:
    def __init__(self):
        self.count = 0
        self.locked = False

    def toogle_lock(self):
        self.locked = not self.locked

    def increment(self):
        if self.locked:
            raise Exception("Counter is locked")
        self.count += 1

    def decrement(self):
        if self.locked:
            raise Exception("Counter is locked")
        self.count -= 1

    def print_count(self):
        print(f"The currect count is {self.count}")


counter = Counter()
counter2 = Counter()


counter.toogle_lock()
counter2.increment()
counter.print_count()
counter2.print_count()
