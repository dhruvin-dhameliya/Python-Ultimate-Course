class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradLevel(self):
        self.level = self.level + 1

class Employee:
    company = "Visa"
    eCode = 120

class Programmer(Freelancer, Employee):    # Frist praorites a frist name 
    name = "Ravi"

p = Programmer()
p.upgradLevel()
print(p.level)
print(p.company)   # Print the company name == Freelancer 