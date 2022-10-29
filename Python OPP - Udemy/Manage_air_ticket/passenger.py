from people import People
from air_ticket import AirTicket
from funcionSort import mergeSort, merge


class Passenger(People):
    def __init__(self):
        super().__init__()
        self.has_air_ticket = []
        self.quality = 1

    def setPassenger(self):
        self.setPeople()
        self.quality = int(input())
        for i in range(self.quality):
            ticket = AirTicket()
            ticket.setAirTicket()
            self.has_air_ticket.append(ticket)

    def totalPayment(self):
        total_payment = 0
        for ticket in self.has_air_ticket:
            total_payment += int(ticket.price_ticket)
        return total_payment


list_passenger = []
n = int(input())
for i in range(n):
    passenger = Passenger()
    passenger.setPassenger()
    list_passenger.append(passenger)

lenght_lst = len(list_passenger)
list_passenger_shorted = mergeSort(list_passenger, lenght_lst)

print('*************************')

for passenger in list_passenger_shorted:
    print("- Passenger's Information ")
    print()
    passenger.getInformationPeople()
    print()
    print("- Flight's Information ")
    print()
    for ticket in passenger.has_air_ticket:
        ticket.getInformationTicket()
        print()
    print(f"=>  Total payment = {passenger.totalPayment()}")
    print()
    print('--------------------')
print()
