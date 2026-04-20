#  use define function 

#1 No input , no return 

def my_frist_function():   # function definition 
    a = 10
    b = 20
    print(a+b)
my_frist_function()   # function call kora 


# 2. input , no return -----------------------------------------------------------------------------------------

def add_two_number(a , b):   # (a,b) parameters
    print(a+b)

add_two_number(15,20)   # (15,20) arguments
add_two_number(10,20)


# 3. input , return ----------------------------------------------------------------------------------------------

def multiply_two_number(a , b):
    return a*b
result = multiply_two_number(12,2)
print(result)


# 4. no input , return ----------------------------------------------------------------------------------------------

def hello():
    return "Hello World"
greeting = hello()
print(greeting)