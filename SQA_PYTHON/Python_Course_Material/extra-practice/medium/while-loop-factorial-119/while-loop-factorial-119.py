"""
Exercise: Factorial Calculation Challenge (id=119)

* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Requirements:

Write a Python function calculate_factorial(n) that takes an integer n as an argument and returns the factorial of n. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
Your function should adhere to the following requirements:

The function should take a single integer argument, n.
The function should return the factorial of n as an integer.
If the input value is not a positive integer, your program should return the message "Please enter a positive integer."
If the input value is not an integer, your program should return the message "Invalid input provided."
Tests for the function are included. Run this script to test your function.
To just try your function without running the tests, uncomment your function from the if __name__ == '__main__': block.

Instructions:

Your task is to implement the program according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid and invalid inputs.

Example:

Valid Input:

Input: 5
Expected Output: 120
Explanation: The factorial of 5 is calculated as 5 * 4 * 3 * 2 * 1 = 120.

Invalid Input:

Input: -10
Expected Output: Please enter a positive integer.
Explanation: The input value is negative.

Generic Error Input:

Input: "abc"
Expected Output: Invalid input provided
Explanation: The input is not an integer.
"""


def calculate_factorial(n):
    # <ADD YOUR CODE HERE>
    pass



#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####
import unittest


class TestFactorialCalculation(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(calculate_factorial(5), 120)

    def test_invalid_input(self):
        self.assertEqual(calculate_factorial(-10), "Please enter a positive integer.")

    def test_generic_error_input(self):
        self.assertEqual(calculate_factorial("abc"), "Invalid input provided")


if __name__ == "__main__":
    unittest.main()