class Person:
    country = "India"

    def takeBreth(self):
        print("I am breathing...")


class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreth(self):
        print("I am an Employee so I am lucily breathing...")


class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmer.")
    
    def takeBreth(self):
        print("I am an programmer so I am breathing++...")

p = Person()
p.takeBreth()
# p.company()   # Throw the error

e = Employee()
e.takeBreth()
print(e.country)
print(e.company)

pr = Programmer()
pr.takeBreth()
print(pr.country)
print(pr.company)