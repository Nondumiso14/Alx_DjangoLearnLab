from bookshelf.models import Book
# Update the title of “1984” to “Nineteen Eighty-Four”
book = Book.objects.get(title="1984")
book.title = 'Nineteen Eighty-Four'
book.save()
print(book)

Expected Output: Book: Nineteen Eighty-Four