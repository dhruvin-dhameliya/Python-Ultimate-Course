# Find a given number is Factorial.

n = int(input("Enter name: "))
p = 1
for i in range(n):      # Normal program using For loop.
    p = p * (i+1)
print(p)

print("-------------------------")

def factorial_iter(n):
    p = 1
    for i in range(n):    # UDF function use in factorial program.
        p = p * (i+1)
    return p

f = factorial_iter(5)
print(f)

print("-------------------------")

def factorial_recuesive(n):
    if n == 1 or n == 0:   
        return 1                # Recurstion function use in factorial program.
    return n * factorial_recuesive(n-1)

f = factorial_recuesive(4)
print(f)
