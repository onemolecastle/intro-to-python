"""
Exercise: Python While Loop Challenge (id=115)

Write a Python program that takes an integer input and returns all the even numbers from 0 to that number using a while loop. 
Your program should adhere to the following requirements:
- If the input value is not a positive integer, your program should return "The input value <input_value> is invalid. Please enter a positive integer." message.
- If the input value is not an integer, your program should return "Invalid input provided" message.

* Tests for the function are included. Run this script to test your function.
* To just try your function witout running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Instructions:
Your task is to implement the program according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid and invalid inputs.

Examples:

Valid Input:

Input: 10
Expected Output: [2, 4, 6, 8, 10]
Explanation: The even numbers from 0 to 10 are 2, 4, 6, 8, 10.

Invalid Input:

Input: -10
Expected Output: The input value -10 is invalid. Please enter a positive integer.
- where -10 is the input value, so you need to replace it with the actual input value.
Explanation: The input value is negative.

Generic Error Input:

Input: "abc"
Expected Output: Invalid input provided
Explanation: The input is not an integer.

"""

def even_numbers(n):
    
    if not isinstance(n, int):
        return "Invalid input provided"
    
    if n < 0:
        
        return f"The input value {n} is invalid. Please enter a positive integer."
    
    i = 2
    even_numbers = []
    while i <= n:
        if i % 2 == 0:
            even_numbers.append(i)
        i += 2
    return even_numbers
#=======================================
#============UNIT TESTS START===========
#=======================================
# DO NOT MODIFY THE CODE BELOW THIS LINE
import unittest

class TestEvenNumbers(unittest.TestCase):
                
                def test_valid_input(self):
                    self.assertEqual(even_numbers(10), [2, 4, 6, 8, 10])
                
                def test_invalid_input(self):
                    self.assertEqual(even_numbers(-10), "The input value -10 is invalid. Please enter a positive integer.")
                
                def test_generic_error_input(self):
                    self.assertEqual(even_numbers("abc"), "Invalid input provided")
                    
#=======================================
#===========UNIT TESTS END==============
#=======================================

if __name__ == "__main__":
    unittest.main() # This runs our unit tests. you can comment this out if you don't want to run the tests. and uncomment the following lines to just try your function.
    
    #even_numbers(10)
    #even_numbers(-10)
    