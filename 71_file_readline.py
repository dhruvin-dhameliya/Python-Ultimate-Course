from os import linesep


f = open('sample.txt')
# read frist line
data = f.readline()
print(data)

# read second line
data = f.readline()
print(data)

# read third line
data = f.readline()
print(data)

# read fourth line... and so on...
data = f.readline()
print(data)

f.close()


# Modes of opening a file :

# r  =  open for reading
# w  =  open for writing
# a  =  open for appending (Last in add the line.)
# +  =  open for updating (Read & Write both permmision)


# 'rb' will open for read in binary mode
# 'rt' will open for read in text mode