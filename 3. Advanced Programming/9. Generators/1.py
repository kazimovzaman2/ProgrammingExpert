# def gen():
#     yield 1
#     yield 2
#     yield 3


# itr = gen()
# print(next(itr))
# print(next(itr))
# print(next(itr))




def fib(n):
    last = 1
    second_last = 1
    current = 3

    while current <= n:
        num = last + second_last
        yield num

        second_last = last
        last = num
        current += 1

for val in fib(10):
    print(val)


"""
fib_numbers = [1,1]

for i in range(2, 100):
    last = fib_numbers[i-1]
    second_last = fib_numbers[i-2]
    num = last + second_last
    fib_numbers.append(num)

print(fib_numbers)
"""