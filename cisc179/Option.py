class Option:
    def __init__(self, details):
        self.setDetails(details)

    def getDetails(self):
        return self.details

    def setDetails(self, newDetails):
        if newDetails == "" or len(newDetails) > 32 or not isinstance(newDetails, str):
            raise ValueError("Option details must contain a string with less than 32 characters.")
        self.details = newDetails