# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Wrapper functiion called func!")
#         result = func(*args, **kwargs)
#         return result
    
#     return wrapper

# @decorator   # foo = decorator(foo) -> same thing
# def foo(x, y, z=None):
#     print(x, y, z)
#     return x + y + z

# print(foo(2,3,z=4))













import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        total_time = end_time - start_time
        print("Time taken to execute:", total_time)
        return result
    
    return wrapper

def pretty_printer(func):
    def wrapper(*args, **kwargs):
        print("----")
        result = func(*args, **kwargs)
        print("----")
        return result
    return wrapper


@timer
@pretty_printer
def print_numbers(num):
    for i in range(num):
        pass

# print_numbers = timer(pretty_printer(print_numbers))
print_numbers(1000000)



# @timer
# def loop():
#     for _ in range(100000):
#         pass

# @timer
# def get_max(x,y,z):
#     return max(x,y,z)

# print(get_max(1,2,3))