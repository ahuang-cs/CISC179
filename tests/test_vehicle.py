from cisc179.Vehicle import Vehicle

def testVehicle():
   vehicle = Vehicle("GMC", 80000, 7995, 4);

   assert vehicle.getManufacturerName() == "GMC"
   assert vehicle.getMilesOnVehicle() == 80000
   assert vehicle.getPrice() == 7995
   assert vehicle.getNumberOfSeats() == 4
