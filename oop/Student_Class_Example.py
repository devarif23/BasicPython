class student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def show_info(self):
        # print(f"Name : {self.name}, roll : {self.roll} , marks:{self.marks}")
        if self.marks >= 33:
            print(f'{self.name} tumi pass')
        else:
            print(f'{self.name} tumi file')
student1 = student( 'jahan', 12 , 36)
student.show_info(student1)