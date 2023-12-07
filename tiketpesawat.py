class Flight:
    def __init__(self, flight_number, departure_city, arrival_city, departure_time, arrival_time, seats_available):
        self.flight_number = flight_number
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.seats_available = seats_available

def get_input(prompt):
    return input(prompt)

def create_flight():
    flight_number = get_input("Enter the flight number: ")
    departure_city = get_input("Enter the departure city: ")
    arrival_city = get_input("Enter the arrival city: ")
    departure_time = get_input("Enter the departure time (format: HH:MM): ")
    arrival_time = get_input("Enter the arrival time (format: HH:MM): ")
    seats_available = int(get_input("Enter the number of available seats: "))

    return Flight(flight_number, departure_city, arrival_city, departure_time, arrival_time, seats_available)

def book_flight(flight, seats_to_book):
    if flight.seats_available >= seats_to_book:
        flight.seats_available -= seats_to_book
        print(f"Flight {flight.flight_number} successfully booked with {seats_to_book} seats.")
    else:
        print(f"Sorry, there are not enough available seats on Flight {flight.flight_number}.")

def main():
    flights = []

    while True:
        action = get_input("Enter 'create' to create a new flight, 'book' to book a flight, or 'exit' to exit the program: ")

        if action == "create":
            flights.append(create_flight())
        elif action == "book":
            flight_number = get_input("Enter the flight number to book: ")
            flight = next((flight for flight in flights if flight.flight_number == flight_number), None)

            if flight:
                seats_to_book = int(get_input("Enter the number of seats to book: "))
                book_flight(flight, seats_to_book)
            else:
                print(f"Sorry, there is no flight with the number {flight_number}.")
        elif action == "exit":
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
