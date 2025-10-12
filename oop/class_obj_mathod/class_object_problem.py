class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")
         
stu1 = Person('arif', 34)
stu2 = Person('jahan', 30)

stu1.introduce()
stu2.introduce()