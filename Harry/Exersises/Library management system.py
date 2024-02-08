# make a class library with at least two variables, number of books and books name, every time you add a book, number of books should increase, make a method to check if number of books match with books added, answer if memory persits sfter you end the program.

class library:
    entries = 0
    books = []

    def __init__(self, book_name, author):
         self.book_name = book_name
         self.author = author
         library.books.append(book_name)
         library.entries += 1

    def check():
         if library.entries == len(library.books):
              print('Everything is OK')
         else:
              print('Error,number of books is not adding up!')

while True:
     q = input('Do you want to add another book(y/n): ').lower()
     if q == 'y':
          a = input('Name of the book: ')
          b = input('Name of the author: ')
          print('Done, Thank you.')
          bx = library(a , b) #how to change name of variable each time
     elif q == 'n':
          print('As you Wish')
          break
     else:
          print('Please enter a vadlid response.')

b1 = library('A song of ice and fire', 'Gerorge RR Martin')
b2 = library('Wheel of time', 'Robert Jordon')
b3 = library('Stormlight Archive', 'Brandon Sanderson')
b4 = library('Empire of Vampire', 'Jay Kristof')
t = "\n".join(library.books)
print(f'The books are:\n{t}')
print(f'Library has {library.entries} books.')