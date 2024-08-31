"""
Exercise: Strings Starting with Vowels (id=111)

Write a Python function strings_starting_with_vowels(lst) that takes a list of strings as input and returns a new list containing only the strings that start with a vowel.
- If no strings starting with vowels were found, return the string "No strings starting with vowels were found in the list" message. 
- If the input is not a list, return "Invalid input provided" message. 
- If the input list is empty, return "Empty list provided as input" message.

* Tests for the function are included. Run this script to test your function.
* To just try your function witout running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Instructions:
Your task is to implement the strings_starting_with_vowels function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid and invalid lists.

Examples:

Valid Input:

Input: strings_starting_with_vowels(['apple', 'banana', 'cherry', 'orange', 'pear'])
Expected Output: ['apple', 'orange']
Explanation: The strings starting with vowels in the list ['apple', 'banana', 'cherry', 'orange', 'pear'] are 'apple' and 'orange'. both start with the letter 'a' and 'o'.

Input2: strings_starting_with_vowels(['cherry', 'pear'])
Expected Output: No strings starting with vowels were found in the list
Explanation: There are no strings starting with vowels in the list ['cherry', 'pear'].

Invalid Input:

Input: strings_starting_with_vowels([])
Expected Output: Empty list provided as input
Explanation: The input list is empty.

Generic Error Input:
 
Input: strings_starting_with_vowels(123)
Expected Output: Invalid input provided
Explanation: The input is not a list.

"""

def strings_starting_with_vowels(lst):

    if not isinstance(lst, list):
        return "Invalid input provided"
    if len(lst) == 0:
        return "Empty list provided as input"
    
    result = []
    for i in lst:
        if i[0] in ['a', 'e', 'i', 'o', 'u']:
            result.append(i)
    if len(result) == 0:
        return "No strings starting with vowels were found in the list"
    return result

#=======================================
#============UNIT TESTS START===========
#=======================================
# DO NOT MODIFY THE CODE BELOW THIS LINE
import unittest

class TestStringsStartingWithVowels(unittest.TestCase):
        
        def test_valid_input(self):
            self.assertEqual(strings_starting_with_vowels(['apple', 'banana', 'cherry', 'orange', 'pear']), ['apple', 'orange'])
        
        def test_invalid_input(self):
            self.assertEqual(strings_starting_with_vowels([]), "Empty list provided as input")
        
        def test_generic_error_input(self):
            self.assertEqual(strings_starting_with_vowels(123), "Invalid input provided")
            
#=======================================
#===========UNIT TESTS END==============
#=======================================

if __name__ == "__main__":
    unittest.main() # This runs our unit tests. you can comment this out if you don't want to run the tests. and uncomment the following lines to just try your function.
    
    #print(strings_starting_with_vowels(['apple', 'banana', 'cherry', 'orange', 'pear']))
    #print(strings_starting_with_vowels(['apple', 'banana', 'cherry', 'orange', 'pear', '123']))
    