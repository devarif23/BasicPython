# parent class / super class
class phone:
    def call (self):
        print("you can call")
    def massage (self):
        print('you can massage')
# chaild class  / sub class
class vivo(phone):    
    def photo(self):
        print('you can photo')
v = vivo()
v.photo()
v.call()
v.massage()
