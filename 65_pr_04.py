# Sum of Natural Number.

def n_sum(n):
    if n == 1 or n == 0:   
        return 1                # Recurstion function use in factorial program.
    return n + n_sum(n-1)

f = n_sum(5)   # Given the number.

print(f)

print("-------------------------------------")

print(f"Sum of netural number is: {f}")       # Deferent staels print the statment.

print("-------------------------------------")

print("Sum of netural number is: " + str(f))