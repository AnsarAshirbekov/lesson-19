# Используя механизм множественного наследования разработайте класс “Автомобиль”.
# Должны быть классы «Колеса», «Двигатель», «Двери».

class Wheels:
    def __init__(self, wheels_brand):
        self.wheels_brand = wheels_brand

    def get_wheels_brand(self):
        return self.wheels_brand

class Engine:
    def __init__(self, power):
        self.power = power

    def get_engine_power(self):
        return self.power
    
class Doors:
    def __init__(self, openning):
        self.openning = openning

    def get_info_of_doors(self):
        return self.openning
    
class Car(Wheels, Engine, Doors):
    def __init__(self, wheels_brand, power, openning):
        Wheels.__init__(self, wheels_brand) # здесь уже функция super() не сработает, потому что мы наследуем сразу от
        Engine.__init__(self, power)        # нескольких классов разные атрибуты и методы, и нужно указывать от какого
        Doors.__init__(self, openning)      # конкретного класса мы будем наследовать его атрибуты и методы

my_car = Car('Michelin', 200, 'Ручное')

print('Колеса бренда:', my_car.get_wheels_brand())
print('Мощность двигателя:', my_car.get_engine_power(),'л.с.')
print('Открывание дверей:', my_car.get_info_of_doors())