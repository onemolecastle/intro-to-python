"""
Exercise: List Analysis (id=202)

* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ == '__main__':" block.

Requirements:

Write a Python function analyze_list(numbers) that analyzes a list of integers and returns a dictionary containing the following information:

- "sum": The sum of all the numbers in the list.
- "average": The average of the numbers in the list (rounded to two decimal places).
- "min": The minimum number in the list.
- "max": The maximum number in the list.

Function Name: analyze_list(numbers)

Parameters:
- numbers (list): A list of integers.

Your function should return a dictionary with the keys "sum," "average," "min," and "max," each corresponding to the respective statistic.

Instructions:

1. Implement the `analyze_list` function according to the specified requirements.
2. Use loops to calculate the sum, average, minimum, and maximum values.
3. Round the average to two decimal places using the `round()` function.
4. Return the results as a dictionary.

Examples:

Here are some examples to illustrate the expected behavior of your function:

Input: analyze_list([1, 2, 3, 4, 5])
Expected Output: {"sum": 15, "average": 3.00, "min": 1, "max": 5}

Input: analyze_list([10, -5, 8, 20, 2])
Expected Output: {"sum": 35, "average": 7.00, "min": -5, "max": 20}

Input: analyze_list([])
Expected Output: {"sum": 0, "average": 0.00, "min": None, "max": None}

"""

import unittest

def analyze_list(numbers):
    try:
       # <your code here>
       pass
    except Exception:
        # Handle any exceptions by returning None for all stats
        return {"sum": None, "average": None, "min": None, "max": None}

# Unit tests
class TestAnalyzeList(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(analyze_list([1, 2, 3, 4, 5]), {"sum": 15, "average": 3.00, "min": 1, "max": 5})

    def test_example2(self):
        self.assertEqual(analyze_list([10, -5, 8, 20, 2]), {"sum": 35, "average": 7.00, "min": -5, "max": 20})

    def test_empty_list(self):
        self.assertEqual(analyze_list([]), {"sum": 0, "average": 0.00, "min": None, "max": None})

    def test_invalid_input1(self):
        self.assertEqual(analyze_list("numbers"), {"sum": None, "average": None, "min": None, "max": None})

    def test_invalid_input2(self):
        self.assertEqual(analyze_list([1, 2, "3", 4, 5]), {"sum": None, "average": None, "min": None, "max": None})

if __name__ == "__main__":
    unittest.main()
