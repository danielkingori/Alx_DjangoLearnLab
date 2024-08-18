# retrieve the book
book = Book.objects.get(title="1984)

# update the title 
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(updated_book)