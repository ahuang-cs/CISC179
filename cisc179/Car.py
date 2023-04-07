from cisc179.Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, manufacturerName, milesOnVehicle, price, numberOfSeats, numberOfDoors):
        super().__init__(manufacturerName, milesOnVehicle, price, numberOfSeats)
        self.numberOfDoors = numberOfDoors

    def getNumberOfDoors(self):
        return self.numberOfDoors

    @staticmethod
    def toArr(car):
        return [car.manufacturerName, car.milesOnVehicle, car.price, car.numberOfSeats, car.numberOfDoors]

    @staticmethod
    def fromArr(arr):
        return Car(arr[0], arr[1], arr[2], arr[3], arr[4])