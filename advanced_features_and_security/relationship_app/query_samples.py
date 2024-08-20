from relationship_app.models import Author, Book, Librarian, Library

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.objects.filter(author=author)
        books = author.books.all()
        if books.exists():
            print(f"books by {author_name}:")
            for book in books:
                print(f"- {book.title}")
            
        else:
            print(f"no books found for {author_name}")
    except Author.DoesNotExist:
        print(f"Author: {author_name} does not exist in the DB")
        
def list_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        if books.exists():
            print(f"books in the {library_name} library:")
            for book in books:
                print(f"- {book.title}")
            else:
                print(f"no books found in the {library_name} library")
            
    except Library.DoesNotExist:
        print(f"The {library_name} library does not exist in the DB")
        

def get_librarian_for_library(library_name):
    try:
        library = Librarian.objects.get(library=library_name)
        librarian = library.librarian
        
        print(f"the librarian for the {library_name} library is {librarian.name}")
        
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist in the database.")
    except Librarian.DoesNotExist:
        print(f"the is not librarian for the {library_name} library")

if __name__ == "__main__":
    get_books_by_author('Specific Author')
    list_all_books_in_library('Main Library')
    get_librarian_for_library('Main Library')
    
