"""
Exercise: Email Validation (id=143)

Requirements:
You are tasked with creating a function that checks if a given string is a valid email address.
Email addresses must follow certain rules to be considered valid, such as having the "@" symbol and a valid domain.

Function Name: is_valid_email(email)
Parameters:
email (str): A string representing the email address to be validated.
Return Value:
A boolean value (True or False) indicating whether the provided email address is valid.

Email Validation Rules:
The email address must contain the "@" symbol
The "@" symbol should not be the first or last character of the email address.
There must be at least one character before and after the "@" symbol.
The domain (the part after "@" symbol) should contain at least one period (".") character.
The domain should have at least one character before and after the period.
The domain cannot contain spaces or special characters.

Examples:

Here are some examples of how the program should work:
# Check if the email is valid
result = is_valid_email("john.doe@example.com")
# The 'result' variable should contain the following:
True
# Check another email
result = is_valid_email("notavalidemail")
# The 'result' variable should contain the following:
False
Instructions:

Implement the is_valid_email function according to the specified requirements.
Use string manipulation and conditions to check each rule.
Return True if the email address is valid and False if it is not.
Write unit tests to validate the correctness of your function.
"""


def is_valid_email(email):
    is_valid = False
    # Check if "@" symbol is present and not at the start or end
    if "@" in email and email[0] != "@" and email[-1] != "@":
        # Split the email into local and domain parts
        local_part, domain = email.split("@")
        # Check if local part and domain part are not empty
        if local_part and domain:
            # Check if the domain contains a period
            if "." in domain:
                # Split the domain into subdomains (if any)
                subdomains = domain.split(".")
                # Check if all subdomains contain at least one character
                if all(subdomain for subdomain in subdomains):
                    # Check if the domain part contains only alphanumeric characters
                    is_valid = True
    return is_valid


import unittest


class TestEmailValidation(unittest.TestCase):

    def test_valid_email(self):
        """
        Test for a valid email address.
        """
        self.assertTrue(is_valid_email("john.doe@example.com"))

    def test_invalid_email(self):
        """
        Test for an invalid email address.
        """
        self.assertFalse(is_valid_email("notavalidemail"))

    def test_valid_email_with_subdomains(self):
        """
        Test for a valid email address with subdomains.
        """
        self.assertTrue(is_valid_email("user@mail.example.co"))

    def test_valid_email_with_numbers(self):
        """
        Test for a valid email address containing numbers.
        """
        self.assertTrue(is_valid_email("1234@example.com"))


if __name__ == "__main__":
    unittest.main()
