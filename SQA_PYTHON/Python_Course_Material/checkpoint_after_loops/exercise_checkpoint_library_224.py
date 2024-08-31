# Checkpoint exercise - after Loops - "Library" example.

# Library data structure
library = {
    'books': [
        {'id': 1, 'title': "1984", 'author_id': 1, 'copies': 5, 'borrowers': [2, 3]},
        {'id': 2, 'title': "To Kill a Mockingbird", 'author_id': 2, 'copies': 3, 'borrowers': []},
        {'id': 3, 'title': "The Great Gatsby", 'author_id': 3, 'copies': 2, 'borrowers': [1, 3]}
    ],
    'authors': [
        {'id': 1, 'name': "George Orwell"},
        {'id': 2, 'name': "Harper Lee"},
        {'id': 3, 'name': "F. Scott Fitzgerald"}
    ],
    'borrowers': [
        {'id': 1, 'name': "Alice", 'borrowed_books': [3]},
        {'id': 2, 'name': "Bob", 'borrowed_books': [1]},
        {'id': 3, 'name': "Charlie", 'borrowed_books': [1, 3]}
    ]
}

# Exercise 1: Print the title of all books in the library

# Exercise 2: Print the names of all authors in the library

# Exercise 3: Find the total number of books in the library

# Exercise 4: List the borrowers who have borrowed more than one book

# Exercise 5: Update the number of copies for "1984" by adding 2 more copies

# Exercise 6: Remove a book with the title "To Kill a Mockingbird"

# Exercise 7: Print the names of all borrowers who have borrowed the book with id 3

# Exercise 8: Add a new author and assign a new book to that author

# Exercise 9: Print the average number of books borrowed by each borrower

# Exercise 10: List all books borrowed by Alice
