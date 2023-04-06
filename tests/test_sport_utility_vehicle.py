from cisc179.SportUtilityVehicle import SportUtilityVehicle
def testSportUtilityVehicle():
   suv = SportUtilityVehicle("Toyota", 19000, 75995, 6, [], 4500);

   assert suv.getManufacturerName() == "Toyota"
   assert suv.getMilesOnVehicle() == 19000
   assert suv.getPrice() == 75995
   assert suv.getNumberOfSeats() == 6
   assert suv.getMaxTowingWeight() == 4500