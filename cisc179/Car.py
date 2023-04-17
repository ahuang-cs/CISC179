from cisc179.Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, manufacturerName, milesOnVehicle, price, numberOfSeats, options, numberOfDoors):
        super().__init__(manufacturerName, milesOnVehicle, price, numberOfSeats, options)
        self.setNumberOfDoors(numberOfDoors)

    def getNumberOfDoors(self):
        return self.numberOfDoors

    def setNumberOfDoors(self, newNumberOfDoors):
        if(newNumberOfDoors < 1):
            raise ValueError("A car must have more than one door.")
        self.numberOfDoors = newNumberOfDoors