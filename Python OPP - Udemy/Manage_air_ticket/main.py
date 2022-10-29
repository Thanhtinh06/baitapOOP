from passenger import Passenger
from air_ticket import AirTicket
from funcionSort import mergeSort


class InputOutput:

    def inputPassenger(self, n):
        list_passenger = []
        for i in range(n):
            passenger = Passenger()
            name = input()
            sex = input()
            age = input()
            quantity = int(input())
            list_ticket = []
            for j in range(quantity):
                ticket = AirTicket()
                flight_name = input()
                flight_day = input()
                price_ticket = int(input())
                ticket.setAirTicket(flight_name, flight_day, price_ticket)
                list_ticket.append(ticket)
            passenger.setPassenger(name, sex, age, quantity, list_ticket)
            list_passenger.append(passenger)

        return list_passenger

    def outputPassenger(self, list_passenger_shorted):
        print('*************************')

        for passenger in list_passenger_shorted:
            print("- Passenger's Information ")
            print()
            passenger.printInformationPerson()
            print()
            print("- Flight's Information ")
            print()
            for ticket in passenger.tickets:
                ticket.printInformationTicket()
                print()
            print(f"=>  Total payment = {passenger.totalPayment()}")
            print()
            print('--------------------')
        print()


n = int(input())
list_passenger = InputOutput.inputPassenger(InputOutput, n)
lenght_lst = len(list_passenger)
list_passenger_shorted = mergeSort(list_passenger, lenght_lst)
InputOutput.outputPassenger(InputOutput, list_passenger_shorted)
