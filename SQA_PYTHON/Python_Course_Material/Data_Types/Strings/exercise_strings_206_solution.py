'''
1. Create and Display a Message
   - Create a variable named `announcement` that holds the string "Welcome to the world of Python!" and print the variable.
'''
announcement = "Welcome to the world of Python!"
print(announcement)


'''
2. Greeting with a Twist
   - Define a variable `your_name` with the name of a fictional character. Print a greeting that says "Greetings, [character name]! Welcome to Python."
'''
your_name = "Alice"
print(f"Greetings, {your_name}! Welcome to Python.")


'''
3. Extracting Words
   - Given the string "Machine Learning", extract and print the word "Learning".
'''
phrase = "Machine Learning"
print(phrase.split()[1])


'''
4. Accessing Ending Characters
   - Print the first 4 characters of the string "Programming".
'''
word = "Programming"
print(word[:4])

'''
5. Making Everything Lowercase
   - Take the string "PYTHON" and convert it to lowercase, then print the result.
'''
word_upper = "PYTHON"
print(word_upper.lower())


'''
6. Creative Replacements
   - In the string "machine learning", replace all instances of the letter "e" with "3" and print the new string.
'''
sentence = "machine learning"
print(sentence.replace('e', '3'))


'''
7. Formatting with Variables
   - Using the `format` method, print the sentence "There are 7 continents and 5 oceans on Earth." using variables for numbers.
'''
continents = 7
oceans = 5
print("There are {} continents and {} oceans on Earth.".format(continents, oceans))


'''
8. Precision with f-strings
   - Print the result of multiplying 7 by 4.5, using an f-string to format the number to one decimal place.
'''
result = 7 * 4.5
print(f"{result:.1f}")


'''
9. Sentence Word Counter
   - Assign the sentence "A journey of a thousand miles begins with a single step" to a variable. Then, print how many words are in this sentence.
'''
journey_sentence = "A journey of a thousand miles begins with a single step"
print(len(journey_sentence.split()))


'''
10. Word Order Reversal
    - Take the sentence from the previous exercise and print it with the words in reverse order (e.g., "step single a with begins miles thousand a of journey A").
'''
words = journey_sentence.split()
words.reverse()
reversed_sentence = ' '.join(words)
print(reversed_sentence)