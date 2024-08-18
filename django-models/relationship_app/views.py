from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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
    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Login")
        
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form":form})

class Login(login):
    template_name = "login.html"