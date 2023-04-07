from cisc179.Car import Car
from tests.FileIOTest import FileIOTest


class FileIOCarTest(FileIOTest):
   def testCarFile(self):
      cars = [Car("Ford",15000,9999,7,4),
              Car("Toyota",30000,14999,5,4)]

      Car.saveToFile(super().getFileName(), cars)

      loadedCars = Car.loadFromFile(super().getFileName())

      assert len(loadedCars) == 2
      assert loadedCars[0].getManufacturerName() == "Ford"
      assert loadedCars[0].getMilesOnVehicle() == 15000
      assert loadedCars[0].getPrice() == 9999
      assert loadedCars[0].getNumberOfSeats() == 7
      assert loadedCars[0].getNumberOfDoors() == 4