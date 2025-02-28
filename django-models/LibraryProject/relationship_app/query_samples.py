#Get all books by a specific author
author_name = 'John Smitg'
books = Book.objects.filter(author__name=author_name)

#List all books in a library
library_name = 'Main Library'
library = Library.objects.get(name=library_name)
books = library.books.all()

#Retrieve the librarian for a library
library_name = 'Main Library'
library = Library.objects.get(name=library_name)
librarian = library.librarian