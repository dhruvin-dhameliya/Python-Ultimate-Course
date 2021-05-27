class Employee:
    company = "Google"
    salary = 1000

dhruvin = Employee()
ravi = Employee()
dhruvin.salary = 5000
ravi.salary = 8000

print(dhruvin.company)
print(ravi.company)

Employee.company = "YouTub"
print(dhruvin.company)
print(ravi.company)
 
print(dhruvin.salary)
print(ravi.salary)