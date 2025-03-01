from django.shortcuts import render

# Create your views here.
def book_list(request):
    books = Book.objects.all()  # Fetch all book instances from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['relationship_app'] = self.object.books.all()
        return context
