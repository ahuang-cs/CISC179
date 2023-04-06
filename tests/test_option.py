from cisc179.Vehicle import Vehicle
from cisc179.Option import Option

def testOption():
   moonroof = Option("Moonroof");
   assert moonroof.getDetails() == "Moonroof"

   leather = Option("Leather");
   assert leather.getDetails() == "Leather"
   options = [ moonroof, leather ]

   vehicle = Vehicle("BMW", 90000, 10995, 4, options);

   assert vehicle.getOptions()[0].getDetails() == "Moonroof"
   assert vehicle.getOptions()[1].getDetails() == "Leather"