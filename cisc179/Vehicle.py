class Vehicle:
    def __init__(self, manufacturerName, milesOnVehicle, price, numberOfSeats, options):
        self.manufacturerName = manufacturerName
        self.milesOnVehicle = milesOnVehicle
        self.price = price
        self.numberOfSeats = numberOfSeats
        self.options = options

    def getManufacturerName(self):
        return self.manufacturerName

    def getMilesOnVehicle(self):
        return self.milesOnVehicle

    def getPrice(self):
        return self.price

    def getNumberOfSeats(self):
        return self.numberOfSeats
    def getOptions(self):
        return self.options