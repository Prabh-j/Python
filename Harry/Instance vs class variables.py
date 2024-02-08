#class variable are those that are inside a class but are not associated to object, they are same for every object unless modified
#instance variable are those that are created for objects

class library:
    entries = 0 # a class variable
    books = []

    def __init__(self, book_name, author):
         self.book_name = book_name #a instance variable
         self.author = author
         library.books.append(book_name)
         library.entries += 1

    def check():
         if library.entries == len(library.books):
              print('Everything is OK')
         else:
              print('Error,number of books is not adding up!')

a = input('Name of the book: ')
b = input('Name of the author: ')

#class variable by itself cannot be changed, instead when we try to modify it, a new instance variable is creadted just for that perticular object, and next object will access old class vaiable 

b1 = library('A song of ice and fire', 'Gerorge RR Martin')
b2 = library('Wheel of time', 'Robert Jordon')
b3 = library('Stormlight Archive', 'Brandon Sanderson')
b4 = library('Empire of Vampire', 'Jay Kristof')
b5 = library(a , b)

print(library.books)
print(library.entries)


