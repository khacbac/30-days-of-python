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
