book = Book.objects.get(title="1984")
book.delete()

# Confirm the deletion 
books = Book.objects.all()
# Expected output: An empty QuerySet
print(books)

Expected Output:
QuerySet[]


