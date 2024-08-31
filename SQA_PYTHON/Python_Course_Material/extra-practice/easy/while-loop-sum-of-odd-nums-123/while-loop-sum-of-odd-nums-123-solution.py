"""
Exercise: Sum of Odd Numbers Challenge (id=123)

* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Requirements:
Write a Python program that finds the sum of all odd numbers from 1 to 100 using a while loop. The program should calculate and return the sum.
Your program should adhere to the following requirements:

The program should use a while loop to iterate over the numbers from 1 to 100.
The program should only consider the odd numbers in the sum calculation.
The program should return the final sum of the odd numbers.
Instructions:

Your task is to implement the program according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your program to verify its correctness.

Example:

Expected Output: 2500
Explanation: The sum of all odd numbers from 1 to 100 is 2500.
"""


def sum_of_odd_numbers():
    total_sum = 0
    num = 1
    while num <= 100:
        if num % 2 != 0:
            total_sum += num
        num += 1
    return total_sum



#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####

import unittest


class TestSumOfOddNumbers(unittest.TestCase):

    def test_sum_of_odd_numbers(self):
        self.assertEqual(sum_of_odd_numbers(), 2500)


if __name__ == "__main__":
    unittest.main()