"""
Exercise: Password Validator and Strength Checker (id=201)

* Tests for the function are included. Run this script to test your function.
* To just try your function without running the tests, uncomment your function from the "if __name__ = '__main__':" block.

Requirements:

You are developing a Python function for password validation and strength checking. Your function should check if a given password meets specific criteria and return its strength level.

Criteria for a valid password:
1. The password must be at least 8 characters long.
2. The password must contain at least one uppercase letter.
3. The password must contain at least one lowercase letter.
4. The password must contain at least one digit.
5. The password must contain at least one special character from the set: !@#$%^&*()-_+=[]{}|;:'\",.<>?/

Strength Levels:
- Weak: Meets only one of the criteria or the length is under 8 characters.
- Moderate: Meets three of the criteria.
- Strong: Meets four criteria.
- Very Strong: Meets all five criteria.

Function Name: check_password_strength(password)

Parameters:
- password (str): The password to validate and check its strength.

Your function should return one of the following strings based on the password's strength level: "Weak," "Moderate," "Strong," or "Very Strong."


Instructions:

1. Implement the `check_password_strength` function according to the specified requirements.
2. Use loops and if-else statements to check each criterion for the password.
3. Determine the strength level based on how many criteria are met and return the corresponding string.
4. Make sure to handle exceptions gracefully and return "Invalid input" if the input is not a string.

Examples:

Here are some examples to illustrate the expected behavior of your function:

Weak Password:
Input: check_password_strength("password")
Expected Output: "Weak"

Moderate Password:
Input: check_password_strength("P@ssword")
Expected Output: "Moderate"

Strong Password:
Input: check_password_strength("Str0ng#Pwd")
Expected Output: "Strong"

Very Strong Password:
Input: check_password_strength("V3ry#Str0ng&Pwd")
Expected Output: "Very Strong"

Invalid Input (Non-String):
Input: check_password_strength(123456)
Expected Output: "Invalid input"

"""

#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####
import unittest

def check_password_strength(password):
    try:
        if not isinstance(password, str):
            return "Invalid input"
        
        has_length = False
        has_uppercase = False
        has_lowercase = False
        has_digit = False
        has_special = False

        for char in password:
            if char.isupper():
                has_uppercase = True
            if char.islower():
                has_lowercase = True
            if char.isdigit():
                has_digit = True
            if char in "!@#$%^&*()-_+=[]{}|;:'\",.<>?/":
                has_special = True
        
        # Check if the password is at least 8 characters long
        if len(password) < 8:
            return "Weak"
        else:
            has_length = True

        conditions = [has_length, has_uppercase, has_lowercase, has_digit, has_special]
        meet_conditions = [i for i in conditions if i == True]

        # Check if the criteria are met
        if len(meet_conditions) == 5:
            return "Very Strong"
        elif len(meet_conditions) == 4:
            return "Strong"
        elif len(meet_conditions) == 3:
            return "Moderate"
        else:
            return "Weak"
        
    except Exception:
        return "Invalid input"

# Unit tests
class TestPasswordStrengthChecker(unittest.TestCase):

    def test_weak_password(self):
        self.assertEqual(check_password_strength("password"), "Weak")

    def test_moderate_password(self):
        self.assertEqual(check_password_strength("p@ssword"), "Moderate")

    def test_strong_password(self):
        self.assertEqual(check_password_strength("str0ng#pwd"), "Strong")

    def test_very_strong_password(self):
        self.assertEqual(check_password_strength("V3ry#Str0ng&Pwd"), "Very Strong")

    def test_non_string_input(self):
        self.assertEqual(check_password_strength(123456), "Invalid input")

if __name__ == "__main__":
    unittest.main()

    # check_password_strength()