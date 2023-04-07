from cisc179.SportUtilityVehicle import SportUtilityVehicle
from tests.FileIOTest import FileIOTest


class FileIOSportUtilityVehicleTest(FileIOTest):
   def testSportUtilityVehicleFile(self):
      sportUtilityVehicles = [SportUtilityVehicle("Ford",15000,9999,7,3500),
                              SportUtilityVehicle("Toyota",30000,14999,5,2000)]

      SportUtilityVehicle.saveToFile(super().getFileName(), sportUtilityVehicles)

      loadedSportUtilityVehicles = SportUtilityVehicle.loadFromFile(super().getFileName())

      assert len(loadedSportUtilityVehicles) == 2
      assert loadedSportUtilityVehicles[0].getManufacturerName() == "Ford"
      assert loadedSportUtilityVehicles[0].getMilesOnVehicle() == 15000
      assert loadedSportUtilityVehicles[0].getPrice() == 9999
      assert loadedSportUtilityVehicles[0].getNumberOfSeats() == 7
      assert loadedSportUtilityVehicles[0].getMaxTowingWeight() == 3500