import sys
from argparse import ArgumentParser
from cisc179.Car import Car

def main():  # pragma: no cover
    cars = []  # list of cars in memory

    # validates command line parameters
    parser = ArgumentParser(description="Car management tool")
    parser.add_argument("--carsFile", dest="carsFile", required=True,
                        help="Path to your cars file")
    options = parser.parse_args()

    if options.carsFile:
        print("Read from carsFile:")
        cars = Car.loadFromFile(options.carsFile)
        for car in cars:
            Car.print(car)

        while 1:
            car = Car.prompt()
            if not car:
                break
            else:
                cars.append(car)

        Car.saveToFile(options.carsFile, cars)
    else:
        sys.exit("Usage:\n\npython -m cisc179 ---carsFile /path/to/file")

