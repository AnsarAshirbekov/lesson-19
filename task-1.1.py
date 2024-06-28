# Создайте класс Device, который содержит информацию об устройстве. С помощью
# механизма наследования, реализуйте класс CoffeeMachine (содержит информацию о
# кофемашине), класс Blender (содержит информацию о блендере), класс MeatGrinder
# (содержит информацию о мясорубке). Каждый из классов должен содержать необходимые
# для работы методы.

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def get_info(self):
        return f"{self.brand} {self.model}"


class CoffeeMachine(Device):
    def __init__(self, brand, model, coffee_type):
        super().__init__(brand, model)
        self.coffee_type = coffee_type
    
    def make_coffee(self):
        return f"Making {self.coffee_type} coffee"


class Blender(Device):
    def __init__(self, brand, model, speed_levels):
        super().__init__(brand, model)
        self.speed_levels = speed_levels
    
    def blend(self):
        return f"Blending at {self.speed_levels} speed levels"


class MeatGrinder(Device):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity
    
    def grind_meat(self):
        return f"Grinding meat with {self.capacity} capacity"

coffee_machine = CoffeeMachine('Zojirushi', 'EC-ESC120', 'Capuccino')
coffee = coffee_machine.make_coffee()
print(coffee)