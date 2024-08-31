"""
Exercise: Grade Calculator (id=205)

Requirements:

You are tasked with creating a grade calculator function that calculates the final grade of a student based on their scores in various assessments. The assessments include homework, quizzes, and exams, each with its weight in the final grade calculation.

Function Name: calculate_final_grade(homework, quizzes, exams)

Parameters:
- homework (float): The average score of homework assignments (0-100).
- quizzes (float): The average score of quizzes (0-100).
- exams (float): The average score of exams (0-100).

Return Value:
- A string representing the final letter grade based on the weighted averages.

Grading Criteria:
- Homework contributes 20% to the final grade.
- Quizzes contribute 30% to the final grade.
- Exams contribute 50% to the final grade.

Example of how to calculate the grade:
 weighted_average = (homework * 0.2) + (quizzes * 0.3) + (exams * 0.5)

Use the following grading scale:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: 0-59

Examples:

Here's an example of how the program should work:

# Calculate the final grade
final_grade = calculate_final_grade(85.5, 75.0, 92.0)

# The 'final_grade' variable should contain the following:
"Grade: B"

Instructions:

1. Implement the `calculate_final_grade` function according to the specified requirements. Calculate the weighted average of homework, quizzes, and exams.
2. Use the grading scale to determine the final letter grade based on the calculated average.
3. Return the final grade as a string in the format "Grade: X" where X is the letter grade.

"""

def calculate_final_grade(homework, quizzes, exams):
    # Calculate the weighted average
    weighted_average = (homework * 0.2) + (quizzes * 0.3) + (exams * 0.5)
    
    # Determine the letter grade
    if 90 <= weighted_average <= 100:
        return "Grade: A"
    elif 80 <= weighted_average < 90:
        return "Grade: B"
    elif 70 <= weighted_average < 80:
        return "Grade: C"
    elif 60 <= weighted_average < 70:
        return "Grade: D"
    else:
        return "Grade: F"



#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####

import unittest

class TestGradeCalculator(unittest.TestCase):

    def test_grade_A(self):
        """
        Test for a final grade of A.
        """
        self.assertEqual(calculate_final_grade(90.0, 90.0, 90.0), "Grade: A")

    def test_grade_B(self):
        """
        Test for a final grade of B.
        """
        self.assertEqual(calculate_final_grade(80.0, 75.0, 85.0), "Grade: B")

    def test_grade_C(self):
        """
        Test for a final grade of C.
        """
        self.assertEqual(calculate_final_grade(70.0, 68.0, 75.0), "Grade: C")

    def test_grade_D(self):
        """
        Test for a final grade of D.
        """
        self.assertEqual(calculate_final_grade(62.5, 58.0, 65.0), "Grade: D")

    def test_grade_F(self):
        """
        Test for a final grade of F.
        """
        self.assertEqual(calculate_final_grade(55.0, 48.0, 50.0), "Grade: F")

if __name__ == "__main__":
    unittest.main()
