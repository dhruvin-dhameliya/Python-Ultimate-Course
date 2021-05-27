# Train Resurvation Program:

class Train:
    def __init__(self, name, fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

# Get Status Parts:
    def getStatus(self):
        print("************************")
        print(f"The name of train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************************")


# Fare Info Parts:
    def fareInfo(self):
        print(f"The price of the ticket is: Rs. {self.fare}")



# Book Tichet Parts:
    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal...")



# Cancel Ticket Parts:
    def cancelTicket(self):
        if(self.bookTicket):
            print("Your ticket is cancel.")
            self.seats = self.seats + 1
        else:
            print("Your ticket is not cancel... Try again !!!...")
        

# Printing Parts:

intercity = Train("Intercity Express - 14015", 90, 200) 
intercity.getStatus()    # Show the full status
intercity.fareInfo()     # price of ticket 


intercity.bookTicket()  
intercity.bookTicket()   # Ticket Book
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()   # Show the full status


intercity.cancelTicket()  # Cancel Ticket
intercity.getStatus()    #  Show the full status