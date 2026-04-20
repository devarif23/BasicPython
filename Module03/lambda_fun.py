# anonymous function --> Unnamed

# def square(x):
#     return x*x
# print(square(5))

# lamda fubction --->  lamda argments : expression

square = lambda x: x * x
# print(square(4))


add = lambda a, b: a + b
# print(add(10,15))


# number dia sorted kora --  x:x[1]
student = [("Rahim", 120), ("arif", 10), ("Rita", 90), ("Anjum", 20)]
sorted_student = sorted(student, key=lambda x: x[1])
print(sorted_student)

# name dia sorted -- x:x[0]
student = [("Rahim", 120), ("arif", 10), ("Rita", 90), ("Anjum", 20)]
sorted_student = sorted(student, key=lambda x: x[0])
print(sorted_student)


# map() filter() reduce()

# map()
nums = [1, 2, 3, 4, 5]
# sq_nums = list(map(square korte chacchi , kar upor apply korte chacchi))
sq_nums = list(map(lambda x: x * x, nums))
print(sq_nums)


# filter()
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)


#reduce()

import functools


