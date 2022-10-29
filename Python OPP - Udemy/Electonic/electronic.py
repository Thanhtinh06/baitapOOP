class Electronic:
  
    def __init__(self, brand, color, size, feature, use_electricity):
        self.use_electricity = use_electricity
        self.feature = feature
        self.brand = brand
        self.color = color
        self.size = size
        

class TV(Electronic):

    def __init__(self, brand, color, size, feature, use_electricity, resolution, type):
        super().__init__(brand, color, size, feature, use_electricity)
        self.resolution = resolution
        self.type = type
        
class Computer(Electronic):
  
    def __init__(self, brand, color, size, feature, use_electricity, series_CPU, amount_of_RAM, resolution, storage, operating_system, graphics):
        super().__init__(brand, color, size, feature, use_electricity)
        self.series_CPU = series_CPU
        self.amount_of_RAM = amount_of_RAM
        self.resolution = resolution
        self.storage = storage
        self.operating_system = operating_system
        self.graphics = graphics
        

class Desktop(Computer, Electronic):
        
    def __init__(self, brand, color, size, feature, use_electricity, series_CPU, amount_of_RAM, resolution, storage, operating_system, graphics,modal):
          super().__init__(brand, color, size, feature, use_electricity, series_CPU, amount_of_RAM, resolution, storage, operating_system, graphics)
          self.modal = modal
             

class Laptop(Computer, Electronic):
    def __init__(self, brand, color, size, feature, use_electricity, series_CPU, amount_of_RAM, resolution, storage, operating_system, graphics, weight, pin):
        super().__init__(brand, color, size, feature, use_electricity, series_CPU, amount_of_RAM, resolution, storage, operating_system, graphics)

        self.weight = weight
        self.pin = pin