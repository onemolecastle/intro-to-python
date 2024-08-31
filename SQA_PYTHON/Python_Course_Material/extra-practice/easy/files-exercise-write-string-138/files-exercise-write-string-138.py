"""
Exercise: Python File Writing Challenge (id=138)

Write a Python function write_file(filename, content) that writes a string to a text file. 
Your function should adhere to the following requirements:

The function should take two string arguments, filename and content, which are the name of the file to be written and the content to be written respectively.
The function should open the file in write mode and write the content to it.
The function should close the file after writing and return a success message "File written successfully."
If the file cannot be opened or written, your function should return an error message "File cannot be opened or written."

* Tests for the function are included. Run this script to test your function.
* To just try your function witout running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Instructions:
Your task is to implement the write_file function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid filenames and content, and filenames that cannot be opened or written.

Examples:

Valid Filename and Content:

Input: write_file("sample.txt", "This is some output.")
Expected Output: "File written successfully."
Explanation: The text "This is some output." is written to the file sample.txt.

This is some output.

Filename that Cannot be Opened or Written:

Input: write_file("read_only.txt", "This will fail.")
Expected Output: "File cannot be opened or written."
Explanation: The file read_only.txt is read-only and cannot be opened or written.

"""
import os

def write_file(filename, content):
    current_path = os.path.dirname(os.path.realpath(__file__))
    # <ADD YOUR CODE HERE>
    pass

#=======================================
#============UNIT TESTS START===========
#=======================================
# DO NOT MODIFY THE CODE BELOW THIS LINE
import unittest

class TestWriteFile(unittest.TestCase):

    def test_valid_filename_and_content(self):
        self.assertEqual(write_file("sample.txt", "This is some output."), "File written successfully.")

    def test_filename_that_cannot_be_opened_or_written(self):
        self.assertEqual(write_file("read_only.txt", "This will fail."), "File cannot be opened or written.")
#=======================================
#===========UNIT TESTS END==============
#=======================================

if __name__ == '__main__':
    unittest.main() # This runs our unit tests. you can comment this out if you don't want to run the tests. and uncomment the following lines to just try your function.
    
    # print(write_file("sample.txt", "This is some output."))
    # print(write_file("read_only.txt", "This will fail."))