# Exercise 1
# Create a function to calculate area of a circle given radius of circle. function should return the area
# this I actually use on interviews
# area of a circle is PI * r^2
# There are at least two ways you can do it

def calculate_area_of_circle_v1(radius):
    PI = 3.142
    Area =  PI  * (radius**2)
    return Area
area = calculate_area_of_circle_v1(10)
print(area)


def calculate_area_of_circle_v2(radius):
    radius_square = (radius**2)
    PI = 3.142
    Area = radius_square * PI
    return Area
area = calculate_area_of_circle_v2(10)
print(area)
# # Test data
# radius = 4
# area = ??
#
# radius = 10
# area = ??
#
# radius = "15"
# area = ??
#

########################################

# Exercise 2
# Define a function that takes in social security number as parameter (formated XXX-XX-XXXX) and return the last for digits
# Example if input is 1234-56-7890, the the function will return 7890
# def get_last_4_digit_of_ssn_v1():
#     ssn = input("Please enter your ssn here: ")
#     formated_ssn = (ssn[-1:-4])
#     print(formated_ssn)
#     return formated_ssn

# ssn_secret = get_last_4_digit_of_ssn_v1()
# print(ssn_secret)



# Exercise 2 - Continuation
# Define a function that takes in social security number as parameter (formated XXX-XX-XXXX) and return the last for digits
# Validate the input data matches the format expected. If not raise an exception.
def get_last_4_digit_of_ssn_v1():
    ssn = input("Please enter your ssn here: ")
    strip_ssn = ssn.split("-")
    if len(strip_ssn[0]) != 3 or len(strip_ssn[1]) != 2 or len(strip_ssn[2]) != 4:
        print("invalid number")
        print("please enter a number with this format: XXX-XX-XXXX")
    else:
            formated_ssn = strip_ssn[2]
            return formated_ssn
secret_ssn = get_last_4_digit_of_ssn_v1()
print(secret_ssn)

##########################################################################
# Exercise 3
# Note: similar to the ssn ex so if ssn is solved in class then this can be homework
# define a functiont that takes in a birthday and return the year of the birthday
# verify the year of the birthday is 4 digits if not raise error
# It should accept format mm/dd/yyyy or mm-dd-yyyy

def get_year_of_bday(bday):
    pass


##########################################################################
# Exercise 4
# define a function that will take a list of employees and filter employees with salaries over given amount.
# Returns a list of employees that have salaries above the provided amount.
# Each employee data is a dictionary with employee info including salary.
# The Minimum salary amount (to be filtered by) is a parameter to the function.
# Example input/output:
employees = [
    {"name": "John", "salary": 50000},
    {"name": "Bob", "salary": 35000},
    {"name": "Mary", "salary": 49000},
    {"name": "Jose", "salary": 76000},
    {"name": "Ivan", "salary": 150000},
             ]
# output if above sample data was provided with the minimum amount 50000
# example_output = [{'name': 'Jose', 'salary': 76000}, {'name': 'Ivan', 'salary': 150000}]

def filter_by_salary(list_of_employees, min_salary):
    pass

my_list = filter_by_salary(employees, 50000)
print(my_list)
my_list = filter_by_salary(employees, 100000)
print(my_list)

##########################################################################
# Exercise 5 
# Define a function that takes in a list of users full names and return a list with only first name.

example_input = ["Admas Kinfu", "Michel Jordan", "Kobe Briant", "Derek Car", "Tom Brady"]
example_output = ['Admas', 'Michel', 'Kobe', 'Derek', 'Tom']

def get_first_names_v1(full_name_list):
    pass

def get_first_names_v2(full_name_list):
    pass

my_list = get_first_names_v1(example_input)
print(my_list)

my_list = get_first_names_v1(example_input)
print(my_list)

#.................................................................................
#.................................................................................


