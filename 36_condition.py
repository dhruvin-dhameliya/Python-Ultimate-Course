a = 10
b = 25

# Simpale if statment.
if(a<b):
    print("B greter than A.")


# Simpale if-else statment.
if(a>b):
    print("B greter than A.")
else:
    print("B not greter than A.")


# Simpale Nested if statment.
if(a<b):
    if(a==b):
        print("A and B is Equal to.")
    else:
        print("A and B is not Equal to.")


# Simpale if-esif-else statment.
if(a>b):
    print("A greter than B.")
elif(a!=b):
    print("A and B is not Equal to.")
elif(a==b):
        print("A and B is Equal to.")
else:
    print("B greter than A.")

print("--------------------------------------------")


# Else is Optional in Python.
if(a>b):                            # IMP 
    print("A greter than B.")
elif(a!=b):                             
    print("A and B is not Equal to.")       # This program in not use Else part 
elif(a==b):                                 # And can be Run Programs and not throws syntex error   
        print("A and B is Equal to.")



print("--------------------------------------------")

# OPERATORS :

age = int(input("Enter your age: "))

if(age>18 and age<51):
    print("You can work with us.")
else:                                              # AND - logical operator
    print("You cannot work with us.")


if(age>18 or age==18):
    print("You can work with us.")
else:                                              # OR - logical operator
    print("You cannot work with us.")
    
print("--------------------------------------------")

# In and Is function in Python.

a = None

if(a is None):
    print("Yes")   # Is function
else:
    print("No")


l = [45, 32, 51, 88, 251]

print(51 in l)     # In function
print(250 in l)

