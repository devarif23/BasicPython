class phone:
    def __init__(self):
        print("I am in Phone class")

class samsung(phone):
    # init
    def __init__(self):
        #  overriding mathod
        super().__init__()      
        print("I am  in  samsung class")

s = samsung()
