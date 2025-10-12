class Animals: 
   
        a = 10
        b = 20
        def sound(self):
             print(self.a+ self.b)
class Dog(Animals):
    def bark(self):
        print('bog braks')


d = Dog()
d.bark()
d.sound()