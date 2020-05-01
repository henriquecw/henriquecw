class Flight:

	counter = 1

	def __init__(self, origin, destination, duration):

		self.id = Flight.counter
		Flight.counter += 1

		self.passengers = []

		self.origin = origin
		self.destination = destination
		self.duration = duration


	def print_info(self):
		print(f"Flight origin: {self.origin}")
		print(f"Flight destination: {self.destination}")
		print(f"Flight duration: {self.duration}")

		print()
		print("Passengers")
		for passenger in self.passengers:
			print(f"{passenger.name}")

	def delay(self, amount):
		self.duration += amount

	def add_passenger(self, p):
		self.passengers.append(p)
		p.flight_id = self.id


class Passenger:

	def __init__(self, name):
		self.name = name

def main():

	# Create flight.
	f = Flight(origin="New York", destination="Paris", duration=540)

	# Change the value of a variable
	f.duration += 10

	# Print details about flight.
	print(f.origin)
	print(f.destination)
	print(f.duration)

if __name__ == "__main__":
	main()