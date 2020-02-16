import re
import string


#
# This code is an example ripped from w3resource, so props to them
# https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php
#
# I'm going to take it and pass it the whole file which is about 50% of the work for this part
#
def word_count(str, counts):
    words = str.split()

    for word in words:
        word = standardize(word)
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
# end w3resource code

# returns a lowercase version of the input without special characters
def standardize(word):
    word = word.lower()
    word = re.sub('[^a-zA-Z0-9-_.]', '', word)
    # TODO: turn abbreviations into the full english word

    return word
