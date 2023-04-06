from cisc179.ElectricCar import ElectricCar
def testElectricCar():

   car = ElectricCar("Nissan", 10000, 35995, 4, [], 2);

   assert car.getManufacturerName() == "Nissan"
   assert car.getMilesOnVehicle() == 10000
   assert car.getPrice() == 35995
   assert car.getNumberOfSeats() == 4
   assert car.getNumberOfDoors() == 2