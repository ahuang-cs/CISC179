from cisc179.Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, manufacturerName, milesOnVehicle, price, numberOfSeats, options, numberOfDoors):
        super().__init__(manufacturerName, milesOnVehicle, price, numberOfSeats, options)
        self.numberOfDoors = numberOfDoors

    def getNumberOfDoors(self):
        return self.numberOfDoors