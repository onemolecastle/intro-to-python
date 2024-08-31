"""
Exercise: Sum of Squares of Prime Numbers (id=124)
* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Requirements:
Write a Python program that finds the sum of the squares of prime numbers, using a for loop.

Instructions:
Your task is to implement the sum_of_squares_of_primes function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.

Please test your function with various input scenarios, including valid and invalid inputs.

Examples:

Valid Input:

Input: sum_of_squares_of_primes(1, 10)
Expected Output: 38
Explanation: The prime numbers between 1 and 10 are [2, 3, 5, 7]. The sum of the squares of these prime numbers is 2^2 + 3^2 + 5^2 + 7^2 = 38.

Input: sum_of_squares_of_primes(1, 20)
Expected Output: 227
Explanation: The prime numbers between 1 and 20 are [2, 3, 5, 7, 11, 13, 17, 19]. The sum of the squares of these prime numbers is 2^2 + 3^2 + 5^2 + 7^2 + 11^2 + 13^2 + 17^2 + 19^2 = 227.

Invalid Input:

Input: sum_of_squares_of_primes(20, 10)
Expected Output: Invalid input provided
Explanation: The starting number is greater than the ending number, which is invalid.

Input: sum_of_squares_of_primes(1, -10)
Expected Output: Invalid input provided
Explanation: The ending number is negative, which is invalid.

Input: sum_of_squares_of_primes(1.5, 10)
Expected Output: Invalid input provided
Explanation: The input contains a floating-point number, which is invalid.

Input: sum_of_squares_of_primes(1, "10")
Expected Output: Invalid input provided
Explanation: The ending number is a string, which is invalid.

Note:

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
You can assume that both the starting and ending numbers are integers.
"""


def sum_of_squares_of_primes(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        return "Invalid input provided"
    if start > end:
        return "Invalid input provided"
    if end < 0:
        return "Invalid input provided"

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)

    sum_of_squares = sum([prime ** 2 for prime in primes])
    return sum_of_squares


#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####
import unittest


class TestSumOfSquaresOfPrimes(unittest.TestCase):
    def test_valid_input_1(self):
        self.assertEqual(sum_of_squares_of_primes(1, 10), 87)

    def test_valid_input_2(self):
        self.assertEqual(sum_of_squares_of_primes(1, 20), 1027)

    def test_invalid_input_1(self):
        self.assertEqual(sum_of_squares_of_primes(20, 10), "Invalid input provided")

    def test_invalid_input_2(self):
        self.assertEqual(sum_of_squares_of_primes(1, -10), "Invalid input provided")

    def test_invalid_input_3(self):
        self.assertEqual(sum_of_squares_of_primes(1.5, 10), "Invalid input provided")

    def test_invalid_input_4(self):
        self.assertEqual(sum_of_squares_of_primes(1, "10"), "Invalid input provided")


if __name__ == "__main__":
    unittest.main()