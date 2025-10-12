# class book:
#     def __init__(self,title,author,price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def show_info(self):
#         print(f'title: {self.title} \nAuthor: {self.author} \nPrice: {self.price}')
#     def discount(self,present):
#         self.price = self.price - (self.price * present/100)

# book1 = book('pytohn basice ' , 'arif', 500)
# book1.discount(10)
# book1.show_info()

class student:
    roll = " "
    gpa = " "

rahim=student()
rahim.roll = 101
rahim.gpa = 3.70
print(f"Roll: {rahim.roll}, GPA : {rahim.gpa}")

karim=student()
karim.roll = 101
karim.gpa = 3.70
print(f"Roll: {karim.roll}, GPA : {karim.gpa}")
