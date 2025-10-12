
class car:
    def __init__(self, brand , model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    # methode 

    def drive(self):
        print(f"{self.brand} {self.model} is driveing")
    def stop(self):
        print(f"{self.brand} {self.model} has stop")
    
    # object 

    car1 = chr('toyota' , " corola" , "red")
    car2 = chr('honda', 'civic', 'blue')

    # object er mathode call 
    car1.drive()


    # Object এর property access করা
    print(car1.color)   