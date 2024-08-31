# IMPORTANT: Some of the challenges expect you to use the input() function. 
# Look up how to use the input() function.

# ******************************************************

# Challenge 1: Print Numbers 1 to 5
# Use a while-loop to print numbers from 1 to 5.
number = 1
while number <= 5:
    print(number)
    number += 1

# Challenge 2: Sum of First N Numbers
# Write a while-loop to calculate the sum of the first 5 numbers (1 to 5) and print the sum.
number = 1
sum = 0
while number <= 5:
    sum += number
    number += 1
print(sum)

# Challenge 3: Repeat a String
# Repeat the string "Hello" 3 times using a while-loop and print the result.
repeat_count = 0
result = ""
while repeat_count < 3:
    result += "Hello "
    repeat_count += 1
print(result.strip())

# Challenge 4: Countdown from 10 to 1
# Write a while-loop to count down from 10 to 1 and print each number.
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1

# Challenge 5: Find the Power of 2
# Using a while-loop, find and print the first power of 2 greater than 100.
power = 1
while 2 ** power <= 100:
    power += 1
print(2 ** power)

# Challenge 6: Accumulate Even Numbers
# Accumulate the sum of even numbers between 1 and 10 (inclusive) using a while-loop and print the sum.
number = 1
sum_even = 0
while number <= 10:
    if number % 2 == 0:
        sum_even += number
    number += 1
print(sum_even)

# Challenge 7: Loop Until User Stops
# Ask the user to input any word and continue asking until they type "stop". Print "User stopped the loop." after.
word = ""
while word.lower() != "stop":
    word = input("Enter any word (or type 'stop' to end): ")
print("User stopped the loop.")

# Challenge 8: Validate Input
# Write a while-loop to keep asking for a number between 1 and 10 until the user enters a valid number. Print "Thank you!" after.
number = int(input("Enter a number between 1 and 10: "))
while number < 1 or number > 10:
    number = int(input("Invalid. Please enter a number between 1 and 10: "))
print("Thank you!")

# Challenge 9: Reverse a String
# Reverse the string "Hello" using a while-loop and print the reversed string.
original = "Hello"
reversed_str = ""
index = len(original) - 1
while index >= 0:
    reversed_str += original[index]
    index -= 1
print(reversed_str)

# Challenge 10: Guess the Number
# Implement a simple guess-the-number game where the answer is 7. Keep asking the user to guess the number until they get it right.
guess = int(input("Guess the number (1-10): "))
while guess != 7:
    guess = int(input("Wrong! Try again: "))
print("Correct! The number was 7.")
