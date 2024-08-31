'''
1. Create and Print a List of Cities
   - Create a list named `cities` containing "New York", "London", "Tokyo", and "Paris". Print the entire list.
'''
cities = ["New York", "London", "Tokyo", "Paris"]
print(cities)


'''
2. Access the Last Element
   - Print the last city in the `cities` list.
'''
print(cities[-1])


'''
3. Replace the Second City
   - Change "London" in the `cities` list to "Beijing" and print the modified list.
'''
cities[1] = "Beijing"
print(cities)


'''
4. Append a City
   - Add "Sydney" to the `cities` list and print the list.
'''
cities.append("Sydney")
print(cities)


'''
5. Insert a City at the Second Position
   - Insert "Mumbai" at the second position in the `cities` list and print the list.
'''
cities.insert(1, "Mumbai")
print(cities)


'''
6. Remove a City by Value
   - Remove "Tokyo" from the `cities` list and print the list.
'''
cities.remove("Tokyo")
print(cities)


'''
7. Pop the Last City
   - Use the `pop` method to remove and print the last city in the list.
'''
last_city = cities.pop()
print(last_city)


'''
8. Print the New Length of the Cities List
   - Print the number of items in the `cities` list after the removals.
'''
print(len(cities))


'''
9. Create a List of Squares Using `range()`
    - Create a list of squares for the numbers 6 through 10 and print the list.
'''
squares = [number ** 2 for number in range(6, 11)]
print(squares)


'''
10. Print a Slice of the Cities List
    - Print the middle two cities from the `cities` list.
'''
# Assuming a populated list; adjust based on current content
middle_cities = cities[1:3]  # This will depend on the current size of the list
print(middle_cities)


'''
11. Reverse and Print the Cities List
    - Reverse the `cities` list and print it.
'''
cities_reversed = cities[::-1]
print(cities_reversed)


'''
12. Sort the Cities List Alphabetically and Print It
    - Sort the `cities` list in alphabetical order and print the list.
'''
cities_sorted = sorted(cities)
print(cities_sorted)


'''
13. Copy the Cities List and Print the Copy
    - Make a copy of the `cities` list named `cities_copy` and print the copy.
'''
cities_copy = cities[:]
print(cities_copy)


'''
14. Combine Two New Lists into the Cities List
    - Create two new lists, `additional_cities` and `more_cities`, each with at least one city. Extend `cities` with these lists and print the updated list.
'''
additional_cities = ["Dublin"]
more_cities = ["Cairo"]
# Assuming cities list is re-populated as the previous clear would have emptied it
cities.extend(additional_cities + more_cities)
print(cities)


'''
15. Clear the Cities List and Print It
    - Clear the `cities` list and print the now empty list.
'''
cities.clear()
print(cities)
