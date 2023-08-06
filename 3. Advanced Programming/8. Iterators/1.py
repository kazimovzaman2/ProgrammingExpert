# x = [1,2,3]

# x_iter = iter(x) # x.__iter__()

# while True:
#     try:
#         print(next(x_iter))
#     except StopIteration:
#         break



class Numbers:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def __iter__(self):
        return NumberIterator(self.num1, self.num2, self.num3)

class NumberIterator:
    def __init__(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three
        self.current = 0

    def __next__(self):
        self.current += 1
        if self.current == 1:
            return self.one
        elif self.current == 2:
            return self.two
        elif self.current == 3:
            return self.three
        else:
            raise StopIteration

nums = Numbers(1,2,3)

for num in nums:
    print(num)
