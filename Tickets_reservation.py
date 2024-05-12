import datetime
class Event:
    def __init__(self, event_name, event_date, event_time, event_place):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.event_place = event_place
    def __str__(self):
        return f"Event: {self.event_name}, Date: {self.event_date}, Time: {self.event_time}, Place: {self.event_place}"

class Ticket(Event):
    def __init__(self, event_name, event_date, event_time, event_place, ticket_price, ticket_quantity):
        super().__init__(event_name, event_date, event_time, event_place)
        self.ticket_price = ticket_price
        self.ticket_quantity = ticket_quantity
    def __str__(self):
        return f"Event: {self.event_name}, Date: {self.event_date}, Time: {self.event_time}, Place: {self.event_place}, Price: {self.ticket_price}, Quantity: {self.ticket_quantity}"
    def total_price(self):
        return self.ticket_price * self.ticket_quantity

event1 = Event("Depeche Mode Concert", datetime.date(2020, 12, 15), datetime.time(20, 0), "Warsaw")
event2 = Event("Madonna Concert", datetime.date(2020, 12, 20), datetime.time(20, 0), "Warsaw")
event3 = Event("Queen Concert", datetime.date(2020, 12, 25), datetime.time(20, 0), "Warsaw")

ticket1 = Ticket("Depeche Mode Concert", datetime.date(2020, 12, 15), datetime.time(20, 0), "Warsaw", 200, 1)
ticket2 = Ticket("Madonna Concert", datetime.date(2020, 12, 20), datetime.time(20, 0), "Warsaw", 300, 1)
ticket3 = Ticket("Queen Concert", datetime.date(2020, 12, 25), datetime.time(20, 0), "Warsaw", 400, 1)

class reservation:
    def __init__(self):
        self.reservation_list = []
    def add_ticket(self, ticket):
        self.reservation_list.append(ticket)
    def total_price(self):
        return sum([ticket.total_price() for ticket in self.reservation_list])

res = reservation()

while True:

    print("1. Show events")
    print("2. Add ticket to reservation")
    print("3. Total price")
    print("4. Show reservation")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("1.", event1)
        print("2.", event2)
        print("3.", event3)
    elif choice == "2":
        print("1. Depeche Mode Concert")
        print("2. Madonna Concert")
        print("3. Queen Concert")
        event_choice = input("Enter event choice: ")
        quantity = input("Enter quantity: ")
        if event_choice == "1":
            ticket1.ticket_quantity = int(quantity)
            res.add_ticket(ticket1)
        elif event_choice == "2":
            ticket2.ticket_quantity = int(quantity)
            res.add_ticket(ticket2)
        elif event_choice == "3":
            ticket3.ticket_quantity = int(quantity)
            res.add_ticket(ticket3)
    elif choice == "3":
        print(res.total_price())
    elif choice == "4":
        for ticket in res.reservation_list:
            print(ticket)
    elif choice == "5":
        print("Goodbye, enjoy the concert!")
        break




