"""
Exercise: Multiplication Table (id=149)

*Tests for the function are included. Run this script to test your function.
*To just try your function without running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Requirements:
Write a Python function that generates a multiplication table for numbers 1 to given number.
The multiplication table should be returned as a nested list, where each inner list represents a row of the table.

Instructions:
Your task is to implement the multiplication_table function according to the specified requirements.
 Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid and invalid inputs.

Examples:

Valid Input:

Input: multiplication_table(5)
Expected Output: [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
Explanation: The multiplication table for numbers 1 to 5 is as follows:
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
The function should return a nested list representing this table.

Invalid Input:

Input: multiplication_table('invalid')
Expected Output: Invalid input provided
Explanation: The function should not accept any input arguments. Providing a string argument is considered invalid input.

"""


def multiplication_table(num):
    if not isinstance(num, int):
        return "Invalid input provided"

    table = []
    for i in range(1, num + 1):
        row = [i * j for j in range(1, num + 1)]
        table.append(row)
    return table


#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####

import unittest


class TestMultiplicationTable(unittest.TestCase):
    def test_valid_input(self):
        expected_output = [
            [1, 2, 3, 4, 5],
            [2, 4, 6, 8, 10],
            [3, 6, 9, 12, 15],
            [4, 8, 12, 16, 20],
            [5, 10, 15, 20, 25]
        ]
        self.assertEqual(multiplication_table(5), expected_output)

    def test_invalid_input_2(self):
        self.assertEqual(multiplication_table('invalid'), "Invalid input provided")


if __name__ == "__main__":
    unittest.main()
