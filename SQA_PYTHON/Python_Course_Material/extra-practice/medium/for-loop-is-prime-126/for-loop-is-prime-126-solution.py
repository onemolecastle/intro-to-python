
"""
Exercise: Prime Number Check (id=126)
* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Requirements:
Write a Python program that checks if a given number is prime using a for loop.

Instructions:
Your task is to implement the is_prime function according to the specified requirements. 
Make sure to handle any possible exceptions and return the appropriate messages or results.

*A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
In other words, if a number 'n' is prime, it is not divisible by any number between 2 and the square root of 'n'.

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
    if not isinstance(num, int) or num < 2:
        return "Invalid input provided"

    max_divisor = int(num ** 0.5) + 1
    for i in range(2, max_divisor):
        if num % i == 0:
            return False

    return True


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