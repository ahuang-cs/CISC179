from _pytest.python_api import raises

from cisc179.Vehicle import Vehicle
from cisc179.Option import Option

def testOption():
   moonroof = Option("Moonroof")
   assert moonroof.getDetails() == "Moonroof"

   leather = Option("Leather")
   assert leather.getDetails() == "Leather"
   options = [ moonroof, leather ]

   vehicle = Vehicle("BMW", 90000, 10995, 4, options)

   assert vehicle.getOptions()[0].getDetails() == "Moonroof"
   assert vehicle.getOptions()[1].getDetails() == "Leather"

def testOptionValidation():
   with raises(ValueError, match="Option details must contain a string with less than 32 characters."):
      option = Option("")

   with raises(ValueError, match="Option details must contain a string with less than 32 characters."):
      option = Option("This high performance material, made from a special mixture of powders, resins and fibres in a complex manufacturing process, has been used since the 1970s in braking systems for aerospace applications and since the 1980s in motorsports.")