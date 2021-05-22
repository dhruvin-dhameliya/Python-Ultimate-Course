# Find a given number is Prime or not prime.

num = int(input("Enter the number: "))

prime = True

for i in range(2, num):
    if(num%2 == 0):
        prime = False
        break

if prime:
    print("This number is Prime.")
else:
    print("This number is not Prime.")