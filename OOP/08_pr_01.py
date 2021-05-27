class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
         self.name = name
         self.product = product
        
    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} And the product is {self.product}.")

dhruvin = Programmer("Dhruvin", "GitHub")
ravi = Programmer("Ravi", "Skype") 

dhruvin.getInfo()
ravi.getInfo()