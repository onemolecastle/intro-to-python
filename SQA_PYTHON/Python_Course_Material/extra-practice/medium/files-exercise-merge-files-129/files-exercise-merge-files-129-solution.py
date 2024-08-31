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

import os

def merge_files(output_file, *input_files):
    """
    Merges multiple text files into one output file.
    
    Parameters:
        output_file (str): The name of the file where content will be merged into.
        *input_files (str): Names of the files to be merged.
        
    Returns:
        str: A message indicating the success or failure of the file merge.
    """
    
    # Step 1: Check if all input files exist
    for file in input_files:
        if not os.path.exists(file):
            return f"File not found"
    
    # Step 2: Open the output file for writing
    with open(output_file, 'w') as output:
        
        # Step 3: Go through each input file
        for file in input_files:
            
            # Step 4: Open the input file for reading
            with open(file, 'r') as input:
                
                # Step 5: Write the content of the input file into the output file
                output.write(input.read())
    
    # Step 6: Return a success message
    return "Files merged successfully"

# Example usage:
result = merge_files("output.txt", "file1.txt", "file2.txt")
print(result)  # Should print "Files merged successfully" or "File not found"

#### ANOTHER VESTION THAT IS MORE COMPACT  ####
# def merge_files(output_file, *input_files):
#     if all(os.path.exists(file) for file in input_files):
#         with open(output_file, 'w') as output:
#             for file in input_files:
#                 with open(file, 'r') as input:
#                     output.write(input.read())
#             return "Files merged successfully"
#     else:
#         return "File not found"


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

    # def test_non_existent_filename(self):
    #     input_files = [
    #         os.path.join(self.current_path, "file1.txt"),
    #         os.path.join(self.current_path, "missing.txt"),
    #         os.path.join(self.current_path, "file3.txt")
    #     ]
    #     output_file = os.path.join(self.current_path, "merged.txt")
    #     self.assertEqual(merge_files(output_file, *input_files), "File not found")
    def test_non_existent_filename(self):
        # Define the list of input files and output file
        input_files = [
            os.path.join(self.current_path, "file1.txt"),
            os.path.join(self.current_path, "missing.txt"),
            os.path.join(self.current_path, "file3.txt")
        ]
        output_file = os.path.join(self.current_path, "merged.txt")
        
        # Run the function and check the returned value
        self.assertEqual(merge_files(output_file, *input_files), "File not found")


if __name__ == '__main__':
    unittest.main()
