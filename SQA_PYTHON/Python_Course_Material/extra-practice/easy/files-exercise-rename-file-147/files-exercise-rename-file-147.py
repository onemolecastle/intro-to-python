"""
Exercise: Python File Renaming Challenge (id=147)

Tests for the function are included. Run this script to test your function.
To just try your function without running the tests, uncomment your function from the "if name = 'main':" block.

Requirements:

Write a Python function rename_file(old_filename, new_filename) that renames a file in the file system.
Your function should adhere to the following requirements:

The function should take two string arguments, old_filename and new_filename, representing the current name and the desired new name of the file, respectively.
The function should check if the file specified by old_filename exists before attempting to rename it.
If the file exists, the function should rename it to new_filename and return a success message.
If the file does not exist, the function should return an error message "File not found."

Instructions:
Your task is to implement the rename_file function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid filenames, non-existent filenames, and cases where the new filename already exists.

Examples:

Valid Filename:

Input: rename_file("data.txt", "new_data.txt")
Expected Output: "File renamed successfully."
Explanation: The file data.txt exists and can be renamed to new_data.txt.

Non-Existent Filename:

Input: rename_file("missing.txt", "new_missing.txt")
Expected Output: "File not found."
Explanation: The file missing.txt does not exist.

Existing New Filename:

Input: rename_file("data.txt", "data.txt")
Expected Output: "File renamed successfully."
Explanation: The file data.txt exists and can be renamed to data.txt, overwriting the existing file.

"""
import os
import unittest


def rename_file(old_filename, new_filename):
    # <ADD YOUR CODE HERE>
    pass

# Unit Tests
# DO NOT MAKE ANY CHANGES IN THIS CLASS


class TestRenameFile(unittest.TestCase):
    current_path = os.path.dirname(os.path.abspath(__file__))
    def test_valid_filename(self):
        old_filename = os.path.join(self.current_path, "data.txt")
        new_filename = os.path.join(self.current_path, "new_data.txt")
        self.assertEqual(rename_file(old_filename, new_filename), "File renamed successfully.")

    def test_non_existent_filename(self):
        old_filename = os.path.join(self.current_path, "missing.txt")
        new_filename = os.path.join(self.current_path, "new_missing.txt")
        self.assertEqual(rename_file(old_filename, new_filename), "File not found.")

    def test_existing_new_filename(self):
        old_filename = os.path.join(self.current_path, "data.txt")
        new_filename = os.path.join(self.current_path, "data.txt")
        self.assertEqual(rename_file(old_filename, new_filename), "File renamed successfully.")

if __name__ == '__main__':
    unittest.main()