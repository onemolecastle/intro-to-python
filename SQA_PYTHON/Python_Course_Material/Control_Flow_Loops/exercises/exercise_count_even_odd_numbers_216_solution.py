"""
Counting the Number of Even and Odd Numbers in a List

Write a program that uses a for loop to count the number of even and odd numbers in a list.

The program should define a list of numbers and initialize two variables called even_count and odd_count to zero.

Then, the program should use a for loop to iterate over the list of numbers, checking if each number is even or odd.
If a number is even, the program should increment the even_count variable. If a number is odd, the program
should increment the odd_count variable.

Finally, the program should print the number of even and odd numbers.


"""

numbers = [5, 12, 3, 7, 9, 20, 1]
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("The list contains", even_count, "even numbers and", odd_count, "odd numbers.")
