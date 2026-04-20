#  Keyword Arguments


"""


 def my_func(f_name, l_name, age):
    print(f"My name is {f_name} {l_name}. i am {age} years old.")

# my_func("Arif", "Ullah", 20)
# my_func(20, "Ullah","Arif")
my_func(age = 20, l_name="Ullah",f_name="Arif")

"""


def student(**kwargs):
    print(kwargs)
    print(
        f"My name is {kwargs['f_name']} {kwargs['l_name']} . I am {kwargs['age']} years old . I got {kwargs['marks']} in programing.I live in {kwargs['address']} "
    )


student(age=20, f_name="Arif", l_name="jahan", marks=33, address="Rangpur")
