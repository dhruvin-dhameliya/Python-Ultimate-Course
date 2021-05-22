
# Print the pattern follow:
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *  ......
n = int(input("Enter the number: "))

for i in range(n):
        print("* " * (i+1))

# Both are valide

for i in range(n+1):
        print("* " * (i))