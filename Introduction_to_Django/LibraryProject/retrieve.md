# Retrieving Created Book
from bookshelf.models import Book
book = Book.objects.get(title='1984')
print(book.title)

# Display all the Book instance attributes
# Display all attributes of the Book instance
print("title:", book.title)
print("author:", book.author)
print("publication_year:", book.publication_year)

expected output: 1984 George Orwell 1949
