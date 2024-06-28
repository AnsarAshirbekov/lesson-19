# Используя понятие множественного наследования, разработайте класс «Окружность,
# вписанная в квадрат». 

class Square:
    def __init__(self, side):
        self.side = side

    def square_area(self):
        return self.side ** 2
    
    def perimetr(self):
        return self.side * 4
    
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return 3.14 * self.radius ** 2
    
    def circumference(self):
        return 2 * 3.14 * self.radius
    
class CircleInSquare(Square, Circle):
    def __init__(self, side):
        super().__init__(side) # наследуем от двух предыдущих классов и принимаемым аргументом будет только сторона квадрата
                                    
        self.radius = side / 2 # находим радиус окружности, вписанной в квадрат

circle_in_square = CircleInSquare(6)

print('Площадь окружности, вписанной в квадрат:', circle_in_square.circle_area())
print('Площадь квадрата, в который вписана окружность:', circle_in_square.square_area())
print('Длина окружности, вписанной в квадрат:', circle_in_square.circumference())
print('Периметр квадрата, в который вписана окружность:', circle_in_square.perimetr())