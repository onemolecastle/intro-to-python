"""
Exercise: Vowel Counter (id=117)

* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ == '__main__':" block.

Requirements:

Write a Python function `count_vowels(text)` that counts the number of vowels (both lowercase and uppercase) in a given text and returns the count.

Function Name: count_vowels(text)

Parameters:
- `text` (str): The input text in which you need to count vowels.

Returns:
- (int): The total count of vowels (both lowercase and uppercase) in the input text.

Instructions:

1. Implement the `count_vowels` function according to the specified requirements.
2. Use a loop to iterate through each character in the input text.
3. Check if each character is a vowel (either lowercase or uppercase).
4. Keep a count of the vowels encountered.
5. Return the total count of vowels.

Examples:

Here are some examples to illustrate the expected behavior of your function:

Input: count_vowels("Hello, World!")
Expected Output: 3 (The vowels are 'e', 'o', and 'o')

Input: count_vowels("Python is awesome")
Expected Output: 6 (The vowels are 'o', 'i', 'o', 'e', 'a', and 'e')

Input: count_vowels("AEIOU")
Expected Output: 5 (All uppercase vowels)

Empty Text:
Input: count_vowels("")
Expected Output: 0 (No vowels in an empty text)
"""

import unittest

def count_vowels(text):
    # <your code here>
    pass

# Unit tests
class TestCountVowels(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(count_vowels("Hello, World!"), 3)

    def test_example2(self):
        self.assertEqual(count_vowels("Python is awesome"), 6)

    def test_all_uppercase_vowels(self):
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_empty_text(self):
        self.assertEqual(count_vowels(""), 0)

if __name__ == "__main__":
    unittest.main()
