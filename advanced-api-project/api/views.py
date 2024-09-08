from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Book



class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'publication_date']
    template_name = 'book_form.html'
    
    # Custom method to handle form submission

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        return super().form_valid(form)

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publication_date']
    template_name = 'book_form.html'
    
    # Additional logic for filtering or customizing update behavior can go here
    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

class BookDeleteView(DeleteView):
    model = Book
    success_url = '/books/' # redirect after deletion
    template_name = 'book_confirm_delete.html'
