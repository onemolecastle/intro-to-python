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
for book in library['books']:
    print(book['title'])

# Exercise 2: Print the names of all authors in the library
for author in library['authors']:
    print(author['name'])

# Exercise 3: Find the total number of books in the library
total_books = sum(book['copies'] for book in library['books'])
print(f"Total number of books: {total_books}")

# Exercise 4: List the borrowers who have borrowed more than one book
for borrower in library['borrowers']:
    if len(borrower['borrowed_books']) > 1:
        print(f"{borrower['name']} has borrowed more than one book.")

# Exercise 5: Update the number of copies for "1984" by adding 2 more copies
for book in library['books']:
    if book['title'] == "1984":
        book['copies'] += 2

# Exercise 6: Remove a book with the title "To Kill a Mockingbird"
library['books'] = [book for book in library['books'] if book['title'] != "To Kill a Mockingbird"]

# Exercise 7: Print the names of all borrowers who have borrowed the book with id 3
book_id = 3
borrower_ids = [book['borrowers'] for book in library['books'] if book['id'] == book_id][0]
for borrower in library['borrowers']:
    if borrower['id'] in borrower_ids:
        print(borrower['name'])

# Exercise 8: Add a new author and assign a new book to that author
new_author = {'id': 4, 'name': "J.K. Rowling"}
library['authors'].append(new_author)
new_book = {'id': 4, 'title': "Harry Potter", 'author_id': 4, 'copies': 4, 'borrowers': []}
library['books'].append(new_book)

# Exercise 9: Print the average number of books borrowed by each borrower
total_borrowed_books = sum(len(borrower['borrowed_books']) for borrower in library['borrowers'])
average_books = total_borrowed_books / len(library['borrowers'])
print(f"Average number of books borrowed: {average_books}")

# Exercise 10: List all books borrowed by Alice
alice_books = [book['id'] for book in library['books'] if 1 in book['borrowers']]
print(f"Alice has borrowed books with IDs: {alice_books}")
