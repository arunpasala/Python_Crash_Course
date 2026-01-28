class Car:
    """A simple attempt to represent a car."""
    def __init__(self,make,model,year):
        """Initialize the attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Retrun a neatly formatted descriptive name"""
        long_name=(f"{self.year} {self.make} {self.model}")
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the reaading of the car's milage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    
    def update_odometer(self, mileage):
        """ set the odometer value to given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back on odometer reading")
    
    def increment_odeometer(self,miles):
        """Add give mileage to odometer"""
        self.odometer_reading += miles
        

class ElectricCar(Car):
    """Define aspects of a car, specific to electric vechiles."""
    
    def __init__(self,make, model, year):
        """Initialize attributes of parent class.
        Then intialize attributes specific to an child class(electric  car)"""
        super().__init__(make,model,year)
        self.battery_size=40


    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has {self.battery_size}-KWH battery")
        
        
my_leaf = ElectricCar("nissan","leaf","2026")
print(my_leaf.get_descriptive_name())
print(my_leaf.describe_battery())
        
        