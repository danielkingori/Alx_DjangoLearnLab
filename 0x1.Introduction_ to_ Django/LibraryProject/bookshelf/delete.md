# Delete a book instance

from bookshelf.models import Book

# retrieve the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# delete the book instance
book.delete()