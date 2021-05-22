myDict = {
    "Pankha": "Fan",
    "Vastu": "Item",
    "Kitab": "Book",
    "Dabba": "Box",
    "Kagaj": "Page"
}

print("Option are ", myDict.keys())

a = input("Enter the Hindi Word \n")
# print("The meaning of your word is:", myDict[a])  # Some time throw error

# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))
