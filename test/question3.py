#Create a Book class with instance Library_name, book_name, author, pages?
class Book :
    category = "Thriller"
    def __init__(self,lib_name,book_name,author):
          self.lib_name = lib_name
          self.book_name = book_name
          self.author = author
          print(self.lib_name,self.author,self.lib_name,Book.category)
o1 = Book("District Library","Sky is falling","Sidney sheldon")