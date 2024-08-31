"""
Summing a List of Numbers

Write a program that uses a for loop to sum a list of numbers.

The program should define a list of numbers and initialize a variable called total to zero.

Then, the program should use a for loop to iterate over the list of numbers, adding each number to the total.

Finally, the program should print the total.
"""

numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print("The sum of the numbers is:", total)
