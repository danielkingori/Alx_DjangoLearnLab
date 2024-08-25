
Book Views:

"book_list": Displays all books if the user has the "can_view_books" permission.
"book_create": Allows users with "can_create_books" permission to add new books.
"book_edit": Allows users with "can_edit_books" permission to modify existing books.
"book_delete": Allows users with "can_delete_books" permission to remove books.

BookList Views:

"booklist_list": Lists all book lists created by the current user if they have "can_view_booklists" permission.
"booklist_create": Allows users with "can_create_booklists" permission to create a new book list.
"booklist_edit": Allows users with "can_edit_booklists" permission to edit a book list they created.
"booklist_delete": Allows users with "can_delete_booklists" permission to delete a book list they created.

Permission Decorators: The "@permission_required" decorator is applied to each view, specifying the required permission (e.g., 'bookshelf.can_create_books'). The raise_exception=True argument ensures that unauthorized users see a 403 Forbidden error.

In the Django admin, you can create groups like "Admins", "Editors", and "Viewers", then assign the appropriate permissions:

Admins: Assign all permissions (for both "Book" and "BookList" models).
Editors: Assign permissions like "can_create_books", "can_edit_books", "can_create_booklists", and "can_edit_booklists".
Viewers: Assign only view permissions ("can_view_books", "can_view_booklists")