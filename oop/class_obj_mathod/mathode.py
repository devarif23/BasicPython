# class student:
#     roll = ''
#     name = ''

#     def display(self):
#         print(f'Roll: {self.roll} GPA : {self.gpa}')

# rahim = student()
# rahim.roll = 101
# rahim.gpa = 3.90
# rahim.display()

# karim = student()
# karim.roll = 102
# karim.gpa = 4.00
# karim.display()


# ============= eta ke amra aro onno vabe krte pari 

class student:
    roll = ''
    gpa = ''

    def set_valu(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll number: {self.roll},  GPA number: {self.gpa}")

   
    
rahim = student()
rahim.set_valu(101,3.90)
rahim.display()

karim = student()
karim.set_valu(102,4.00)
karim.display()
