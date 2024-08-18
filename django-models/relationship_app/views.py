from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context = {
        'books':books
    }
    
    return render(request, 'relationship_app/list_books.html', context)

def index(request):
    return render(request, "index.html")

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the list of books in the library to the context
        context['books'] = self.object.books.all()  # self.object refers to the current Library instance
        return context