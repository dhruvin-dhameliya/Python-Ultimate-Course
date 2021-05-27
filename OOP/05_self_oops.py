class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this emplyee working in {self.company} is {self.salary} ")


dhruvin = Employee()
dhruvin.salary = 80000
dhruvin.getSalary()    # Or   Employee.getSalary(dhruvin)
