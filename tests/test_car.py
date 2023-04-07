from cisc179.Car import Car
def testCar():
   car = Car("BMW", 190000, 5995, 4, 2);

   assert car.getManufacturerName() == "BMW"
   assert car.getMilesOnVehicle() == 190000
   assert car.getPrice() == 5995
   assert car.getNumberOfSeats() == 4
   assert car.getNumberOfDoors() == 2