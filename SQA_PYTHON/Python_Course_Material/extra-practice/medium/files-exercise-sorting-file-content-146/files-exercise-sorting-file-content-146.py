"""
Exercise: Python File Sorting Challenge (id=146)

Tests for the function are included. Run this script to test your function.
To just try your function without running the tests, uncomment your function from the "if name = 'main':" block.
Requirements:

Write a Python function sort_lines(input_file, output_file) that sorts the lines of a text file in alphabetical order.
Your function should adhere to the following requirements:

The function should take two string arguments: input_file (the name of the input file) and output_file (the name of the output file).
The function should check if the input file exists before attempting to sort its lines.
If the input file does not exist, the function should return an error message "Input file not found" and should not create the output file.
If the input file exists, the function should read its contents, sort the lines in alphabetical order, and write the sorted lines to the output file.
The function should return a success message "Lines sorted successfully" upon successful sorting of lines.

Instructions:
Your task is to implement the sort_lines function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid filenames, non-existent filenames, and cases with different line contents and lengths.

Examples:

Valid Filenames:

Input: sort_lines("input.txt", "output.txt")
Expected Output: "Lines sorted successfully"
Explanation: The file input.txt exists and its lines can be sorted alphabetically and written to the output file output.txt.

Non-Existent Filename:

Input: sort_lines("missing.txt", "output.txt")
Expected Output: "Input file not found"
Explanation: The file missing.txt does not exist.

"""
import os
import unittest


def sort_lines(input_file, output_file):
    # <ADD YOUR CODE HERE>
    pass


# Unit Tests
# DO NOT MAKE ANY CHANGES IN THIS CLASS
class TestSortLines(unittest.TestCase):
    current_path = os.path.dirname(os.path.abspath(__file__))

    def test_valid_filenames(self):
        input_file = os.path.join(self.current_path, "input.txt")
        output_file = os.path.join(self.current_path, "output.txt")
        self.assertEqual(sort_lines(input_file, output_file), "Lines sorted successfully")

    def test_non_existent_filename(self):
        input_file = os.path.join(self.current_path, "missing.txt")
        output_file = os.path.join(self.current_path, "output.txt")
        self.assertEqual(sort_lines(input_file, output_file), "Input file not found")


if __name__ == '__main__':
    unittest.main()
