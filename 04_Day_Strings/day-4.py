# Creating a String
print("Creating a String"+"-"*50)
letter = "P"
print(letter)
print(len(letter))
multiple_string = '''I am a teacher and I love love to inspire and teach people.
How are you?'''
print(multiple_string)
print(multiple_string.upper())
print(multiple_string.lower())
print(multiple_string.capitalize())
print(multiple_string.count("I"))
print(multiple_string.find("love"))
print(multiple_string.replace("love", "enjoy"))
# Escape Sequences in Strings
print("\n\nEscape Sequences in Strings"+"-"*50)
# In Python and other programming languages \ followed by a character is an escape sequence. Let us see the most common escape characters:

# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# New Style String Formatting (str.format)
# This formatting is introduced in Python version 3.
print("\n\nNew Style String Formatting (str.format)"+"-"*50)
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
# String Interpolation / f-Strings (Python 3.6+)
print("\n\nString Interpolation / f-Strings (Python 3.6+)"+"-"*50)
# Another new string formatting is string interpolation, f-strings. Strings start with f and we can inject the data in their corresponding positions.
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Python Strings as Sequences of Characters
# Python strings are sequences of characters, and share their basic methods of access 
# with other Python ordered sequences of objects – lists and tuples. 
# The simplest way of extracting single characters from strings (and individual members from any sequence) is to unpack them into corresponding variables.
print("\n\nPython Strings as Sequences of Characters"+"-"*50)
print("Unpacking Characters")
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
print("Accessing Characters in Strings by Index")
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o
print("Reversing a String")
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH
print("Skipping Characters While Slicing")
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto