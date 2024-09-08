from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from rest_framework import filters.OrderingFilter
from rest_framework import filters.SearchFilter
# from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import BookSerializer


# class BookListView(ListView):
#     model = Book
#     template_name = 'book_list.html'

# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'book_detail.html'

# class BookCreateView(CreateView):
#     model = Book
#     fields = ['title', 'author', 'publication_date']
#     template_name = 'book_form.html'
    
#     # Custom method to handle form submission

#     def form_valid(self, form):
#         if self.request.user.is_authenticated:
#             form.instance.author = self.request.user
#         return super().form_valid(form)

# class BookUpdateView(UpdateView):
#     model = Book
#     fields = ['title', 'author', 'publication_date']
#     template_name = 'book_form.html'
    
#     # Additional logic for filtering or customizing update behavior can go here
#     def form_valid(self, form):
#         form.instance.updated_by = self.request.user
#         return super().form_valid(form)

# class BookDeleteView(DeleteView):
#     model = Book
#     success_url = '/books/' # redirect after deletion
#     template_name = 'book_confirm_delete.html'

class BookListView(generics.ListAPIView):
    """
    Retrieve a list of all books.
    Allows unauthenticated users to read the list.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Anyone can view the list, only authenticated users can create
    
    # Adding filtering, search, and ordering functionality
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']  # Fields allowed for ordering

class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve details of a single book by ID.
    Allows unauthenticated users to read the details.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Anyone can view details

class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    Only authenticated users can add new books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create

    def perform_create(self, serializer):
        # Optionally assign the logged-in user as the creator
        serializer.save(created_by=self.request.user)

class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    Only authenticated users can update a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update

    def perform_update(self, serializer):
        # Optionally update the book with the logged-in user as the one making changes
        serializer.save(updated_by=self.request.user)
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete an existing book.
    Only authenticated users can delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete

