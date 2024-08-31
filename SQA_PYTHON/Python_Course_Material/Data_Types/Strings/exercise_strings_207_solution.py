'''
1. Welcome Message
   - Create a variable named `welcome` that holds the string "Diving into Python programming!" and print the variable.
'''
welcome = "Diving into Python programming!"
print(welcome)


'''
2. Dynamic Greeting
   - Define a variable `hero_name` with the name of a superhero. Then, print a message that says, "Welcome to our world, [hero name]!"
'''
hero_name = "Batman"
print(f"Welcome to our world, {hero_name}!")


'''
3. Substring Extraction
   - From the string "Artificial Intelligence", extract and print the word "Intelligence".
'''
phrase = "Artificial Intelligence"
print(phrase.split()[1])


'''
4. Beginning Characters
   - Print the last 5 characters of the string "Developer".
'''
text = "Developer"
print(text[-5:])


'''
5. Title Case Conversion
   - Convert the string "hello world" to title case (where each word begins with a capital letter), then print the result.
'''
greeting = "hello world"
print(greeting.title())


'''
6. Unique Replacements
   - Replace the spaces with underscores in the string "deep learning" and print the updated string.
'''
phrase = "deep learning"
print(phrase.replace(' ', '_'))


'''
7. Dynamic String Formatting
   - Use the `format` method to print the sentence "The Earth revolves around the Sun." by incorporating the words "Earth" and "Sun" from variables.
'''
planet = "Earth"
star = "Sun"
print("The {} revolves around the {}.".format(planet, star))


'''
8. Calculations with f-strings
   - Using an f-string, show the result of 123 divided by 9, ensuring the result is shown with three decimal places.
'''
result = 123 / 9
print(f"{result:.3f}")


'''
9. Counting Sentence Words
   - Use the sentence "Exploration is really the essence of the human spirit" and print the total number of words it contains.
'''
sentence = "Exploration is really the essence of the human spirit"
print(len(sentence.split()))


'''
10. Inverting Words in a Sentence
    - Reverse the order of words in "Exploration is really the essence of the human spirit" so it reads backwards by word.
'''
words = sentence.split()
words.reverse()
print(' '.join(words))


'''
11. Concatenating Strings
    - Create two string variables: `part1` with the value "Python" and `part2` with the value "Rocks!". Concatenate these strings to form and print the complete message "Python Rocks!".
'''
part1 = "Python"
part2 = "Rocks!"
message = part1 + " " + part2
print(message)


'''
12. Building Sentences
    - Given three string variables `subject` ("Learning"), `action` ("enhances"), and `object` ("understanding"), concatenate them to form the complete sentence "Learning enhances understanding." Ensure there are spaces between the words and print the result.
'''
subject = "Learning"
action = "enhances"
object = "understanding"
sentence = subject + " " + action + " " + object + "."
print(sentence)