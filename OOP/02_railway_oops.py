class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Nmae is: {self.name}")
        print(f"Train is: {self.train}")

dhruvinApplication = RailwayForm()
dhruvinApplication.name = "Dhruvin"
dhruvinApplication.train = "Rajdhani Express"
dhruvinApplication.printData()