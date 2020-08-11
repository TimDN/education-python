class Thermometer:
    """
    A thermometer class that is used to keep track of the current
    temperature.
    !! Only supports celsius as the temperature unit !!
    """
    def __init__(self, inital_temp = 0):
        """
        :param inital_temp: Default value is 0
        """
        self.temperature = inital_temp
        self.unit = "celsius"

    def __str__(self):
        """
        Overloaded __str__

        :returns: Current temperature and which temperature unit is in use
        """
        return "{} degrees {}".format(self.temperature, self.unit)

    def change_temperature(self, new_temperature):
        """
        :param new_temperautre: The new temperature in celsius
        :raises ValueError: If below absolute zero
        """
        if new_temperature < -273.15:
            raise ValueError("Can not set below absolute zero")
        self.temperature


temp = Thermometer(10)
temp.change_temperature(100)
print(temp)