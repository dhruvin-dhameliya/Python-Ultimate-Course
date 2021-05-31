print("-----------------------------------")
print("Select your choice: ")
print("1. Addition")
print("2. Subtrection")
print("3. Multiplication")
print("4. Divison")
print("5. Modules")

while True:
     choice = input("Enter the choice (1/2/3/4/5): ")
     print("-----------------------------------")

     if choice in('1', '2', '3', '4', '5'):
        num1 = float(input("Enter the frist number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(f"Addition is: {num1 + num2}")

        elif choice == '2':
            print(f"Subtrection is: {num1 - num2}")

        elif choice == '3':
            print(f"Multiplication is: {num1 * num2}")

        elif choice == '4':
            print(f"Divison is: {num1 / num2}")

        elif choice == '5':
            print(f"Modules is: {num1 % num2}")
        break
     else:
        print("Envalid Input.")
print("-----------------------------------")