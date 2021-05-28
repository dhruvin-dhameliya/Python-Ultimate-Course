# Inheritance in supar method:

class Person:
    country = "India"
    def __init__(self):
        print("Initializing Person...\n")
        
        
    def takeBreth(self):
        print("I am breathing...")


class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")

    def getSalary(self):
        super().takeBreth()
        print(f"Salary is {self.salary}")
    
    def takeBreth(self):
        super().takeBreth()
        print("I am an Employee so I am lucily breathing...")


class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer...\n")

    def getSalary(self):
        print(f"No salary to programmer.")
    
    def takeBreth(self):
        super().takeBreth()
        print("I am an programmer so I am breathing++...")

# p = Person()
# p.takeBreth()

# e = Employee()
# e.takeBreth()

pr = Programmer()
# pr.takeBreth()
