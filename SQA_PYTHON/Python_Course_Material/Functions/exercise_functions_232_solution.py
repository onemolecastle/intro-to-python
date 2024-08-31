# Excercise: Word Counter

"""
Count the Occurrence of Words in a String

Write a function called count_words that takes a string as an argument and returns a dictionary
containing the frequency of each word in the string.

The keys of the dictionary should be the words in the string, and the values should be the number
of times each word appears in the string.

The function should ignore case and should not count any punctuation as part of a word.

For example,
    if the string is "The quick brown fox jumps over the lazy dog.", the function should return the following dictionary:
    {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}


"""



def count_words(s):
    words = s.lower().split()
    word_count = {}
    for word in words:
        word = word.strip('.')
        word = word.strip(',')
        word = word.strip('!')
        word = word.strip('?')
        # word = word.strip('.,!?') # or we can do the last 4 lines in just 1 line
        # word = word.strip('.').strip(',').strip('!').strip('?') # also we can do the last 4 lines in just 1 line
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

string = "The quick brown fox jumps over the lazy dog."
word_count = count_words(string)
print(word_count)
