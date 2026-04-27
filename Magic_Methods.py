#Concept
# Magic (Dunder) Methods are special methods with double underscores like:
#Practice
class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
        # Magic (Dunder) Methods
    def __str__(self):
        return f"Book: {self.title}"
    # Magic (Dunder) Methods
    def __len__(self):
         return self.pages
book=Book("OOP",30)   
print(book)
print(len(book)) 
   
#Example
class Cart:
    def __init__(self, items):
        self.items = items

    def __add__(self, other):
        return Cart(self.items + other.items)

    def __str__(self):
        return f"Cart Items: {self.items}"

c1 = Cart(["Apple", "Banana"])
c2 = Cart(["Milk"])

c3 = c1 + c2

print(c3)