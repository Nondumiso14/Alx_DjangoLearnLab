from django.shortcuts import render
from .models import Library

# Create your views here.
def book_list(request):
    books = Book.objects.all()  # Fetch all book instances from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['relationship_app'] = self.object.books.all()
        return context

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth import login
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/login.html'

import UserCreationForm from django.contrib.auth.forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile

from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'


@login_required
def admin_view(request):
    if request.user.userprofile.role == 'Admin':
        return render(request, 'admin_view.html')
    else:
        return redirect('home')

@login_required
def librarian_view(request):
    if request.user.userprofile.role == 'Librarian':
        return render(request, 'librarian_view.html')
    else:
        return redirect('home')

@login_required
def member_view(request):
    if request.user.userprofile.role == 'Member':
        return render(request, 'member_view.html')
    else:
        return redirect('home')


