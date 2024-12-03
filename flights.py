#Kevin Henderson
#11/29/2024
import json
class Flights:
    
    #flights = [] #might need to put this in __init__ as self.flights = [], might also be for individual flights
    
    def __init__(self, filename, /):
        self.filename = filename
        self.flights = []
        try:
            with open(filename, 'r') as f:
                self.flights = json.load(f)
        except FileNotFoundError:
            print("File not found!")
    def add_flight(self, origin, destination, number, /):
        pass

    def get_flights(self, /):
        pass