# Challenge 1: Print All Fruits
# Write a for-loop to print each fruit in the list.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Challenge 2: Calculate and Print the Sum
# Given a list of numbers, write a for-loop to calculate the sum of the numbers and print the sum.
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print(sum)

# Challenge 3: Count and Print Even Numbers
# Given a list of integers, write a for-loop to count how many even numbers are in the list and print the count.
numbers = [1, 2, 3, 4, 5, 6]
even_count = 0
for number in numbers:
    if number % 2 == 0:
        even_count += 1
print(even_count)

# Challenge 4: Find and Print the Maximum Number
# Assuming a list of numbers, write a for-loop to find the maximum number and print it.
numbers = [4, 6, 8, 24, 12, 2]
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)

# Challenge 5: Loop Through a String
# Given a string, write a for-loop to print each character in the string.
for character in "Hello":
    print(character)

# Challenge 6: Create and Print a New List of Squares
# Given a list of numbers, write a for-loop to create a new list containing the square of each number and print the new list.
original = [1, 2, 3, 4, 5]
squares = []
for number in original:
    squares.append(number ** 2)
print(squares)

# Challenge 7: Print Numbers Greater Than 10
# Given a list of numbers, use a for-loop to print only those numbers greater than 10.
numbers = [8, 12, 3, 25, 4, 11]
for number in numbers:
    if number > 10:
        print(number)

# Challenge 8: Print Dictionary Keys
# Given a dictionary, use a for-loop to print its keys.
student_grades = {"John": 88, "Sara": 92, "Leo": 68}
for student in student_grades:
    print(student)

# Challenge 9: Calculate and Print the Sum of Dictionary Values
# Given a dictionary with integer values, write a for-loop to find the sum of the values and print it.
items = {"apple": 2, "banana": 3, "orange": 5}
total = 0
for item in items.values():
    total += item
print(total)

# Challenge 10: Double and Print List Elements
# Given a list of numbers, multiply each element by 2 and print the modified list.
numbers = [2, 4, 6, 8]
for i in range(len(numbers)):
    numbers[i] *= 2
print(numbers)
