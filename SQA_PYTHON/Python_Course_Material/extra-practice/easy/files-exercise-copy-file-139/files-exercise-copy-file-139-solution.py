"""
Exercise: Python File Copying Challenge (id=139)

Write a Python function copy_file(source, destination) that copies a text file from one location to another. 
Your function should adhere to the following requirements:

The function should take two string arguments, source and destination, which are the names of the source file and the destination file respectively.
The function should open the source file in read mode and read its content.
The function should open the destination file in write mode and write the content of the source file to it.
The function should close both files after copying and return a success message "File copied successfully."
If either the source file or the destination file does not exist or cannot be opened, your function should return an error message "Source file not found."
If the source file is corrupted, your function should return an error message "File you are trying to copy is corrupted."

* Tests for the function are included. Run this script to test your function.
* To just try your function witout running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Instructions:
Your task is to implement the copy_file function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid source and destination filenames, non-existent source or destination filenames, and source or destination filenames that cannot be opened.

Examples:

Valid Source and Destination Filenames:

Input: copy_file("sample.txt", "copy.txt")
Expected Output: "File copied successfully."
Explanation: The content of the file sample.txt is copied to the file copy.txt.

Non-Existent Source Filename:

Input: copy_file("missing.txt", "copy.txt")
Expected Output: "Source file not found."
Explanation: The file missing.txt does not exist.

Corrupted Source Filename:

Input: copy_file("corrupted.txt", "copy.txt")
Expected Output: "File you are trying to copy is corrupted."
Explanation: The file corrupted.txt is corrupted and cannot be opened.

"""
import os

def copy_file(source, destination):
    current_path = os.path.dirname(os.path.realpath(__file__))
    try:
        source_file = open(os.path.join(current_path, source), "r")
        content=source_file.read()
        source_file.close()
        destination_file = open(os.path.join(current_path, destination), "w")
        destination_file.write(content)
        destination_file.close()
        return "File copied successfully."
    except FileNotFoundError:
        return "Source file not found."
    except UnicodeDecodeError or PermissionError or OSError or IOError:
        source_file.close()
        return "The file you are trying to copy is corrupted or cannot be opened."

#=======================================
#============UNIT TESTS START===========
#=======================================
# DO NOT MODIFY THE CODE BELOW THIS LINE
import unittest

class TestCopyFile(unittest.TestCase):
    current_path = os.path.dirname(os.path.realpath(__file__))
    def test_valid_source_and_destination_filenames(self):
        self.assertEqual(copy_file("sample.txt","copy.txt"),"File copied successfully.")
        os.remove(os.path.join(self.current_path, "copy.txt"))

    def test_non_existent_source_filename(self):
        self.assertEqual(copy_file("missing.txt","copy.txt"), "Source file not found.")

    def test_non_existent_destination_filename(self):
        self.assertEqual(copy_file("corrupted.txt","copy.txt"), "The file you are trying to copy is corrupted or cannot be opened.")
#=======================================
#===========UNIT TESTS END==============
#=======================================

if __name__ == '__main__':
    unittest.main()# This runs our unit tests. you can comment this out if you don't want to run the tests. and uncomment the following lines to just try your function.
    
    # print(copy_file("sample.txt", "copy.txt"))
    # print(copy_file("missing.txt", "copy.txt"))
    # print(copy_file("corrupted.txt", "copy.txt"))
