# Challenge 1: Break on Negative Number
# Given a list of numbers, write a loop that prints each number until it encounters a negative number, at which point it should stop.
numbers = [3, 5, 7, 8, 0, 4, 7, -1, 4, 6]
for number in numbers:
    if number < 0:
        print("Negative number encountered:", number)
        break
    print(number)
# Explanation:
# This loop iterates through each number in the list. The `if` statement checks if the current number is negative.
# When a negative number is encountered, the loop prints a message including the negative number and exits the loop using `break`.
# If the number is not negative, it prints the number and continues to the next iteration.

# Challenge 2: User Input Break
# Write a program that continuously asks the user to enter a word until they type 'exit'. Then, the program should print "Loop exited" and stop.
while True:
    user_input = input("Enter a word (or type 'exit' to stop): ")
    if user_input == "exit":
        print("Loop exited")
        break
# Explanation:
# This challenge uses an infinite loop (`while True`) to continuously prompt the user for input.
# Inside the loop, it checks if the user's input is equal to "exit". If so, the program prints "Loop exited" and breaks out of the loop.
# The `break` statement here is crucial for stopping an otherwise infinite loop based on user input.

# Challenge 3: Find First Even Number
# Given a list of numbers, print the first even number encountered and stop the loop.
numbers = [1, 3, 5, 4, 9, 8]
for number in numbers:
    if number % 2 == 0:
        print("First even number:", number)
        break
# Explanation:
# The loop iterates over the list and checks each number to see if it's even (number % 2 == 0).
# Once it finds the first even number, it prints that number and exits the loop with `break`.

# Challenge 4: Skip to a Specific Letter
# Iterate over a string and stop when you reach the letter 'm'. Print all letters up until 'm'.
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter == 'm':
        print("Reached 'm', stopping loop.")
        break
    print(letter)
# Explanation:
# This `for` loop goes through each letter in the given string. When it encounters the letter 'm',
# it prints a stopping message and then exits the loop with `break`, having printed all previous letters.

# Challenge 5: Exit Loop on Duplicate Entry
# Given a list of names, stop the loop and print "Duplicate name found" when a duplicate name is encountered.
names = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Alice"]
seen = set()
for name in names:
    if name in seen:
        print("Duplicate name found:", name)
        break
    seen.add(name)
# Explanation:
# The loop tracks names it has seen in a set. For each name, it checks if the name is already in the set.
# If a duplicate is found, it prints the duplicate name and exits the loop with `break`. Otherwise, it adds the name to the set.

# Challenge 6: While Loop with User Confirmation
# Continuously ask the user to confirm if they want to continue. Exit the loop with a "Goodbye" message if they say 'no'.
while True:
    confirm = input("Continue? yes/no: ")
    if confirm == 'no':
        print("Goodbye")
        break
# Explanation:
# This creates an infinite loop that repeatedly asks for user confirmation.
# If the user inputs 'no', it prints a farewell message and breaks out of the loop, stopping the program.

# Challenge 7: Guessing Game with Limit
# Implement a guessing game where the user has 3 attempts to guess a number (let's say 5). Use a while loop and break if they guess correctly.
attempts = 3
while attempts > 0:
    guess = int(input("Guess the number (1-10): "))
    if guess == 5:
        print("Correct! You win!")
        break
    attempts -= 1
    print(f"Wrong. {attempts} attempts left.")
else:
    print("Out of attempts. Better luck next time!")
# Explanation:
# This loop allows the user three attempts to guess the correct number.
# If the user guesses correctly, it congratulates them and breaks out of the loop.
# Otherwise, it decrements the attempt count and provides feedback.

# Challenge 8: Breaking Out of Nested Loops
# Given a nested list of numbers, stop searching once you find the number 7. Print "Found 7" and exit both loops.
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
found = False
for sublist in numbers:
    for number in sublist:
        if number == 7:
            print("Found 7")
            found = True
            break
    if found:
        break
# Explanation:
# This challenge involves nested loops iterating through a list of lists. Upon encountering the number 7,
# it prints a message and sets a flag (`found`) to True, then breaks out of the inner loop.
# The outer loop checks the flag and breaks if True, effectively exiting both loops upon finding the number 7.
