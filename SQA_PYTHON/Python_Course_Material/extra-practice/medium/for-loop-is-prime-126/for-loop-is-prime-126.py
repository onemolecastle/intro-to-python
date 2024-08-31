

"""
Exercise: Prime Number Check (id=126)
* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Requirements:
Write a Python program that checks if a given number is prime using a for loop.

Instructions:
Your task is to implement the is_prime function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.

Please test your function with various input scenarios, including valid and invalid inputs.

Examples:

Valid Input:

Input: is_prime(7)
Expected Output: True
Explanation: The number 7 is a prime number.

Input: is_prime(15)
Expected Output: False
Explanation: The number 15 is not a prime number.

Input: is_prime(2)
Expected Output: True
Explanation: The number 2 is a prime number.

Invalid Input:

Input: is_prime(-5)
Expected Output: Invalid input provided
Explanation: The input is negative, which is invalid.

Input: is_prime(0)
Expected Output: Invalid input provided
Explanation: The input is 0, which is not a prime number.
"""

def is_prime(num):
    # <ADD YOUR CODE HERE>
    pass


#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####
import unittest

class TestIsPrime(unittest.TestCase):
    def test_valid_input_1(self):
        self.assertEqual(is_prime(7), True)

    def test_valid_input_2(self):
        self.assertEqual(is_prime(15), False)

    def test_valid_input_3(self):
        self.assertEqual(is_prime(2), True)

    def test_invalid_input_1(self):
        self.assertEqual(is_prime(-5), "Invalid input provided")

    def test_invalid_input_2(self):
        self.assertEqual(is_prime(0), "Invalid input provided")


if __name__ == "__main__":
    unittest.main()