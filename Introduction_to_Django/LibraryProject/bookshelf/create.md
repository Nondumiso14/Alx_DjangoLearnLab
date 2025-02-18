# Creating a Book instance
from bookshelf.models import Book
book = Book.objects.create
book = Book(title=“1984”, author=“George Orwell”, publication_year="1949")
book.save()
print(book)
Expected Output: Book: 1984

Book.objects.create"