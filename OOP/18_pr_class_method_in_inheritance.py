class Employee:
    company = "Apple"
    salary = 800
    location = "Benglor"

    # def changeSalary(self, sal):         # This method is valid,
    #     self.__class__.salary = sal
    
    @classmethod
    def changeSalary(cls, sal):        # But this shortcut method.
        cls.salary = sal    
    
e = Employee()
print(e.salary)

e.changeSalary(950)
print(e.salary)

print(Employee.salary)