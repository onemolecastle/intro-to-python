"""
Exercise: String Reversal Challenge (id=121)

* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Requirements:
Write a Python function reverse_string(string) that takes a string string as an argument and returns the reversed version of the string using a while loop. The reversed string should have the characters in the opposite order.
Your function should adhere to the following requirements:

The function should take a single string argument, string.
The function should return the reversed version of the string.
If the input value is not a string, your program should return the message "Invalid input provided."
Tests for the function are included. Run this script to test your function.
To just try your function without running the tests, uncomment your function from the if __name__ == '__main__': block.

Instructions:

Your task is to implement the program according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid and invalid inputs.

Example:

Valid Input:

Input: "Hello, World!"
Expected Output: "!dlroW ,olleH"
Explanation: The reversed version of the string "Hello, World!" is "!dlroW ,olleH".

Invalid Input:

Input: 12345
Expected Output: Invalid input provided
Explanation: The input value is not a string

"""

def reverse_string(string):
    # <ADD YOUR CODE HERE>
    pass

#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####
import unittest


class TestStringReversal(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(reverse_string("Hello, World!"), "!dlroW ,olleH")

    def test_invalid_input(self):
        self.assertEqual(reverse_string(12345), "Invalid input provided")



if __name__ == "__main__":
    unittest.main()