"""
Exercise: Fibonacci Sequence Challenge (id=120)

* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Requirements:

Write a Python function fibonacci_sequence(n) that takes an integer n as an argument and returns a list containing the Fibonacci sequence up to the nth term. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. The sequence starts with 0 and 1.
Your function should adhere to the following requirements:

The function should take a single integer argument, n.
The function should return a list containing the Fibonacci sequence up to the nth term.
If the input value is not a positive integer, your program should return the message "Please enter a positive integer."
If the input value is not an integer, your program should return the message "Invalid input provided."
Tests for the function are included. Run this script to test your function.
To just try your function without running the tests, uncomment your function from the if __name__ == '__main__': block.

Instructions:

Your task is to implement the program according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid and invalid inputs.

Example:

Valid Input:

Input: 7
Expected Output: [0, 1, 1, 2, 3, 5, 8]
Explanation: The Fibonacci sequence up to the 7th term is [0, 1, 1, 2, 3, 5, 8].

Invalid Input:

Input: -5
Expected Output: Please enter a positive integer.
Explanation: The input value is negative.

Generic Error Input:

Input: "abc"
Expected Output: Invalid input provided
Explanation: The input is not an integer.
"""


def fibonacci_sequence(n):
    if not isinstance(n, int):
        return "Invalid input provided"

    if n < 0:
        return "Please enter a positive integer."

    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence


#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####
import unittest


class TestFibonacciSequence(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(fibonacci_sequence(7), [0, 1, 1, 2, 3, 5, 8])

    def test_invalid_input(self):
        self.assertEqual(fibonacci_sequence(-5), "Please enter a positive integer.")

    def test_generic_error_input(self):
        self.assertEqual(fibonacci_sequence("abc"), "Invalid input provided")


if __name__ == "__main__":
    unittest.main()