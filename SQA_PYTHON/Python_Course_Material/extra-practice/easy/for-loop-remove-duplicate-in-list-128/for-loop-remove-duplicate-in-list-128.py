"""
Exercise: Remove Duplicate Elements from a List (id=128)
* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Requirements:
Write a Python program that removes duplicate elements from a given list and creates a new list with unique elements using a for loop.

Instructions:
Your task is to implement the remove_duplicates function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.

Please test your function with various input scenarios, including valid and invalid inputs.

Examples:

Valid Input:

Input: remove_duplicates([1, 2, 2, 3, 4, 4, 5])
Expected Output: [1, 2, 3, 4, 5]
Explanation: The duplicates in the list [1, 2, 2, 3, 4, 4, 5] are removed, resulting in a new list with unique elements [1, 2, 3, 4, 5].

Input: remove_duplicates(['a', 'b', 'b', 'c', 'c', 'c'])
Expected Output: ['a', 'b', 'c']
Explanation: The duplicates in the list ['a', 'b', 'b', 'c', 'c', 'c'] are removed, resulting in a new list with unique elements ['a', 'b', 'c'].

Invalid Input:

Input: remove_duplicates([])
Expected Output: Empty list provided as input
Explanation: The input list is empty.

Input: remove_duplicates("invalid")
Expected Output: Invalid input provided
Explanation: The input is not a list.
"""


def remove_duplicates(lst):
    # <ADD YOUR CODE HERE>
    pass

#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####

import unittest


class TestRemoveDuplicates(unittest.TestCase):
    def test_valid_input_1(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_valid_input_2(self):
        self.assertEqual(remove_duplicates(['a', 'b', 'b', 'c', 'c', 'c']), ['a', 'b', 'c'])

    def test_invalid_input_1(self):
        self.assertEqual(remove_duplicates([]), "Empty list provided as input")

    def test_invalid_input_2(self):
        self.assertEqual(remove_duplicates("invalid"), "Invalid input provided")


if __name__ == "__main__":
    unittest.main()