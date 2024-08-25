from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, BookList
# Create your views here.
from django.http import HttpResponse

def index(request): return HttpResponse("Welcome to my book store")


@permission_required("bookshelf.can_view_books", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html',{'books':books})


@permission_required('bookshef.can_create_books', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        Book.objects.create(title=title, author=author, description=description)
        return redirect('book_list')
    return render(request, 'bookshef/book_form.html')

@permission_required('bookshef.can_edit_books', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.save()
        return redirect('book_list')
    return render(request, 'bookshef/book_form.html', {'book': book})

@permission_required('bookshef.can_delete_books', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshef/book_confirm_delete.html', {'book': book})


# BookList Views

@permission_required('bookshef.can_view_booklists', raise_exception=True)
def booklist_list(request):
    booklists = BookList.objects.filter(created_by=request.user)
    return render(request, 'bookshef/booklist_list.html', {'booklists': booklists})

@permission_required('bookshef.can_create_booklists', raise_exception=True)
def booklist_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        booklist = BookList.objects.create(name=name, created_by=request.user)
        books = request.POST.getlist('books')  # Assuming this comes from a multi-select field
        booklist.books.set(books)
        return redirect('booklist_list')
    books = Book.objects.all()
    return render(request, 'bookshef/booklist_form.html', {'books': books})

@permission_required('bookshef.can_edit_booklists', raise_exception=True)
def booklist_edit(request, booklist_id):
    booklist = get_object_or_404(BookList, id=booklist_id, created_by=request.user)
    if request.method == "POST":
        booklist.name = request.POST.get('name')
        books = request.POST.getlist('books')
        booklist.books.set(books)
        booklist.save()
        return redirect('booklist_list')
    books = Book.objects.all()
    return render(request, 'bookshef/booklist_form.html', {'booklist': booklist, 'books': books})

@permission_required('bookshef.can_delete_booklists', raise_exception=True)
def booklist_delete(request, booklist_id):
    booklist = get_object_or_404(BookList, id=booklist_id, created_by=request.user)
    if request.method == "POST":
        booklist.delete()
        return redirect('booklist_list')
    return render(request, 'bookshef/booklist_confirm_delete.html', {'booklist': booklist})
