"""
Exercise: Guess the Number (id=135)

* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if name == ‘main’:" block.

Requirements:
Write a Python program that generates a random number between 1 and 100 and asks the user to guess the number. The program should provide feedback to the user after each guess.

Instructions
Implement guess_the_number function according to the specified requirements. Use loops and conditional statements to generate a random number and ask the user to guess it. Provide feedback to the user after each guess. Return the number of guesses it took for the user to guess correctly.

Examples
Here is an example to illustrate the expected behavior of your function:

Input: guess_the_number() Output: "What is your guess? " 50 "You are wrong! You guessed the number in 1 guess. You guessed too high."

Input: guess_the_number() Output: "What is your guess? " 25 "You are wrong! You guessed the number in 2 guesses. You guessed too low."

Input: guess_the_number() Output: "What is your guess? " 37 "Congratulations! You guessed the number in 3 guesses."

Input: guess_the_number() Output: "What is your guess? " 101 "You are completely wrong! The number is between 1 and 100." 

Input: guess_the_number() Output: "What is your guess? " 0 "You are completely wrong! The number is between 1 and 100."

Input: guess_the_number() Output: "What is your guess? " "You are completely wrong! The number is between 1 and 100."


"""

import random

def guess_the_number():
    """ This function is used to generate a random number between 1 and 100 and ask the user to guess the number, and provide feedback to the user after each guess. It returns the number of guesses it took for the user to guess correctly.

    Returns:
        int: The number of guesses it took for the user to guess correctly.
    """
    
    number = random.randint(1,100)
    count = 0
    while True:
        guess = input("What is your guess? ")
        if guess.isnumeric():
            guess = int(guess)
            count += 1
            if guess == number:
                if count == 1:
                    print(f"Congratulations! You guessed the number in {count} guess.")
                else:
                    print(f"Congratulations! You guessed the number in {count} guesses.")
                break
            elif guess > number:
                print(f"You are wrong! You guessed the number in {count} guesses. You guessed too high.")
            elif guess < number:
                print(f"You are wrong! You guessed the number in {count} guesses. You guessed too low.")
        else:
            print("You are completely wrong! The number is between 1 and 100.")
            break
    return count

if __name__ == '__main__':
    guess_the_number()
    
        