from cisc179.PickupTruck import PickupTruck
def testPickupTruck():
   truck = PickupTruck("Dodge", 9000, 65995, 3, [], 1400);

   assert truck.getManufacturerName() == "Dodge"
   assert truck.getMilesOnVehicle() == 9000
   assert truck.getPrice() == 65995
   assert truck.getNumberOfSeats() == 3
   assert truck.getCargoCapacity() == 1400