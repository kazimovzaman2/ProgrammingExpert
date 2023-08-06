# def foo(x):
#     print(x)
# def call_func(func, x):
#     func(x)
# call_func(foo, 5)



# def outer(x):
#     def inner(y):
#         def inner2(z):
#             print(x + y + z)
        
#         return inner2

#     return inner

# outer(5)(5)(5)



# class Collection:
#     def __init__(self):
#         self.lst = []
    
#     def add_value(self, value):
#         self.lst.append(value)
#         return self.lst

# def collection():

#     lst = []

#     def inner(value):
#         lst.append(value)
#         return lst
    
#     return inner

# add_value = collection()
# print(add_value(1))
# print(add_value(2))
# print(add_value(3))
# print(add_value(4))




# def counter(start):
#     count = start

#     def increment(value):
#         nonlocal count
#         count += value
#         return count
    
#     return increment

# count = counter(2)
# print(count(1))
# print(count(1))
# print(count(1))



def outer():
    def inner():
        def inner2():
            nonlocal x
            x = 2
            print("INNER2:", x)
        
        x = 3
        inner2()
        print("INNER:", x)
    
    x = 4
    inner()
    print("OUTER:", x)

outer()