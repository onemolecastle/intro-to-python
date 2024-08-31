"""
Exercise: Sum of Numbers Divisible by Three and Five (id=112)

Write a Python function sum_divisible_by_three_and_five(lst) that takes a list of integers as input and returns the sum of all numbers that are divisible by three and five.
- If the input is not a list, return "Invalid input provided" message.
- If the input list is empty, return "Empty list provided as input" message.

* Tests for the function are included. Run this script to test your function.
* To just try your function witout running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Instructions:
Your task is to implement the sum_divisible_by_three_and_five function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid and invalid lists.

Examples:

Valid Input:

Input: sum_divisible_by_three_and_five([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
Expected Output: 45
Explanation: The sum of numbers divisible by three and five in the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is 45. The numbers divisible by three and five are 15, 30, 45, 60, 75, 90, 105, 120, 135, 150.

Invalid Input:

Input: sum_divisible_by_three_and_five([])
Expected Output: Empty list provided as input
Explanation: The input list is empty.

Generic Error Input:

Input: sum_divisible_by_three_and_five(123)
Expected Output: Invalid input provided
Explanation: The input is not a list.

"""

def sum_divisible_by_three_and_five(lst):
    
    if not isinstance(lst, list):
        return "Invalid input provided"
    if len(lst) == 0:
        return "Empty list provided as input"
    
    sum = 0
    for i in lst:
        if i % 3 == 0 and i % 5 == 0:
            sum += i
    return sum

#=======================================
#============UNIT TESTS START===========
#=======================================
# DO NOT MODIFY THE CODE BELOW THIS LINE
import unittest

class TestSumDivisibleByThreeAndFive(unittest.TestCase):
    
    def test_valid_input(self):
        self.assertEqual(sum_divisible_by_three_and_five([1, 2, 3, 4, 5, 6, 7, 8, 9, 15]), 15)
    
    def test_invalid_input(self):
        self.assertEqual(sum_divisible_by_three_and_five([]),"Empty list provided as input")
    
    def test_generic_error_input(self):
        self.assertEqual(sum_divisible_by_three_and_five(123), "Invalid input provided")
        
#=======================================
#===========UNIT TESTS END==============
#=======================================

if __name__ == "__main__":
    unittest.main() # This runs our unit tests. you can comment this out if you don't want to run the tests. and uncomment the following lines to just try your function.
    
    #print(sum_divisible_by_three_and_five([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    #print(sum_divisible_by_three_and_five([1, 2, 4, 7, 8, 11, 13]))
    