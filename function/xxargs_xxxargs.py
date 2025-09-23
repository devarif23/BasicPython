# def number(*arges):
#     print(arges)  # tuple 
#     return sum(arges)
# man1 = number(10,20)
# man2 = number(80,20)


def num(*arif):
    print(arif)
    return sum(arif)

x = num(23,98)
# =====================================

# def add(*numbers):
#     sum = 0
#     for num in numbers:
#         sum = sum + num
#     print(sum)
# add(10,20,30)

# =====================================

# Problem 1: Sum of Numbers (*args)
# একটা function লেখো sum_all(*args) নামে, যেটা যতগুলো সংখ্যা দেওয়া হবে সবগুলোর যোগফল বের করবে।

# def sum_all(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print(sum)

# sum_all(2, 3, 4) 
# sum_all(10, 20, 30, 40) 

# 🔹 Problem 2: Find Maximum (*args)
# একটা function লেখো find_max(*args) নামে, যেটা argument হিসেবে যতগুলো সংখ্যা দেওয়া হবে তার মধ্যে সর্বোচ্চ সংখ্যা return করবে।


# def find_max(*agrs):
#     a = agrs[0]
#     for i in agrs:
#         if i > a :
#             a = num
#     print('big number:' , a)
# find_max(10,9)


# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil" , 'gmail')


# def my_function(*kids):
#   print("The youngest child is " , kids[1])

# my_function("Emil", "Tobias", "Linus")

# def my_function(child1 , child2 , child3):
#     print('output' + " " + child2)
# my_function(child1="email" , child2="Name", child3="age")

# def my_function(**kid):
#   print("His last name is " + kid["lname"])
# my_function(fname = "Tobias", lname = "Refsnes")