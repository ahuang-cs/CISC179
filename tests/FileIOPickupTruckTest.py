from cisc179.PickupTruck import PickupTruck
from tests.FileIOTest import FileIOTest


class FileIOPickupTruckTest(FileIOTest):
   def testPickupTruckFile(self):
      pickupTrucks = [PickupTruck("Dodge",15000,9999,7,7500),
              PickupTruck("Chevrolet",30000,14999,5,5000)]

      PickupTruck.saveToFile(super().getFileName(), pickupTrucks)

      loadedPickupTrucks = PickupTruck.loadFromFile(super().getFileName())

      assert len(loadedPickupTrucks) == 2
      assert loadedPickupTrucks[0].getManufacturerName() == "Dodge"
      assert loadedPickupTrucks[0].getMilesOnVehicle() == 15000
      assert loadedPickupTrucks[0].getPrice() == 9999
      assert loadedPickupTrucks[0].getNumberOfSeats() == 7
      assert loadedPickupTrucks[0].getCargoCapacity() == 7500