class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this emplyee working in {self.company} is {self.salary} \n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 8AM in the morning.")

dhruvin = Employee()
dhruvin.salary = 80000
dhruvin.getSalary("Thanks!")  # Or   Employee.getSalary(dhruvin)

dhruvin.greet()   # Employee.greet()

dhruvin.time()    # Employee.time()