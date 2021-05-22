num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num4):
    f1 = num1 
else:           # Comper num1 and num4 
    f1 = num4

if(num2>num3):
    f2 = num2
else:           # Comper num2 and num3 
    f2 = num3

if(f1>f2):
    print(f1, "is Gretest number.")
else:
    print(f2, "is Gretest number.")