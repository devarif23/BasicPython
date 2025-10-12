class student:
    roll = ''
    name = ''
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def display(self):
        print(f'Name : {self.name} Roll : {self.roll}')
    
stu1 = student("arif", 101)
stu1.display()

stu2 = student("glif", 102)
stu2.display()

stu3 = student("jalif", 103)
stu3.display()