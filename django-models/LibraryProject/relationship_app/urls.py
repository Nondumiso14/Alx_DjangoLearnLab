from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    # Function-based view
    path('books/', views.book_list, name='book_list'),

    # Class-based view
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

urlpatterns = [path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),]

#User Logout
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),]

urlpatterns = [
    # ... other URL patterns ...

    
    path('register/', views.register_view, name='register.html')
]

from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]