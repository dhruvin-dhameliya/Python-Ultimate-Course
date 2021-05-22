# With Statement:

with open('another.txt', 'r') as f:
    a = f.read()
with open('another.txt', 'w') as f:
    a = f.write("me")
print(a)


# NOTES:

# The best way to open and close the automatically is the with statement.

# --> Dont need to write f.close() as it is done atomatically.