"""
Exercise: List Intersection (id=144)

Requirements:

You are tasked with creating a Python function that finds the intersection of two lists.
The intersection of two lists consists of the elements that are common to both lists.
Function Name: find_intersection(list1, list2)

Parameters:

list1 (list): The first list containing elements.
list2 (list): The second list containing elements.
Return Value:
A list containing elements that are common to both input lists.
Example:

Here's an example of how the program should work:
# Find the intersection of two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection_result = find_intersection(list1, list2)
# The 'intersection_result' variable should contain the following:
[3, 4, 5]
Instructions:

Implement the find_intersection function according to the specified requirements.
Use a loop or any other appropriate method to find the common elements in the two input lists.
Return a new list containing the common elements.
Write unit tests to validate the correctness of your function.
"""


def find_intersection(list1, list2):
    # Initialize an empty list to store the intersection
    intersection = []

    # Iterate through elements in list1
    for item in list1:
        # Check if the element is in list2
        if item in list2:
            intersection.append(item)

    return intersection


import unittest


class TestListIntersection(unittest.TestCase):

    def test_intersection(self):
        """
        Test the intersection of two lists.
        """
        list1 = [1, 2, 3, 4, 5]
        list2 = [3, 4, 5, 6, 7]
        self.assertEqual(find_intersection(list1, list2), [3, 4, 5])

    def test_no_intersection(self):
        """
        Test when there is no intersection.
        """
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        self.assertEqual(find_intersection(list1, list2), [])

    def test_empty_lists(self):
        """
        Test when one or both lists are empty.
        """
        list1 = []
        list2 = [1, 2, 3]
        self.assertEqual(find_intersection(list1, list2), [])
        self.assertEqual(find_intersection(list2, list1), [])


if __name__ == "__main__":
    unittest.main()
