# retrieving all books
books = Book.objects.all()
print(books)

# retrieving a specific book

books = Book.objects.get(title="1984")
print(books)