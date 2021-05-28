class Employee:
    company = "Google"     # Parent class

    def showDetails(sself):
        print("This is an employee")


class Programmer(Employee):     # Chaild class
    language = "Python"
    company = "YouTube"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(sself):
        print("This is an programmer")

e = Employee()
print(e.company)
e.showDetails()

p = Programmer()
print(p.company)  # Over write the company name (Google --> YouTube)
p.showDetails()