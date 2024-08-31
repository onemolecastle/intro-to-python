'''
1. Creating and Printing a Dictionary
   - Create a dictionary named `book` with keys `title`, `author`, and `year` with values of your choice. Print the dictionary.
'''
book = {"title": "1984", "author": "George Orwell", "year": 1949}
print(book)


'''
2. Adding a New Key-Value Pair
   - Add a new key `genre` with the value "Dystopian fiction" to the `book` dictionary. Print the updated dictionary.
'''
book["genre"] = "Dystopian fiction"
print(book)


'''
3. Modifying a Value
   - Update the `year` of the `book` dictionary to 1950. Print the updated dictionary.
'''
book["year"] = 1950
print(book)


'''
4. Removing a Key-Value Pair
   - Remove the key `author` from the `book` dictionary. Print the updated dictionary.
'''
del book["author"]
print(book)


'''
5. Using get() to Access a Value
   - Use the get() method to print the value of `title` from the `book` dictionary. If `title` doesn't exist, print "Title not found".
'''
print(book.get("title", "Title not found"))


'''
6. Using get() with a Non-existent Key
   - Attempt to access a non-existent key `publisher` using the get() method, providing a default value "Publisher not found". Print the result.
'''
print(book.get("publisher", "Publisher not found"))


'''
7. Copying a Dictionary
   - Create a copy of the `book` dictionary named `book_copy` using the `.copy()` method. Print `book_copy`.
'''
book_copy = book.copy()
print(book_copy)


'''
8. Merging Two Dictionaries
   - Create another dictionary `ratings` with keys `Goodreads` and `Amazon`, each with a numerical rating. Merge `ratings` into `book` using the `update` method and print the updated `book`.
'''
ratings = {"Goodreads": 4.8, "Amazon": 4.7}
book.update(ratings)
print(book)


'''
9. Clearing a Dictionary
   - Clear all contents from the `book` dictionary using the `.clear()` method and print the now empty dictionary.
'''
book.clear()
print(book)


'''
10. Creating a Dictionary from Lists
    - Given two lists `keys = ['a', 'b', 'c']` and `values = [1, 2, 3]`, create a dictionary using the `zip` function. Print the dictionary.
'''
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict)
