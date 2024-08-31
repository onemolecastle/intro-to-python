"""
Exercise: Python File Reading Challenge (id=137)

Write a Python function read_file(filename) that reads a text file and returns its content as a string. 
Your function should adhere to the following requirements:

The function should take one string argument, filename, which is the name of the file to be read.
The function should open the file in read mode and read its content.
The function should close the file after reading and return the content as a string.
If the file does not exist or cannot be opened, your function should return an error message "File not found or cannot be opened."

Instructions:
Your task is to implement the read_file function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid filenames, non-existent filenames, and filenames that cannot be opened.

Examples:

Valid Filename:

Input: read_file("sample.txt")
Expected Output: "This is a sample text file.\nIt has two lines of content."
Explanation: The file sample.txt exists and can be opened.

Non-Existent Filename:

Input: read_file("missing.txt")
Expected Output: "File not found."
Explanation: The file missing.txt does not exist.

Filename that Cannot be Opened:

Input: read_file("corrupted.txt")
Expected Output: "File cannot be opened."
Explanation: The file corrupted.txt is corrupted and cannot be opened.

"""
import os
def read_file(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    # <ADD YOUR CODE HERE>
    pass

#=======================================
#============UNIT TESTS START===========
#=======================================
# DO NOT MODIFY THE CODE BELOW THIS LINE
import unittest

class TestReadFile(unittest.TestCase):
    
    def test_valid_filename(self):
        
        self.assertEqual(read_file("sample.txt"), "This is a sample text file.\nIt has two lines of content.")

    def test_non_existent_filename(self):
        self.assertEqual(read_file("missing.txt"), "File not found.")

    def test_filename_that_cannot_be_opened(self):
        self.assertEqual(read_file("corrupted.txt"), "File cannot be opened.")
        
#=======================================
#===========UNIT TESTS END==============
#=======================================

if __name__ == '__main__':
    unittest.main() # This runs our unit tests. you can comment this out if you don't want to run the tests. and uncomment the following lines to just try your function.
    
    # print(read_file("sample.txt"))
    # print(read_file("missing.txt"))
    # print(read_file("corrupted.txt"))