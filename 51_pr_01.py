# Create Multiplication Table.

num = int(input("Enter the number: "))

        # Using For Loop...

# Simple method.
for i in range(1, 11):
    print(str(num) + " x " + str(i) + " = " + str(i*num))

print("--------------")

# Using a --> F string.
for i in range(1, 11):
     print(f"{num}X{i}={num*i}")

print("--------------")

            # Using While Loop...
i = 1
while i<=10:
    print(str(num) + " x " + str(i) + " = " + str(i*num))
    i = i + 1

print("--------------")

i = 1
while i<=10:
    print(f"{num}X{i}={num*i}")
    i = i + 1