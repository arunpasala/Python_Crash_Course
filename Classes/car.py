class Car:
    """A simple attempt to represent a car"""
    
    def __init__(self, make , model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        #setting a default value for an attribute
        self.odometer_reading = 0
        
        #When an instance is created, attributes can be defined without being passed in as parameters.
        #These attributes can be defined in the __init__() method, Where they are assigned a default value.
        
        
    def get_descriptive_name(self):
        """Retrun a neatly formatted descriptive name"""
        long_name=(f"{self.year} {self.make} {self.model}")
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the reaading of the car's milage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    
    def update_odometer(self, mileage):
        """ set the odometer value to given value"""
        self.odometer_reading = mileage
    
my_new_car = Car('audi','a4','2026')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#modifying attribute value directly
print("\nmodifying attribute value directly")
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#modifying an Attribute's value through a method
print("\nmodifying attribute value through a method")
my_new_car.update_odometer(24)
my_new_car.read_odometer()






