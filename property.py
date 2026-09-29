# class OurClass:

#     def __init__(self, a):
#         self.OurAtt = a

#     @property
#     def OurAtt(self):
#         return self.__OurAtt

#     @OurAtt.setter
#     def OurAtt(self,val):
#         if val < 0 :
#             self.__OurAtt=0
#         elif val >1000:
#             self.__OurAtt=1000
#         else:
#             self.__OurAtt=val


# x = OurClass(101022)
# print(x.OurAtt)


# Making Getters and Setter methods
class Celsius:
    def __init__(self, temperature=0):
        self._temperature=temperature

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value


# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature attribute via a getter
print(human.get_temperature())

# Get the to_fahrenheit method, get_temperature() called by the method itself
print(human.to_fahrenheit())

# new constraint implementation
human.set_temperature(-300)

# Get the to_fahreheit method
print(human.to_fahrenheit())