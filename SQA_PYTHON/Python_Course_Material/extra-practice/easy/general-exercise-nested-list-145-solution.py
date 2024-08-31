"""
Exercise: Difference Between Largest and Smallest Elements in a Nested List (id=145)

Requirements:

You are tasked with creating a Python program that finds the difference between the largest and smallest elements in a nested list.
The nested list contains sublists, and you need to consider both the largest and smallest elements within these sublists to compute the difference.

Function Name: find_difference_in_nested_list(nested_list)

Parameters:

nested_list (list): A nested list containing sublists of integers.
Return Value:
An integer representing the difference between the largest and smallest elements in the nested list.
Example:

Here's an example of how the program should work:
# Find the difference between the largest and smallest elements in a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
difference_result = find_difference_in_nested_list(nested_list)
# The 'difference_result' variable should contain the following:
8  # (9 - 1)
Instructions:

Implement the find_difference_in_nested_list function according to the specified requirements.
Traverse the nested list and find the largest and smallest elements within the sublists.
Calculate the difference between the largest and smallest elements found.
Return the difference as an integer.
"""


def find_difference_in_nested_list(nested_list):
    # Initialize variables to track the largest and smallest values
    largest = None
    smallest = None
    if len(nested_list) == 0:
        return 0

    # Iterate through the sublists
    for sublist in nested_list:
        for element in sublist:
            if largest is None or element > largest:
                largest = element
            if smallest is None or element < smallest:
                smallest = element

    # Calculate the difference
    difference = largest - smallest

    return difference


import unittest


class TestDifferenceInNestedList(unittest.TestCase):

    def test_nested_list_difference(self):
        """
        Test the difference between the largest and smallest elements in a nested list.
        """
        nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(find_difference_in_nested_list(nested_list), 8)

    def test_empty_list(self):
        """
        Test when the nested list is empty.
        """
        nested_list = []
        self.assertEqual(find_difference_in_nested_list(nested_list), 0)

    def test_single_element_list(self):
        """
        Test when the nested list contains a single element.
        """
        nested_list = [[42]]
        self.assertEqual(find_difference_in_nested_list(nested_list), 0)


if __name__ == "__main__":
    unittest.main()
