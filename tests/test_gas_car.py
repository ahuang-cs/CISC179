from cisc179.GasCar import GasCar
def testGasCar():
   car = GasCar("BMW", 5500, 75995, 4, [], 2);

   assert car.getManufacturerName() == "BMW"
   assert car.getMilesOnVehicle() == 5500
   assert car.getPrice() == 75995
   assert car.getNumberOfSeats() == 4
   assert car.getNumberOfDoors() == 2