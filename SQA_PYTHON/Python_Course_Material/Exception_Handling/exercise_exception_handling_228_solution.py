# Exercise 1
# get user locations from list of users V1
# Given list of users, create a new list with locations of the users. if there is a user with no location specified do nothing
users = [{'name': 'Dave', 'occupation': 'engineer', 'location': 'USA'}, {'name': 'Angelina', 'occupation': 'engineer', 'location': 'Mexico'},
        {'name': 'Rose', 'occupation': 'accountant', 'location': 'Nigeria'}, {'name': 'Dave', 'occupation': 'doctor'},
        {'name': 'Divantte', 'occupation': 'engineer', 'location': 'USA'}, {'name': 'Dave', 'occupation': 'engineer', 'location': 'USA'}]

all_locations = []
for user in users:
    try:
        all_locations.append(user['location'])
    except:
        pass
        print("found a user with no location information")
print(all_locations)

###########################################################

# Exercise 2
# get user locations from list of users V2
# Related to the above exercise
# Given list of users, create a new list with locations of the users. Track users with no location in a different list.
# print both lists. (list of locations, and list of users that do not have location information)
users = [{'name': 'Dave', 'occupation': 'engineer', 'location': 'USA'}, {'name': 'Angelina', 'occupation': 'engineer', 'location': 'Mexico'},
        {'name': 'Rose', 'occupation': 'accountant', 'location': 'Nigeria'}, {'name': 'Dave', 'occupation': 'doctor', 'location': 'Brazil'},
        {'name': 'Divantte', 'occupation': 'engineer', 'location': 'USA'}, {'name': 'Dave', 'occupation': 'engineer', 'location': 'USA'}]

all_locations = []
users_missing_location = []
for user in users:
    try:
        all_locations.append(user['location'])
    except:
        users_missing_location.append(user)

print(f"All locations: {all_locations}")
print(f"These users are missing location: {users_missing_location}")

###########################################################

# Exercise 3
# get user locations from list of users V3
# Related to the above exercise
# Given list of users, create a new list with locations of the users. Track users with no location in a different list.
# The list of users with no location should only contain the name of the users
# print both lists. (list of locations, and list of users that do not have location information)
users = [{'name': 'Dave', 'occupation': 'engineer', 'location': 'USA'}, {'name': 'Angelina', 'occupation': 'engineer', 'location': 'Mexico'},
        {'name': 'Rose', 'occupation': 'accountant', 'location': 'Nigeria'}, {'name': 'Dave', 'occupation': 'doctor', 'location': 'Brazil'},
        {'name': 'Divantte', 'occupation': 'engineer', 'location': 'USA'}, {'name': 'Dave', 'occupation': 'engineer', 'location': 'USA'}]

all_locations = []
users_missing_location = []
for user in users:
    try:
        all_locations.append(user['location'])
    except:
        users_missing_location.append(user)

print(f"All locations: {all_locations}")
print(f"These users are missing location: {users_missing_location}")

###########################################################
