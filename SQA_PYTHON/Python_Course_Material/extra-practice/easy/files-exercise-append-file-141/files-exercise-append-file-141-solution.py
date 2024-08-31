"""
Exercise: Python File Append Challenge (id=140)

Write a Python function append_file(filename, text) that appends text to a file. 
Your function should adhere to the following requirements:

The function should take two string arguments, filename and text, which are the name of the file to be appended and the text to be appended respectively.
If the file does not exist, your function should return a message "File does not exist."
If the file already exists, your function should open it in append mode and append the text to it.
If the filename is invalid, your function should return a message "Invalid filename."
If the text is empty, your function should return a message "Text cannot be empty."
If the file cannot be opened or read, your function should return a message "Could not read file contents."

Your function should return a success message "Text appended successfully." if the text is added to the file successfully.

* Tests for the function are included. Run this script to test your function.
* To just try your function witout running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Instructions:
Your task is to implement the append_file function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid filenames and filenames that do not exist.

Examples:

Valid Filename and Text: 

Input: append_file("sample.txt", "This is some new text.")
Expected Output: "Text appended successfully."
Explanation: The text "This is some new text." is appended to the file sample.txt.

Nonexistent Filename:

Input: append_file("nonexistent.txt", "This is some new text.")
Expected Output: "File does not exist."
Explanation: The file nonexistent.txt does not exist.

Invalid Filename 

Input: append_file("", "This is some new text.")
Expected Output: "Invalid filename."
Explanation: The filename is empty.

Invalid Text:

Input: append_file("sample.txt", "")
Expected Output: "Text cannot be empty."
Explanation: The text is empty.

Could not read file contents:

Input: append_file("corrupted.txt", "This is some new text.")
Expected Output: "Could not read file contents."
Explanation: The file corrupted.txt is corrupted and cannot be read.

"""

import os
import re

def append_file(filename, text):
    current_path = os.path.dirname(os.path.realpath(__file__))
    if re.search(r"[^a-zA-Z0-9_.-]", filename) or filename == "" or not filename.endswith(".txt"):
        return "Invalid filename."
    elif not os.path.exists(os.path.join(current_path, filename)):
        return "File does not exist."
    elif text == "":
        return "Text cannot be empty."
    else:
        try:
            # Check if file can be read
            with open(os.path.join(current_path, filename), "r") as file:
                file.read()
            with open(os.path.join(current_path, filename), "a") as file:
                file.write(text)
            return "Text appended successfully."
        except:
            return "Could not read file contents."
    

#=======================================
#============UNIT TESTS START===========
#=======================================
# DO NOT MODIFY THE CODE BELOW THIS LINE
import unittest

class TestAppendFile(unittest.TestCase):
 
            def test_valid_filename(self):
                self.assertEqual(append_file("sample.txt", "This is some new text."), "Text appended successfully.")
                
            def test_invalid_filename(self):
                self.assertEqual(append_file("", "This is some new text."), "Invalid filename.")
            
            def test_invalid_text(self):
                self.assertEqual(append_file("sample.txt", ""), "Text cannot be empty.")
            
            def test_file_does_not_exist(self):
                self.assertEqual(append_file("nonexistent.txt", "This is some new text."), "File does not exist.")
            
            def test_could_not_read_file_contents(self):
                self.assertEqual(append_file("corrupted.txt", "This is some new text."), "Could not read file contents.")
                
#=======================================
#===========UNIT TESTS END==============
#=======================================

if __name__ == '__main__':
    unittest.main() # This runs our unit tests. you can comment this out if you don't want to run the tests. and uncomment the following lines to just try your function.
    
    # print(append_file("newfile.txt", "This is some new text.")).
    # print(append_file("sample.txt", ""))
    # print(append_file("", "This is some new text."))
    # print(append_file("nonexistent.txt", "This is some new text."))
    # print(append_file("corrupted.txt", "This is some new text."))
    # print(append_file("sample.txt", "This is some new text."))
    