from person import Person


class Passenger(Person):
    def __init__(self):
        super().__init__()
        self.tickets = []
        self.quantity = 1

    def setPassenger(self, name, sex, age, quantity, list_ticket):
        self.setPerson(name, sex, age)
        self.quantity = quantity
        self.tickets = list_ticket

    def totalPayment(self):
        total_payment = 0
        for ticket in self.tickets:
            total_payment += int(ticket.price_ticket)
        return total_payment
