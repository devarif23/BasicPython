class book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def show_info(self):
        print(f'title: {self.title} \nAuthor: {self.author} \nPrice: {self.price}')
    def discount(self,present):
        self.price = self.price - (self.price * present/100)

book1 = book('pytohn basice ' , 'arif', 500)
book1.discount(10)
book1.show_info()