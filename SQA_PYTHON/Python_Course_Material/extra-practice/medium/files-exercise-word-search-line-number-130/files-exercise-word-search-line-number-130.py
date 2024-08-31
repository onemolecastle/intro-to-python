"""
Exercise: Python File Word Search Challenge (id=130)

Tests for the function are included. Run this script to test your function.
To just try your function without running the tests, uncomment your function from the "if name = 'main':" block.
Requirements:

Write a Python function search_word(input_file, search_word) that searches for a specific word in a text file and prints the line(s) where it occurs.
Your function should adhere to the following requirements:

The function should take two string arguments: input_file (the name of the input file) and search_word (the word to search for).
The function should check if the input file exists before attempting to search for the word.
If the input file does not exist, the function should return an error message "Input file not found".
If the input file exists, the function should read its contents and search for the word.
For each line that contains the word, the function should print the line number and the line itself.
The line numbers should start from 1.
If the word is not found in any line, the function should print a message "Word not found in the file."

Instructions:
Your task is to implement the search_word function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid filenames, non-existent filenames, and cases with different line contents and lengths.

Examples:

Valid Filename and Word Found:

Input: search_word("input.txt", "apple")
Expected Output:
1: I have an apple.
3: She likes to eat apples.

Explanation: The file input.txt exists and contains the word "apple" on lines 1 and 3. The function prints the line numbers and the lines themselves.

Valid Filename and Word Not Found:

Input: search_word("input.txt", "banana")
Expected Output: "Word not found in the file."
Explanation: The file input.txt exists, but it does not contain the word "banana". The function prints a message indicating that the word was not found.

Non-Existent Filename:

Input: search_word("missing.txt", "apple")
Expected Output: "Input file not found."
Explanation: The file missing.txt does not exist. The function prints an error message indicating that the input file was not found.

"""
import os
import unittest


def search_word(input_file, search_word):
    # <ADD YOUR CODE HERE>
    pass


# Unit Tests
# DO NOT MAKE ANY CHANGES IN THIS CLASS
class TestSearchWord(unittest.TestCase):
    current_path = os.path.dirname(os.path.abspath(__file__))

    def test_valid_filename_word_found(self):
        input_file = os.path.join(self.current_path, "input.txt")
        search_word_data = "apple"
        expected_output = """
1: I have an apple.
3: She likes to eat apple."""
        print(search_word(input_file, search_word_data))
        self.assertEqual(search_word(input_file,search_word_data), expected_output)

    def test_valid_filename_word_not_found(self):
        input_file = os.path.join(self.current_path, "input.txt")
        search_word_data = "banana"
        expected_output = "Word not found in the file."
        self.assertEqual(search_word(input_file, search_word_data), expected_output)

    def test_non_existent_filename(self):
        input_file = os.path.join(self.current_path, "missing.txt")
        search_word_data = "apple"
        expected_output = "Input file not found."
        self.assertEqual(search_word(input_file, search_word_data), expected_output)


if __name__ == '__main__':
    unittest.main()
