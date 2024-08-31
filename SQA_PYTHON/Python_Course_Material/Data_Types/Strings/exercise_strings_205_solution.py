'''
1. Create and Print a String
   - Create a variable named `greeting` that holds the string "Hello, Python learners!" and print the variable.
'''
greeting = "Hello, Python learners!"
print(greeting)


'''
2. Personalized Greeting
   - Define a variable `name` with your name as its value. Then, print a personalized greeting using this name.
'''
name = "Your Name"
print(f"Hello, {name}!")


'''
3. String Slicing to Extract Substring
   - Given the string "Data Science", extract and print the substring "Data".
'''
text = "Data Science"
print(text[:4])


'''
4. Print the Last Characters
   - Print the last 3 characters of the string "Python".
'''
word = "Python"
print(word[-3:])


'''
5. Convert to Uppercase
   - Convert the string "python" to uppercase and print the result.
'''
word = "python"
print(word.upper())


'''
6. Replace Characters in String
   - Replace all instances of the letter "a" with "@" in the string "data analyst" and print the modified string.
'''
phrase = "data analyst"
print(phrase.replace('a', '@'))


'''
7. String Formatting with `format` Method
   - Using the `format` method, print the sentence "I have 3 apples and 4 bananas." by passing the numbers as variables.
'''
apples = 3
bananas = 4
print("I have {} apples and {} bananas.".format(apples, bananas))


'''
8. String Formatting with f-string
   - Using an f-string, display the result of dividing 10 by 3, formatted to two decimal places.
'''
print(f"{10 / 3:.2f}")


'''
9. Count Words in a Sentence
   - Create a string variable with the sentence "The quick brown fox jumps over the lazy dog". Write a program that prints the number of words in the sentence.
'''
sentence = "The quick brown fox jumps over the lazy dog"
print(len(sentence.split()))


'''
10. Reverse Word Order
    - Using the sentence from the previous challenge, print the sentence with the order of the words reversed (e.g., "dog lazy the over jumps fox brown quick The").
'''
words = sentence.split()
words.reverse()
print(' '.join(words))
