"""
Exercise: Find the Smallest Element in a List (id=125)
* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Requirements:
Write a Python program that finds the smallest element in a given list using a for loop.

Instructions:
Your task is to implement the find_smallest_element function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.

Please test your function with various input scenarios, including valid and invalid inputs.

Examples:

Valid Input:

Input: find_smallest_element([5, 2, 8, 1, 10])
Expected Output: 1
Explanation: The smallest element in the list [5, 2, 8, 1, 10] is 1.

Input: find_smallest_element([-3, 0, 2, -5, 1])
Expected Output: -5
Explanation: The smallest element in the list [-3, 0, 2, -5, 1] is -5.

Invalid Input:

Input: find_smallest_element([])
Expected Output: Empty list provided as input
Explanation: The input list is empty.

Input: find_smallest_element("invalid")
Expected Output: Invalid input provided
Explanation: The input is not a list.

python
"""

def find_smallest_element(lst):
    # <ADD YOUR CODE HERE>
    pass


#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####
import unittest


class TestFindSmallestElement(unittest.TestCase):
    def test_valid_input_1(self):
        self.assertEqual(find_smallest_element([5, 2, 8, 1, 10]), 1)

    def test_valid_input_2(self):
        self.assertEqual(find_smallest_element([-3, 0, 2, -5, 1]), -5)

    def test_invalid_input_1(self):
        self.assertEqual(find_smallest_element([]), "Empty list provided as input")

    def test_invalid_input_2(self):
        self.assertEqual(find_smallest_element("invalid"), "Invalid input provided")


if __name__ == "__main__":
    unittest.main()