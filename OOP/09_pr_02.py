n = int(input("Enter the number: "))

class Calculator:
    def __init__(self,num):
        self.num = num
    
    def square(self):
        print(f"The value of {self.num} square is {self.num **2}")
    
    def squareRoot(self):
        print(f"The value of {self.num} square root is {self.num **0.5}")
    
    def cube(self):
        print(f"The value of {self.num} cube is {self.num **3}")

a = Calculator(n)   # Enter the user input number. // Print this number.
a.square()
a.squareRoot()
a.cube()