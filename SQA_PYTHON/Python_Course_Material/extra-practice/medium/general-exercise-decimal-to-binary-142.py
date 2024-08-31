"""
Exercise: Decimal to Binary Converter (id=142)

Requirements:

You are tasked with creating a Python program that converts a decimal number to its binary equivalent.
This program should take a decimal integer as input and return its binary representation as a string.

Function Name: decimal_to_binary(decimal)

Parameters:

decimal (int): An integer representing the decimal number to be converted.
Return Value:
A string representing the binary equivalent of the input decimal number.
Decimal to Binary Conversion Algorithm:
To convert a decimal number to binary, you can use the following algorithm:
Initialize an empty string to store the binary representation.
Repeat the following steps until the decimal number becomes zero:
Divide the decimal number by 2.
Append the remainder (either 0 or 1) to the binary representation string.
Update the decimal number with the integer division result.
Reverse the binary representation string to obtain the correct binary value.

Example:

Here's an example of how the program should work:
# Convert a decimal number to binary
binary_result = decimal_to_binary(10)

# The 'binary_result' variable should contain the following:
"1010"
Instructions:

Implement the decimal_to_binary function according to the specified requirements and the conversion algorithm provided.
Return the binary representation as a string.
Write unit tests to validate the correctness of your function.
"""


def decimal_to_binary(decimal):
    # < ADD YOUR CODE HERE >
    pass


#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####
import unittest


class TestDecimalToBinaryConverter(unittest.TestCase):

    def test_binary_conversion(self):
        """
        Test the conversion of a decimal number to binary.
        """
        self.assertEqual(decimal_to_binary(10), "1010")

    def test_binary_conversion_zero(self):
        """
        Test the conversion of zero to binary.
        """
        self.assertEqual(decimal_to_binary(0), "0000")

    def test_binary_conversion_large_number(self):
        """
        Test the conversion of a large decimal number to binary.
        """
        self.assertEqual(decimal_to_binary(255), "11111111")


if __name__ == "__main__":
    unittest.main()
