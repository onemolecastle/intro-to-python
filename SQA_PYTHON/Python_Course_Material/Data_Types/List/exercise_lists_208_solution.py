'''
1. Create and Print a List
   - Create a list named `colors` containing "red", "blue", and "green". Print the entire list.
'''
colors = ["red", "blue", "green"]
print(colors)


'''
2. Accessing Elements
   - Print the first item from the `colors` list.
'''
print(colors[0])


'''
3. Modifying Elements
   - Change the second item in the `colors` list to "yellow" and print the modified list.
'''
colors[1] = "yellow"
print(colors)


'''
4. Adding Elements
   - Add "orange" to the end of the `colors` list and print the list.
'''
colors.append("orange")
print(colors)


'''
5. Inserting Elements
   - Insert "purple" at the beginning of the `colors` list and print the list.
'''
colors.insert(0, "purple")
print(colors)


'''
6. Removing Elements by Value
   - Remove "blue" from the `colors` list and print the list.
'''
colors.remove("blue")  # Assuming "blue" hasn't been replaced earlier.
print(colors)


'''
7. Removing Elements by Index
   - Remove the first item of the `colors` list using its index and print the list.
'''
del colors[0]
print(colors)


'''
8. List Length
   - Print the number of items in the `colors` list.
'''
print(len(colors))


'''
9. Making Numerical Lists
    - Create a list of numbers from 1 to 5 using the `range()` function and print the list.
'''
numbers = list(range(1, 6))
print(numbers)


'''
10. Slicing Lists
    - Create a list named `numbers` with values from 1 to 10. Print the first 5 numbers using slicing.
'''
numbers = list(range(1, 11))
print(numbers[:5])


'''
11. List Comprehensions
    - Use a list comprehension to create a list of squares for the numbers 1 through 5 and print the list.
'''
squares = [number ** 2 for number in range(1, 6)]
print(squares)


'''
12. Copying a List
    - Create a copy of the `colors` list named `colors_copy` and print it.
'''
colors_copy = colors[:]
print(colors_copy)


'''
13. Joining Lists
    - Create another list named `more_colors` with two colors. Add the contents of `more_colors` to `colors` and print the updated `colors` list.
'''
more_colors = ["black", "white"]
colors.extend(more_colors)
print(colors)


'''
14. Finding the Index of an Element
    - Find and print the index of "green" in the `colors` list.
'''
print(colors.index("green"))


'''
15. Counting Occurrences
    - Add another "green" to the `colors` list. Count and print the number of times "green" appears in the list.
'''
colors.append("green")
print(colors.count("green"))


'''
16. Sorting Lists
    - Sort the `colors` list alphabetically and print the sorted list.
'''
colors.sort()
print(colors)


'''
17. Reversing Lists
    - Reverse the order of the `colors` list and print the reversed list.
'''
colors.reverse()
print(colors)


'''
18. Removing All Elements
    - Remove all items from the `colors` list and print the empty list.
'''
colors.clear()
print(colors)