# All the exercises below are based on this data

university = {
    "name": "Global Tech University",
    "address": {
        "street": "100 Innovation Drive",
        "city": "Techville",
        "state": "Future",
        "zip": "12345"
    },
    "departments": ["Engineering", "Computer Science", "Arts", "Business"],
    "courses": [
        {"code": "CS101", "name": "Intro to Computer Science", "credits": 4},
        {"code": "ENG204", "name": "Advanced Engineering Mathematics", "credits": 3},
        {"code": "BUS301", "name": "Principles of Management", "credits": 3},
        {"code": "ART105", "name": "Modern Art Concepts", "credits": 2}
    ],
    "contact": {
        "phone": "123-456-7890",
        "email": "info@globaltechu.edu",
        "fax": "123-456-7891"
    }
}


# 1. Print the University's Name
print(university["name"])

# 2. Get the Number of Departments
print(len(university["departments"]))

# 3. Access the City of the University
print(university["address"]["city"])

# 4. Print the First Course Name
print(university["courses"][0]["name"])

# 5. Find the Total Credits for 'CS101' Course
# Directly access assuming 'CS101' is the first course
print(university["courses"][0]["credits"])

# 6. Extract and Print the ZIP Code
print(university["address"]["zip"])

# 7. Print the Contact Email
print(university["contact"]["email"])

# 8. Split the University's Street Address
# Splitting and printing the first item as an example
print(university["address"]["street"].split()[0])

# 9. Print the Fax Number
print(university["contact"]["fax"])

# 10. Print the Second Department
# Directly accessing the second department assuming departments are static
print(university["departments"][1])

# 11. Print the State Where the University Is Located
print(university["address"]["state"])

# 12. Print the Email Domain of the University Contact Email
# Extracting the domain part after "@" from the email string
print(university["contact"]["email"].split('@')[1])

# 13. Print the Number of Credits for the Last Course in the List
# Directly accessing the last course assuming a static list of courses
print(university["courses"][-1]["credits"])

# 14. Print the Zip Code Length as a String
# Getting the length of the zip code string
print(len(university["address"]["zip"]))

# 15. Print How Many Subjects Are Offered
# Directly accessing the number of items in the 'departments' list
print(len(university["departments"]))
