'''
1. Create and Print a Dictionary
   - Create a dictionary named `person` with keys `name` and `age`, and values "John Doe" and 30, respectively. Print the dictionary.
'''
person = {"name": "John Doe", "age": 30}
print(person)


'''
2. Accessing Dictionary Values
   - Print the value associated with the key `name` from the `person` dictionary.
'''
print(person["name"])


'''
3. Adding a New Key-Value Pair
   - Add a new key-value pair `location` with the value "New York" to the `person` dictionary. Print the updated dictionary.
'''
person["location"] = "New York"
print(person)


'''
4. Modifying a Value in the Dictionary
   - Change the `age` in the `person` dictionary to 31. Print the updated dictionary.
'''
person["age"] = 31
print(person)


'''
5. Removing a Key-Value Pair
   - Remove the key `location` from the `person` dictionary. Print the updated dictionary.
'''
del person["location"]
print(person)


'''
6. Using the get() Method
   - Use the `get()` method to print the value of `age` from the `person` dictionary. If `age` doesn't exist, print "Age not found".
'''
print(person.get("age", "Age not found"))


'''
7. Keys, Values, and Items
   - Print all keys in the `person` dictionary using the `.keys()` method.
   - Print all values in the `person` dictionary using the `.values()` method.
   - Print all key-value pairs in the `person` dictionary as tuples using the `.items()` method.
'''
print(person.keys())
print(person.values())
print(person.items())


'''
8. Checking if a Key Exists
   - Check if the key `name` exists in the `person` dictionary and print True if it does, otherwise False.
'''
print("name" in person)


'''
9. Copying a Dictionary
   - Create a copy of the `person` dictionary named `person_copy` using the `.copy()` method. Print `person_copy`.
'''
person_copy = person.copy()
print(person_copy)


'''
10. Clearing a Dictionary
    - Clear all contents from the `person` dictionary using the `.clear()` method and print the now empty dictionary.
'''
person.clear()
print(person)
