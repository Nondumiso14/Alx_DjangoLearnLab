Retrieving Created Book
from bookshelf.models import Book
book = Book.objects.get(title='1984')
print(book.title)

# Display all the Book instance attributes
# Display all attributes of the Book instance
books = Book.objects.all()
for book in books:
    print(book.title)

expected output: 1984 Gorge Orwell 1