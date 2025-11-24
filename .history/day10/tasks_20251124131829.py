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

def pangram(text):
    alphabet = set(string.ascii_lowercase)
    text = text.lower()
    
    letters_in_text = set()

    for char in text:
        if char.isalpha():         
            letters_in_text.add(char)

    return alphabet.issubset(letters_in_text)


sentence = "My name is Madueke Gerald Chinememrem"

if is_pangram(sentence):
    print(f'"{sentence}" is a pangram.')
else:
    print(f'"{sentence}" is NOT a pangram.')
    
    
    
# TASK 2
def get_even_numbers(numbers):
    evens = []
    
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    
    return evens

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = get_even_numbers(sample_list)

print("Even numbers:", result)

    
