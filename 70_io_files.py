# Use open function to read the content of a file !

f = open('sample.txt', 'r')
f = open('sample.txt')   # By default the mode is r 
data = f.read()

# data = f.read(7)   # Read the frist 7 character from the file

print(data)
f.close()
