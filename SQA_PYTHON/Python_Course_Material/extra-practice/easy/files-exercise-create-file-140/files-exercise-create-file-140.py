"""
Exercise: Python File Creation Challenge (id=140)

Write a Python function create_file(filename) that creates a new file only if the file doesn't exist. 
Your function should adhere to the following requirements:

The function should take one string argument, filename, which is the name of the file to be created.
If the file already exists, your function should return a file error message "File already exists. File error."
If the file does not exist, your function should create a new file with the specified filename and return a success message "File created successfully."
If the filename contains invalid characters, your function should return an error message "Filename contains invalid characters."
If the filename does not end with the extension ".txt", your function should return "The filename must end with the extension '.txt'."
If the filename is too long, your function should return an error message "Filename is too long."
If the filename is too short, your function should return an error message "Filename is too short."

* Tests for the function are included. Run this script to test your function.
* To just try your function witout running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Instructions:
Your task is to implement the create_file function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid filenames and filenames that already exist.

Examples:

Valid Filename:

Input: create_file("newfile.txt")
Expected Output: "File created successfully."
Explanation: The function should successfully create a new file with the name "newfile.txt" and return a success message.

Filename that Already Exists:

Input: create_file("sample.txt")
Expected Output: "File already exists. File error."
Explanation: The file sample.txt already exists and cannot be created.

Invalid Filename (Missing Extension):

Input: create_file("newfile")
Expected Output: "The filename must end with the extension '.txt'."
Explanation: The filename newfile does not end with the extension ".txt".

Filename with Invalid Characters:

Input: create_file("newfile?.txt")
Expected Output: "Filename contains invalid characters."
Explanation: The filename newfile?.txt contains invalid characters.

Filename that is Too Long:

Input: create_file("newfile.txt" * 100)
Expected Output: "Filename is too long."
Explanation: The filename newfile.txt is too long. The maximum length of a filename is 255 characters.

Filename that is Too Short:

Input: create_file("")
Expected Output: "Filename is too short."
Explanation: The filename is too short. The minimum length of a filename is 1 character.

"""
import os

def create_file(filename):
    current_path = os.path.dirname(os.path.realpath(__file__))
    # <ADD YOUR CODE HERE>
    pass

#=======================================
#============UNIT TESTS START===========
#=======================================
# DO NOT MODIFY THE CODE BELOW THIS LINE
import unittest

class TestCreateFile(unittest.TestCase):
    
        def test_valid_filename(self):
            self.assertEqual(create_file("newfile.txt"), "File created successfully.")
            os.remove(os.path.join(os.path.dirname(os.path.realpath(__file__)), "newfile.txt"))
    
        def test_filename_that_already_exists(self):
            self.assertEqual(create_file("sample.txt"), "File already exists. File error.")
        
        def test_ill_formed_filename(self):
            self.assertEqual(create_file("newfile"), "The filename must end with the extension '.txt'.")
            
        def test_filename_with_invalid_characters(self):
            self.assertEqual(create_file("newfile?.txt"), "Filename contains invalid characters.")
        
        def test_filename_that_is_too_long(self):
            self.assertEqual(create_file("newfile.txt" * 100), "Filename is too long.")
        
        def test_filename_that_is_too_short(self):
            self.assertEqual(create_file(""), "Filename is too short.")
            
            
#=======================================
#===========UNIT TESTS END==============
#=======================================
if __name__ == '__main__':
    unittest.main() # This runs our unit tests. you can comment this out if you don't want to run the tests. and uncomment the following lines to just try your function.
    
    # print(create_file("newfile.txt"))
    # os.remove(os.path.join(os.path.dirname(os.path.realpath(__file__)), "newfile.txt"))
    # print(create_file("sample.txt"))
    # print(create_file("newfile"))
    # print(create_file("newfile?.txt"))
    # print(create_file("newfile.txt" * 100))
    # print(create_file(""))
    
    