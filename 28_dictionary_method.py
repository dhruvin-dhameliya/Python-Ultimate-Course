myDict = {
    "fast": "In a Quick Manner",
    "dhruvin": "A Coder",
    "marks": [10, 25, 40, 37, 48],
    "another_dict": {'dhruvin': 'Student'}, # Inner Dictionary 
    1: 2
}

# Dictionary Methods
print(myDict.keys()) # Print the all key of the dictionary

print("-------------------------------------------------------------------------------------------------------------------------------")

print(type(myDict.keys())) # Type of Dictionary 

print("-------------------------------------------------------------------------------------------------------------------------------")

# List type casting
print(list(myDict.keys())) # Print the all key of the dictionary in list form 

print("-------------------------------------------------------------------------------------------------------------------------------")

print(myDict.values()) # Print the all values of the dictionary

print("-------------------------------------------------------------------------------------------------------------------------------")

print(myDict.items()) # Print the (key, value) for all contents of the dictionary

print("-------------------------------------------------------------------------------------------------------------------------------")

print(myDict)

updateDict = {
    "Python": "Language",
    "C": "Frist Language",
    "HTML": "Using Language the create website",
    "dhruvin": "A Student"
}
# Update Dictionary in use update function  
myDict.update(updateDict) # Update the dictionary by adding key-vaalue pairs from updateDict
print(myDict)

print(myDict.get("dhruvin")) # Print the value associated with key "dhruvin"
print(myDict["dhruvin"]) # Print the value associated with key "dhruvin"

# The difference between .get and [] syntex in Dictionary 
print(myDict.get("dhruvin2")) # Return  --> None --> as dhruvin2 is not present in the dictionary 
print(myDict["dhruvin2"]) # Throw an --> Error --> as dhruvin2 is not present in the dictionary 