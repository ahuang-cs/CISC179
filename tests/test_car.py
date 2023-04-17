from _pytest.python_api import raises

from cisc179.Car import Car
def testCar():
   car = Car("BMW", 190000, 5995, 4, [], 2)

   assert car.getManufacturerName() == "BMW"
   assert car.getMilesOnVehicle() == 190000
   assert car.getPrice() == 5995
   assert car.getNumberOfSeats() == 4
   assert car.getNumberOfDoors() == 2

def testCarDoorValueException():
   with raises(ValueError, match = "A car must have more than one door."):
      car = Car("Kia", 120000, 4995, 5, [], 0)
