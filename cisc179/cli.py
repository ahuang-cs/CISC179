import csv
import sys
from argparse import ArgumentParser
from cisc179.Car import Car

def main():  # pragma: no cover
    cars = []  # list of cars in memory

    # cars.append(Car("Toyota", 12000, 18999, 5))
    # cars.append(Car("BMW", 125000, 8999, 5))

    # validates command line parameters
    parser = ArgumentParser(description="Car management tool")
    parser.add_argument("--carsFile", dest="carsFile", required=True,
                        help="Path to your cars file")
    options = parser.parse_args()

    if options.carsFile:
        print("Read from carsFile:")
        cars = readCars(options.carsFile)
        for car in cars:
            printCar(car)

        while 1:
            car = promptNewCar()
            if not car:
                break
            else:
                cars.append(car)

        saveCars(options.carsFile, cars)
    else:
        sys.exit("Usage:\n\npython -m cisc179 ---carsFile /path/to/file")

def promptNewCar():
    print("Add a new car (S to save and exit):")
    manufacturerName = input("Enter manufacturer name: ")
    if(manufacturerName == "S"):
        return False

    milesOnCar = input("Miles on car: ")
    price = input("Price: ")
    numberOfSeats = input("Number of seats: ")
    numberOfDoors = input("Number of doors: ")

    return Car(manufacturerName, milesOnCar, price, numberOfSeats, numberOfDoors)
def printCar(car):
    print(car.getManufacturerName(), car.getMilesOnVehicle(), car.getPrice(), car.getNumberOfSeats(), car.getNumberOfDoors())
def saveCars(filePath, cars):
    with open(filePath, mode='w', newline='', encoding="utf-8") as carsFile:
        carsCSV = csv.writer(carsFile)
        for car in cars:
            carsCSV.writerow(Car.toArr(car))

def readCars(filePath):
    cars = []
    with open(filePath, mode='r', newline='', encoding="utf-8") as carsFile:
        carsCSV = csv.reader(carsFile)
        for carArr in carsCSV:
            if(len(carArr) > 0):
                cars.append(Car.fromArr(carArr))
    return cars
