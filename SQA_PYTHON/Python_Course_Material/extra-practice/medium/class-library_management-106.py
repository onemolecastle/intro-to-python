"""
Library Management Challenge (id=106)

Challenge Description:

You are tasked with implementing a simple library management system in Python. You should create a class called `Library` that can be used to manage books in a library.

Requirements:

1. Implement the `Library` class with the following methods:
   - `add_book(self, book: Book) -> None`: This method should add a book to the library. The `book` parameter is an instance of the `Book` class (already provided).
   - `remove_book(self, isbn: str) -> None`: This method should remove a book from the library based on its ISBN (International Standard Book Number).
   - `list_books(self) -> List[str]`: This method should return a list of book titles currently available in the library.
   - `borrow_book(self, isbn: str) -> str`: This method should allow a user to borrow a book based on its ISBN. If the book is available, it should be marked as borrowed and return "Borrowed successfully." If the book is already borrowed, return "Book is already borrowed."
   - `return_book(self, isbn: str) -> str`: This method should allow a user to return a borrowed book based on its ISBN. If the book is returned successfully, it should be marked as available and return "Returned successfully." If the book is already available, return "Book is already available."

2. The `Book` class is already provided with attributes:
   - `title` (str): The title of the book.
   - `author` (str): The author of the book.
   - `isbn` (str): The ISBN of the book.

3. The library should keep track of whether a book is available or borrowed.

4. The library should support the borrowing and returning of books.

5. The library should return a list of book titles.

Instructions:

1. Implement the `Library` class with the specified methods according to the requirements.

2. Use the `Book` class provided to create book objects.

3. Ensure that the library correctly tracks the availability of books and allows users to borrow and return them.

4. Write unit tests for the `Library` class to verify its functionality.

5. Make sure that the unit tests cover various scenarios, including borrowing and returning books, adding and removing books, and listing available books.

Examples:

Here are some examples of how the `Library` class should behave:

```python
library = Library()

book1 = Book("Book1", "Author1", "1234567890")
book2 = Book("Book2", "Author2", "9876543210")

# Add books to the library
library.add_book(book1)
library.add_book(book2)

# List available books
available_books = library.list_books()
# Result: ["Book1", "Book2"]

# Borrow a book
result1 = library.borrow_book("1234567890")
# Result: "Borrowed successfully."

# Try to borrow the same book again
result2 = library.borrow_book("1234567890")
# Result: "Book is already borrowed."

# Return a book
result3 = library.return_book("1234567890")
# Result: "Returned successfully."

# Try to return the same book again
result4 = library.return_book("1234567890")
# Result: "Book is already available."

# List available books after returning
available_books_after_return = library.list_books()
# Result: ["Book1", "Book2"]
"""

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False



class Library:
    # < your code here >
    pass



#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####
import unittest

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book1 = Book("Book1", "Author1", "1234567890")
        self.book2 = Book("Book2", "Author2", "9876543210")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        self.library.add_book(Book("Book3", "Author3", "5432109876"))
        self.assertIn("5432109876", self.library.books)

    def test_remove_book(self):
        self.library.remove_book("1234567890")
        self.assertNotIn("1234567890", self.library.books)

    def test_list_books(self):
        books = self.library.list_books()
        self.assertEqual(books, [self.book1, self.book2])

    def test_borrow_book(self):
        result1 = self.library.borrow_book("1234567890")
        result2 = self.library.borrow_book("1234567890")
        self.assertEqual(result1, "Borrowed successfully.")
        self.assertEqual(result2, "Book is already borrowed.")

    def test_return_book(self):
        result1 = self.library.return_book("1234567890")
        result2 = self.library.return_book("1234567890")
        self.assertEqual(result1, "Book is already available.")
        self.assertEqual(result2, "Book is already available.")



if __name__ == "__main__":
    run_app = False
    run_unit_tests = True
    
    if run_unit_tests:
        unittest.main()

    if run_app:
        library = Library()
        while True:
            print("\nWelcome to the Library Management System!\n")
            print("Options:")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. List all books")
            print("4. Borrow a book")
            print("5. Return a book")
            print("6. Quit\n")
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                book = Book(title, author, isbn)
                library.add_book(book)
                print("Book added successfully!")
            
            elif choice == "2":
                isbn = input("Enter ISBN of the book to remove: ")
                library.remove_book(isbn)
            
            elif choice == "3":
                books = library.list_books()
                if books:
                    print("List of books:")
                    for book in books:
                        print(book)
                else:
                    print("No books in the library.")
            
            elif choice == "4":
                isbn = input("Enter ISBN of the book to borrow: ")
                result = library.borrow_book(isbn)
                print(result)
            
            elif choice == "5":
                isbn = input("Enter ISBN of the book to return: ")
                result = library.return_book(isbn)
                print(result)
            
            elif choice == "6":
                print("Goodbye!")
                break
