from django.urls import path
from . import views

urlpatterns = [
    # Function-based view
    path('books/', views.book_list, name='book_list'),

    # Class-based view
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]