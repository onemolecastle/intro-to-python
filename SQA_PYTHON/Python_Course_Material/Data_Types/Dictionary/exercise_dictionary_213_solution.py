'''
1. Nested Dictionaries
   - Create a dictionary `employee` that includes the keys `name`, `department`, and `skills`. `skills` should be a nested dictionary with keys `technical` and `soft`, each holding a list of skills. Fill in some sample skills. Print the dictionary.
'''
employee = {
    "name": "Jane Doe",
    "department": "IT",
    "skills": {
        "technical": ["Python", "SQL"],
        "soft": ["communication", "teamwork"]
    }
}
print(employee)


'''
2. Accessing Nested Data
   - Use the dictionary from the previous exercise. Print the list of `technical` skills from the `employee` dictionary.
'''
print(employee["skills"]["technical"])


'''
3. Adding to a List in a Nested Dictionary
   - Add a new `technical` skill "JavaScript" to the `employee` skills. Print the updated list of `technical` skills.
'''
employee["skills"]["technical"].append("JavaScript")
print(employee["skills"]["technical"])


'''
4. Modifying Nested Dictionary Data
   - Change the `department` value to "Development". Print the updated `employee` dictionary.
'''
employee["department"] = "Development"
print(employee)


'''
5. Using get() on a Nested Dictionary
   - Use the `.get()` method to retrieve the `soft` skills from `employee`. If `soft` doesn't exist, print "Soft skills not found".
'''
print(employee["skills"].get("soft", "Soft skills not found"))


'''
6. Safe Accessing of Nested Data
   - Attempt to print the `management` skills from `employee`, using `.get()` to avoid errors if the key doesn't exist. Use "Management skills not found" as the default value.
'''
print(employee["skills"].get("management", "Management skills not found"))


'''
7. Dictionary from Keys and Default Value
   - Use the `fromkeys()` method to create a new dictionary `defaults` with keys from a list `['a', 'b', 'c']` and a default value of `None`. Print `defaults`.
'''
defaults = dict.fromkeys(['a', 'b', 'c'], None)
print(defaults)


'''
8. Removing an Item by Key and Getting Its Value
   - Remove the key `department` from `employee` and print its value. If `department` doesn't exist, use "Department not found" as the default message.
'''
print(employee.pop("department", "Department not found"))


'''
9. Updating Dictionary with New Keys and Values
   - Create a new dictionary `new_info` with keys `project` and `status`, and values "Website Development" and "In Progress", respectively. Update the `employee` dictionary with this new information and print the updated dictionary.
'''
new_info = {"project": "Website Development", "status": "In Progress"}
employee.update(new_info)
print(employee)


'''
10. Clearing Nested Dictionary Contents
    - Clear the contents of the `skills` nested dictionary within the `employee` dictionary. Print the now empty `skills` dictionary.
'''
employee["skills"].clear()
print(employee["skills"])
