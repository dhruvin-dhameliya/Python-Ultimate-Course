# The Factorial of given number using for loop.
num = int(input("Enter the number: "))
fecto = 1
for i in range(1, num+1):
    fecto = fecto * i

print("Fectorial of " + str(num) + " is: " + str(fecto))

# Both are valid print statment

print(f"Fectorial of {num} is: {fecto}")