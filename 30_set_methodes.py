# Create Empty Set

b = set()
print(type(b))

# Adding values to an empty Set
b.add(4)
b.add(5)
b.add(6)
b.add(4)    # Set is a collection of non repetitive elements
b.add(4)
b.add(5)

# b.add([1, 2, 3]) Can not add list in Set 

b.add((1, 2, 3)) # Always Tuple is added in Set .

# b.add({1:3}) Can not add Dictionary in Set 

# Not repetitive value print in Set 
print(b)


print("Length of Set: " , len(b)) # Prints the length of this set


b.remove(5)
print("Remove 5 element:" ,b)   # Removes 5 from set b 

print("Any remove in set:" ,b.pop())
print(b)

b.clear()  # Empty the set b
print(b) 