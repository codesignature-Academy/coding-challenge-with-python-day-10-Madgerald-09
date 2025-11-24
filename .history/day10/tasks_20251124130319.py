"""
Task 1 === Check if a String is a Pangram

Write a Python function to check whether a string is a pangram or not.

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

Task 2 === Print Even Numbers from a Given List

Write a Python program to print the even numbers from a given list.

Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]

"""



# TASK 1
import string

def is_pangram(text):
    alphabet = set(string.ascii_lowercase)
    text = text.lower()
    
    letters_in_text = set()

    for char in text:
        if char.isalpha():          # count only letters
            letters_in_text.add(char)

    return alphabet.issubset(letters_in_text)


sentence = "The quick brown fox jumps over the lazy dog"

if is_pangram(sentence):
    print(f'"{sentence}" is a pangram.')
else:
    print(f'"{sentence}" is NOT a pangram.')
    
    
    
    ?
