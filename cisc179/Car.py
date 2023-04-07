import csv
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
        return Car(arr[0], float(arr[1]), float(arr[2]), int(arr[3]), int(arr[4]))
    @staticmethod
    def prompt():
        print("Add a new car (S to save and exit):")
        manufacturerName = input("Enter manufacturer name: ")
        if(manufacturerName == "S"):
            return False

        milesOnCar = input("Miles on car: ")
        price = input("Price: ")
        numberOfSeats = input("Number of seats: ")
        numberOfDoors = input("Number of doors: ")

        return Car(manufacturerName, milesOnCar, price, numberOfSeats, numberOfDoors)
    @staticmethod
    def print(car):
        print(car.getManufacturerName(), car.getMilesOnVehicle(), car.getPrice(), car.getNumberOfSeats(), car.getNumberOfDoors())
    @staticmethod
    def saveToFile(filePath, cars):
        with open(filePath, mode='w', newline='', encoding="utf-8") as carsFile:
            carsCSV = csv.writer(carsFile)
            for car in cars:
                carsCSV.writerow(Car.toArr(car))
    @staticmethod
    def loadFromFile(filePath):
        cars = []
        with open(filePath, mode='r', newline='', encoding="utf-8") as carsFile:
            carsCSV = csv.reader(carsFile)
            for carArr in carsCSV:
                if(len(carArr) > 0):
                    cars.append(Car.fromArr(carArr))
        return cars
