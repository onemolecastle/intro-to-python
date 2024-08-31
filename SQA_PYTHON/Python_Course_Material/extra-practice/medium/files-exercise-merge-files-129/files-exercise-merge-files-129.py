"""
Exercise: Python File Merge Challenge (id=129)

Tests for the function are included. Run this script to test your function.
To just try your function without running the tests, uncomment your function from the "if name = 'main':" block.

Requirements:

Write a Python function merge_files(output_file, *input_files) that merges the contents of multiple files into a single file.
Your function should adhere to the following requirements:

The function should take at least two arguments: output_file (string) and *input_files (variable number of strings), representing the name of the output file and the names of the input files, respectively.
The function should check if all the input files exist before attempting to merge them.
If any of the input files do not exist, the function should return an error message "File not found" and should not create the output file.
If all the input files exist, the function should merge their contents into the output file.
The merged contents should be written in the same order as the input files are provided.
The function should return a success message "Files merged successfully" upon successful merging of files.

Instructions:
Your task is to implement the merge_files function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid filenames, non-existent filenames, and cases with different content types (e.g., text files, CSV files, etc.).

Examples:

Valid Filenames:

Input: merge_files("merged.txt", "file1.txt", "file2.txt", "file3.txt")
Expected Output: "Files merged successfully"
Explanation: The files file1.txt, file2.txt, and file3.txt exist and can be merged into the file merged.txt.

Non-Existent Filename:

Input: merge_files("merged.txt", "file1.txt", "missing.txt", "file3.txt")
Expected Output: "File not found"
Explanation: The file missing.txt does not exist.
"""

import os
import unittest


def merge_files(output_file, *input_files):
    # <ADD YOUR CODE HERE>
    pass


#
# Unit Tests
# DO NOT MAKE ANY CHANGES IN THIS CLASS

class TestMergeFiles(unittest.TestCase):
    current_path = os.path.dirname(os.path.abspath(__file__))

    def test_valid_filenames(self):
        input_files = [
            os.path.join(self.current_path, "file1.txt"),
            os.path.join(self.current_path, "file2.txt"),
            os.path.join(self.current_path, "file3.txt")
        ]
        output_file = os.path.join(self.current_path, "merged.txt")
        self.assertEqual(merge_files(output_file, *input_files), "Files merged successfully")

    def test_non_existent_filename(self):
        input_files = [
            os.path.join(self.current_path, "file1.txt"),
            os.path.join(self.current_path, "missing.txt"),
            os.path.join(self.current_path, "file3.txt")
        ]
        output_file = os.path.join(self.current_path, "merged.txt")
        self.assertEqual(merge_files(output_file, *input_files), "File not found")


if __name__ == '__main__':
    unittest.main()
