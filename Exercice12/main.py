class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        """
        Allow to have a clear readability of the list

        Returns:
            object: the book in the list
        """
        return (
            f"Book(title='{self.title}', "
            f"author='{self.author}', year='{self.year}')"
        )


class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        """
        Add a new book to the library

        Args:
            book (object): a book
        """
        self.book = book
        self.books.append(book)

    def search_title(self, book_title, list):
        self.book_title = book_title
        self.list = list
        for book in self.list:
            if book.title == book_title:
                return book

        print((f"Book with title '{book_title}' not found in library."))
        return None

    def remove_book(self, book_title, list):
        self.book_title = book_title
        self.list = list
        result = self.search_title(book_title, list)
        if result is not None:
            list.remove(result)
            print((f"Book '{book_title}' removed."))
            return result

    def borrow_book(self, book_title, list):
        self.book_title = book_title
        book = self.remove_book(book_title, list)
        self.borrowed_books.append(book)

    def return_book(self, book_title, list):
        self.book_title = book_title
        book = self.remove_book(book_title, list)
        self.books.append(book)

    def available_books(self):
        print("Available books : ", self.books)

    def borrowed_books_list(self):
        print("Borrowed books : ", self.borrowed_books)


new_book_1 = Book("Carrie", "Stephen King", "2010")
new_book_2 = Book("Cujo", "Stephen King", "1981")
new_book_3 = Book("Pet Sematary", "Stephen King", "1983")

# Use cases
my_library = Library()
my_library.add_book(new_book_1)
my_library.add_book(new_book_2)
my_library.add_book(new_book_3)
my_library.remove_book("Toto", my_library.books)
my_library.borrow_book("Carrie", my_library.books)
my_library.borrow_book("Cujo", my_library.books)
my_library.available_books()
my_library.borrowed_books_list()
my_library.return_book("Carrie", my_library.borrowed_books)
my_library.available_books()
my_library.borrowed_books_list()
