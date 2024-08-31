"""
Exercise: Iterate Through Dictionary and Return Only Values (id=148)
* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Requirements:
Write a Python function that takes a dictionary as input and returns a list containing only the values from the dictionary. Use a for loop to iterate through the dictionary.

Instructions:
Your task is to implement the get_values function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid and invalid inputs.

Examples:

Valid Input:

Input: get_values({'a': 1, 'b': 2, 'c': 3})
Expected Output: [1, 2, 3]
Explanation: The dictionary {'a': 1, 'b': 2, 'c': 3} contains three key-value pairs. The function should return a list containing only the values [1, 2, 3].

Input: get_values({'name': 'John', 'age': 30, 'city': 'London'})
Expected Output: ['John', 30, 'London']
Explanation: The dictionary {'name': 'John', 'age': 30, 'city': 'London'} contains three key-value pairs. The function should return a list containing only the values ['John', 30, 'London'].

Invalid Input:
Input: get_values('invalid')
Expected Output: Invalid input provided
Explanation: The input is not a dictionary, which is invalid. The function should return an error message indicating invalid input.

Input: get_values(123)
Expected Output: Invalid input provided
Explanation: The input is not a dictionary, which is invalid. The function should return an error message indicating invalid input.

"""


def get_values(dictionary):
    # < ADD YOUR CODE HERE >
    pass


#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####
import unittest


class TestGetValues(unittest.TestCase):
    def test_valid_input_1(self):
        self.assertEqual(get_values({'a': 1, 'b': 2, 'c': 3}), [1, 2, 3])

    def test_valid_input_2(self):
        self.assertEqual(get_values({'name': 'John', 'age': 30, 'city': 'London'}), ['John', 30, 'London'])

    def test_valid_input_3(self):
        self.assertEqual(get_values({'a': 1, 'b': 2, 'c': [1, 2, 3]}), [1, 2, [1, 2, 3]])

    def test_invalid_input_1(self):
        self.assertEqual(get_values('invalid'), "Invalid input provided")

    def test_invalid_input_2(self):
        self.assertEqual(get_values(123), "Invalid input provided")


if __name__ == "__main__":
    unittest.main()