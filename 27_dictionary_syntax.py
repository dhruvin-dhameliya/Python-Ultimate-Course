# Always can be change the Dictionary.

myDict = {
    "fast": "In a Quick Manner",
    "dhruvin": "A Coder",
    "marks": [10, 25, 40, 37, 48]
}

print(myDict['fast'])
print(myDict['dhruvin'])

myDict['marks'] = [1, 2, 3] # Change the Dictionary in Marks key .
print(myDict['marks'])

# Nested Dictionary.
myDict = {
    "fast": "In a Quick Manner",
    "dhruvin": "A Coder",
    "marks": [10, 25, 40, 37, 48],
    "another_dict": {'dhruvin': 'Student'} # Inner Dictionary 
}

print(myDict['another_dict'])
print(myDict['another_dict']['Dhruvin'])