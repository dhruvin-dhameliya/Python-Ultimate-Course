class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created !")
    
    def getDetails(self):
        print(f"The name of the employee: {self.name}")
        print(f"The salary of the employee: {self.salary}")
        print(f"The name of the employee: {self.subunit}")

    def getSalary(self, signature):
        print(f"Salary for this emplyee working in {self.company} is {self.salary} \n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 8AM in the morning.")

dhruvin = Employee("Dhruvin", 8000, "YouTube")
dhruvin.getDetails()