"""
Exercise: Reverse a List (id=127)
* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Requirements:
Write a Python program that reverses the elements of a given list using a for loop.

Instructions:
Your task is to implement the reverse_list function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.

Please test your function with various input scenarios, including valid and invalid inputs.

Examples:

Valid Input:

Input: reverse_list([1, 2, 3, 4, 5])
Expected Output: [5, 4, 3, 2, 1]
Explanation: The elements of the list [1, 2, 3, 4, 5] are reversed to [5, 4, 3, 2, 1].

Input: reverse_list(['a', 'b', 'c', 'd'])
Expected Output: ['d', 'c', 'b', 'a']
Explanation: The elements of the list ['a', 'b', 'c', 'd'] are reversed to ['d', 'c', 'b', 'a'].

Invalid Input:

Input: reverse_list([])
Expected Output: Empty list provided as input
Explanation: The input list is empty.

Input: reverse_list("invalid")
Expected Output: Invalid input provided
Explanation: The input is not a list.

"""
def reverse_list(lst):
    # <ADD YOUR CODE HERE>
    pass

#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####

import unittest

class TestReverseList(unittest.TestCase):
    def test_valid_input_1(self):
        self.assertEqual(reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_valid_input_2(self):
        self.assertEqual(reverse_list(['a', 'b', 'c', 'd']), ['d', 'c', 'b', 'a'])

    def test_invalid_input_1(self):
        self.assertEqual(reverse_list([]), "Empty list provided as input")

    def test_invalid_input_2(self):
        self.assertEqual(reverse_list("invalid"), "Invalid input provided")

if __name__ == "__main__":
    unittest.main()