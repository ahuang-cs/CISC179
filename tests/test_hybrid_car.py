from cisc179.HybridCar import HybridCar
def testHybridCar():
   car = HybridCar("Toyota", 1000, 63995, 4, [], 2);

   assert car.getManufacturerName() == "Toyota"
   assert car.getMilesOnVehicle() == 1000
   assert car.getPrice() == 63995
   assert car.getNumberOfSeats() == 4
   assert car.getNumberOfDoors() == 2