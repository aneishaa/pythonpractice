class Book :
    def __init__(self,pages):
          self.pages = pages
    def __add__(self, other):
        return Book(self.pages+other.pages)
    def __str__(self):
        return str(self.pages)

o1 = Book(100)
o2 = Book(200)
o3 = Book(300)

print(o1+o2+o3)
