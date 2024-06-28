# Создайте класс Ship, который содержит информацию о корабле. С помощью механизма
# наследования, реализуйте класс Frigate (содержит информацию о фрегате), класс Destroyer
# (содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые для работы методы. 

class Ship:
    def __init__(self, country, speed):
        self.country = country
        self.speed = speed

    def get_info(self):
        return f'This ship belong {self.country} and has speed {self.speed} knots'
    
class Frigate(Ship):
    def __init__(self, country, speed, cannons):
        super().__init__(country, speed)
        self.cannons = cannons

    def salvo_of_cannons(self):
        return f'This frigate can fire a salvo of {self.cannons} cannons'
    
class Destroyer(Ship):
    def __init__(self, country, speed, torpedoes):
        super().__init__(country, speed)
        self.torpedoes = torpedoes

    def torpedo_stock(self):
        return f'This destroyer has a stock of {self.torpedoes} torpedoes'
    
class Cruiser(Ship):
    def __init__(self, country, speed, weight):
        super().__init__(country, speed)
        self.weight = weight

    def cruiser_weight(self):
        return f'This cruiser has weight {self.weight} tons'
    
destroyer = Destroyer('USA', 50, 30)
print(destroyer.torpedo_stock())