class Flight:
    def __init__(self, flight: tuple) -> None:
        self.flight = flight

    def __str__(self):
        return f' flight {self.flight[0]} is set on {self.flight[1]}, ' \
            f' departures from {self.flight[2]} and arrives in {self.flight[3]} at {self.flight[4]}'


A = [input('enter an prod_number'), int(input('Enter the time of departure')), input('Enter the gate of departure')]
B = [input('Enter the gate of arrival'), int(input('Enter the time of arrival'))]
C = [input('enter an prod_number'), int(input('Enter the time of departure')), input('Enter the gate of departure')]
D = [input('Enter the gate of arrival'), int(input('Enter the time of arrival'))]
print(A, B, C, D)
list_of_flights = [zip(A, B), zip(C + D)]
print(list_of_flights)
for element in list_of_flights:
    print(Flight(element))

# add description
# add dint
