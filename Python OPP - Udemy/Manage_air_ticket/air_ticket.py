class AirTicket:
    def __init__(self):
        self.flight_name = ''
        self.flight_day = ''
        self.price_ticket = 0

    def setAirTicket(self, flight_name, flight_day, price_ticket):

        self.flight_name = flight_name
        self.flight_day = flight_day
        self.price_ticket = price_ticket

    def getPriceTicket(self):
        return self.price_ticket

    def printInformationTicket(self):
        print(f"Flight name: {self.flight_name}")
        print(f"Flight day: {self.flight_day}")
        print(f"Price tiket: {self.price_ticket}")
