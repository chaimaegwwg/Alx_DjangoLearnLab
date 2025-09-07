from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1. All books by a specific author
    author = Author.objects.get(name="J.K. Rowling")
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

    # 2. All books in a library
    library = Library.objects.get(name="Central Library")
    books_in_library = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

    # 3. Retrieve the librarian for a library
    librarian = library.librarian
    print(f"Librarian of {library.name}: {librarian.name}")

