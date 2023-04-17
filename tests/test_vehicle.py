from _pytest.python_api import raises

from cisc179.Vehicle import Vehicle

def testVehicle():
   vehicle = Vehicle("GMC", 80000.8, 7999.95, 4, [])

   assert vehicle.getManufacturerName() == "GMC"
   assert vehicle.getMilesOnVehicle() == 80000.8
   assert vehicle.getPrice() == 7999.95
   assert vehicle.getNumberOfSeats() == 4

def testVehicleManufacturerNameValidation():
   with raises(ValueError, match="Vehicle manufacturer name must contain a string with less than 16 characters."):
      vehicle = Vehicle("", 180000, 17995, 4, [])
      vehicle = Vehicle("International Consolidated Airlines Group SA", 10000, 1995, 5, [])
      vehicle = Vehicle(27, 180000, 17995, 4, [])

def testVehicleMilesOnVehicleValidation():
   with raises(ValueError, match="Vehicle miles on vehicle must be a non-negative number."):
      vehicle = Vehicle("GMC", -80000, 7995, 4, [])
      vehicle = Vehicle("GMC", "a", 7995, 4, [])

def testVehiclePriceValidation():
   with raises(ValueError, match="Vehicle price must be a non-negative number."):
      vehicle = Vehicle("GMC", 80000, -7995.90, 4, [])
      vehicle = Vehicle("GMC", 80000, "b", 4, [])

def testVehicleNumberOfSeatsValidation():
   with raises(ValueError, match="Vehicle number of seats must be a non-negative whole number."):
      vehicle = Vehicle("GMC", 80000, -7995.90, 4.5, [])
      vehicle = Vehicle("GMC", 80000, 7999.95, "c", [])