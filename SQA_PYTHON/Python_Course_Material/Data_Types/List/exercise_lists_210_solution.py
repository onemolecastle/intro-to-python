'''
1. Create and Print a List of Programming Languages
   - Create a list named `languages` containing "Python", "Java", "C++", and "JavaScript". Print the entire list.
'''
languages = ["Python", "Java", "C++", "JavaScript"]
print(languages)


'''
2. Access the Second-to-Last Element
   - Print the second-to-last language in the `languages` list.
'''
print(languages[-2])


'''
3. Modify the Last Language
   - Change the last language in the `languages` list to "Ruby" and print the modified list.
'''
languages[-1] = "Ruby"
print(languages)


'''
4. Prepend a Language
   - Add "Go" to the beginning of the `languages` list and print the list.
'''
languages.insert(0, "Go")
print(languages)


'''
5. Remove the Third Language by Index
   - Remove the third language in the `languages` list by its index and print the list.
'''
del languages[2]
print(languages)


'''
6. Duplicate a Language
   - Add another "Python" to the `languages` list and print the list.
'''
languages.append("Python")
print(languages)


'''
7. Find the Index of "Java"
   - Find and print the index of "Java" in the `languages` list.
'''
print(languages.index("Java"))


'''
8. Count the Occurrence of "Python"
   - Count and print the number of times "Python" appears in the `languages` list.
'''
print(languages.count("Python"))


'''
9. Reverse the List Order Without Modifying the Original List
   - Print the `languages` list in reverse order without altering the original list.
'''
print(languages[::-1])


'''
10. Alphabetically Sort the List Without Modifying the Original
    - Print the `languages` list in alphabetical order without changing the original list.
'''
print(sorted(languages))


'''
11. Create and Print a Nested List
    - Create a nested list named `tech_stack` that contains the `languages` list and a new list of databases: ["MySQL", "PostgreSQL", "MongoDB"]. Print `tech_stack`.
'''
tech_stack = [languages, ["MySQL", "PostgreSQL", "MongoDB"]]
print(tech_stack)


'''
12. Access and Print a Database from the Nested List
    - Print the first database from the nested `tech_stack` list.
'''
print(tech_stack[1][0])


'''
13. Combine Two Lists Without Duplicates
    - Create a new list named `more_languages` with "Swift" and "Python". Combine it with `languages` to create a new list `combined_languages` that doesn't contain duplicates. Print `combined_languages`.
'''
more_languages = ["Swift", "Python"]
combined_languages = list(set(languages + more_languages))
print(combined_languages)


'''
14. Remove All Elements and Verify the List is Empty
    - Clear the `languages` list. Then, print True if the list is empty, or False otherwise.
'''
languages.clear()
print(languages == [])
