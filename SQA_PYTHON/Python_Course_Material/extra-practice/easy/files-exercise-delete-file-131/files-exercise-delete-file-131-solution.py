"""
Exercise: Python File Deletion Challenge (id=131)

* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Requirements:

Write a Python function delete_file(filename) that deletes a file from the file system.
Your function should adhere to the following requirements:

The function should take one string argument, filename, which is the name of the file to be deleted.
The function should check if the file exists before attempting to delete it.
If the file exists, the function should delete it and return a success message.
If the file does not exist, the function should return an error message "File not found."

Instructions:
Your task is to implement the delete_file function according to the specified requirements. Make sure to handle any possible exceptions and return the appropriate messages or results.
Please test your function with various input scenarios, including valid filenames, and non-existent filenames.

Examples:

Valid Filename:

Input: delete_file("data.txt")
Expected Output: "File deleted successfully."
Explanation: The file sample.txt exists and can be deleted.

Non-Existent Filename:

Input: delete_file("missing.txt")
Expected Output: "File not found."
Explanation: The file missing.txt does not exist.

"""
import os
import unittest


def delete_file(filename):

    if os.path.exists(filename):
        os.remove(filename)
        return "File deleted successfully."
    else:
        return "File not found."


#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####

class TestDeleteFile(unittest.TestCase):
    current_path = os.path.dirname(os.path.abspath(__file__))

    def test_valid_filename(self):
        filename = os.path.join(self.current_path, "data.txt")
        # Create the file first then delete it
        with open(filename, 'w') as f:
            f.write("Test data")
        self.assertEqual(delete_file(filename), "File deleted successfully.")

    def test_non_existent_filename(self):
        filename = os.path.join(self.current_path, "notfound.txt")
        self.assertEqual(delete_file(filename), "File not found.")


if __name__ == '__main__':
    unittest.main()
