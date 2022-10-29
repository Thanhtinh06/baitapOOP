class AirTicket:
    def __init__(self):
        self.flight_name = ''
        self.flight_day = ''
        self.price_ticket = 0

    def setAirTicket(self):

        self.flight_name = input()
        self.flight_day = input()
        self.price_ticket = input()

    def getPriceTicket(self):
        return self.price_ticket

    def getInformationTicket(self):
        print(f"Flight name: {self.flight_name}")
        print(f"Flight day: {self.flight_day}")
        print(f"Price tiket: {self.price_ticket}")
