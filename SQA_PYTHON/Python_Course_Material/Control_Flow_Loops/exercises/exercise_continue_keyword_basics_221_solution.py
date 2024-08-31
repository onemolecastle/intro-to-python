# Challenge 1: Skip Even Numbers
# Write a loop to print odd numbers from 1 to 10, skipping even numbers.
for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)
# Explanation:
# The `continue` statement skips the rest of the loop's body for even numbers (`number % 2 == 0`).
# Only odd numbers are printed because `continue` prevents executing the `print` statement for even numbers.

# Challenge 2: Skip Negative Numbers
# Given a list of numbers, print each number unless it's negative.
numbers = [3, -1, 5, -2, 7, -4]
for number in numbers:
    if number < 0:
        continue
    print(number)
# Explanation:
# Here, `continue` skips printing for any negative number. The loop only prints positive numbers and zero.

# Challenge 3: Ignore 'pass' in Passwords
# Print all items from a list of passwords, skipping any that are exactly "pass".
passwords = ["123", "admin", "pass", "password"]
for pwd in passwords:
    if pwd == "pass":
        continue
    print(pwd)
# Explanation:
# If a password is "pass", `continue` halts further execution of the loop body, skipping the `print` function for it.

# Challenge 4: Exclude Specific Letter
# Loop through a string and print each letter except 'a'.
for letter in "banana":
    if letter == 'a':
        continue
    print(letter)
# Explanation:
# The loop prints each letter except for 'a'. The `continue` statement bypasses the `print` call whenever 'a' is encountered.

# Challenge 5: Skip Placeholder Names
# Iterate over a list of names and print each one, skipping any that are "TBD".
names = ["Alice", "Bob", "TBD", "Charlie"]
for name in names:
    if name == "TBD":
        continue
    print(name)
# Explanation:
# "TBD" names are skipped due to the `continue` statement. It avoids executing the `print` function for placeholder names.

# Challenge 6: Non-Zero Items
# Print only non-zero items from a given list of integers.
items = [0, 1, 2, 0, 3, 0]
for item in items:
    if item == 0:
        continue
    print(item)
# Explanation:
# Zeroes are skipped in the loop, and `continue` ensures only non-zero items are printed.

# Challenge 7: Skip Printing Specific Index
# Loop through a list and print the item unless it's at index 2.
words = ["sun", "moon", "stars", "sky"]
for i in range(len(words)):
    if i == 2:
        continue
    print(words[i])
# Explanation:
# This loop checks the index and uses `continue` to skip printing the item at index 2, effectively excluding "stars".

# Challenge 8: Avoid Printing Duplicate Letters
# Print each letter from a string, skipping it if it has already been printed.
seen = set()
for letter in "hello":
    if letter in seen:
        continue
    seen.add(letter)
    print(letter)
# Explanation:
# The loop tracks seen letters in a set. If a letter is repeated, `continue` skips its second printing, avoiding duplicates.

# Challenge 9: Print Even Indices
# Print elements at even indices in a list, skipping odd indices.
elements = ["a", "b", "c", "d", "e"]
for i in range(len(elements)):
    if i % 2 != 0:
        continue
    print(elements[i])
# Explanation:
# The loop iterates through the list indices. Using `continue`, it skips elements at odd indices, printing only those at even indices.

# Challenge 10: Ignore Case 'x'
# Given a string, print each character except for 'x', ignoring case.
for char in "Example Text":
    if char.lower() == 'x':
        continue
    print(char)
# Explanation:
# By converting each character to lowercase for comparison, this loop skips 'x' and 'X'.
# `continue` prevents further execution within the loop for these cases, printing all other characters.
