# Создайте базовый класс Shape для рисования плоских фигур.
# Определите методы:
# Show() — вывод на экран информации о фигуре;
# Save() — сохранение фигуры в файл;
# Load() — считывание фигуры из файла.
# Определите производные классы:
# Square — квадрат, который характеризуется координатами левого верхнего угла и
# длиной стороны;
# Rectangle — прямоугольник с заданными координатами верхнего левого угла и
# размерами;
# Circle — окружность с заданными координатами центра и радиусом;
# Ellipse — эллипс с заданными координатами верхнего угла, описанного вокруг него
# прямоугольника со сторонами, параллельными осям координат, и размерами этого
# прямоугольника. Создайте список фигур, сохраните фигуры в файл, загрузите в другой список
# и отобразите информацию о каждой из фигур.

# Создадим базовый класс
class Shape:
    # Здесь будет содержаться конструктор, который будет пустым, и будет переопределяться в производных классах
    def __init__(self):
        pass
    # Метод Show также будет пустым и будет переопределяться в производных классах
    def Show(self):
        pass
    # Создадим метод для сохранения информации о фигуре в некоторый файл filename
    def Save(self, filename):
        with open(filename, 'w') as file:
            file.write(self.get_save_string()) # здесь будет вызываться метод из производных классов, которые будут
                                               # выдавать строку с информацией о фигуре
        # Затем здесь будет выдаваться сообщение об успешном сохранении объекта фигуры, где type(self).__name__ вернет
        # имя текущего класса объекта, что позволит точно указать тип сохраненного объекта 
        print(f'Сохранен объект класса {type(self).__name__} в файл {filename}')
    # Далее создадим классовый метод, который позволит нам работать не только с конкретным экземпляром класса, а со всем
    # классом в целом 
    @classmethod
    # этот метод будет принимать в качестве первого аргумента сам класс (cls), к которому будет применяться метод Load, и в 
    # качестве второго аргумента файл filename, из которого будет производиться загрузка данных
    def Load(cls, filename):
        with open(filename, 'r') as file:
            data = file.read().strip() # считываем информацию из файла без лишних пробелов и записываем в новую переменную
        # Далее здесь будет применяться метод из производных классов к тому классу, к которому будет применяться метод Load,
        # то есть cls и на основе данных считанных из файла будет создан новый экземпляр этого класса
        return cls.from_load_string(data)

# Теперь создаем класс Квадрат, который будет производным классом от базового класса Фигура     
class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__() # здесь унаследованный конструктор будет переопределяться и задаст свои атрибуты
        self.x = x
        self.y = y
        self.side = side    
    def Show(self): # унаследованный метод также будет переопределяться и выдавать строку с некоторой информацией
        print(f"Квадрат: Координаты левого верхнего угла: ({self.x}; {self.y}), длина стороны: {self.side}")
    # Далее здесь создадим метод, который будет работать почти как предыдущий метод Show, но только будет возвращать 
    # строку с информацией, чтобы ее смог применить метод Save из базового класса и создать файл с этой строкой 
    def get_save_string(self):
        return f"{self.x},{self.y},{self.side}"
    # Теперь создадим классовый метод для отправки данных для создания нового экземпляра класса
    @classmethod
    # Этот метод будет использоваться методом из базового класса Load, который уже считал информацию с некоторого файла и
    # и записал ее в переменную data в виде строки. Он будет вызывать этот метод и передаст ему эту переменную.
    def from_load_string(cls, data): # cls в классовых методах работает почти как self в обычных методах и используется
                                     # по умолчанию. Желательно его указывать, чтобы явно определить с каким классом мы 
                                     # сейчас работаем. В данном случае с классом Square
        # метод будет брать строку из переменной data и конвертировать ее в список с разделителим запятой ","
        parts = data.split(',')
        # затем из списка будут извлекаться элементы и записываться в переменные
        x = int(parts[0])
        y = int(parts[1])
        side = int(parts[2])
        # потом эти переменные будут выступать аргументами, закладываемыми в новый экземпляр класса Square 
        return cls(x, y, side) # Теперь этот класс отправится к методу Load, который в свою очередь также ее "вернет"
        # Результат работы классовых методов Load и from_load_string один и тот же по сути - создание нового экземпляра 
        # класса, можно было б их объединить, но у Shape будут и другие производные классы, помимо Square, у которых 
        # передаваемые аргументы будут другими, поэтому эти методы нужно разделить

# Создадим следующие производные классы
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def Show(self):
        print(f"Прямоугольник: Координаты верхнего левого угла: ({self.x}; {self.y}), ширина: {self.width}, высота: {self.height}")
    
    def get_save_string(self):
        return f"{self.x},{self.y},{self.width},{self.height}"
    
    @classmethod
    def from_load_string(cls, data):
        parts = data.split(',')
        x = int(parts[0])
        y = int(parts[1])
        width = int(parts[2])
        height = int(parts[3])
        return cls(x, y, width, height)

class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
    
    def Show(self):
        print(f"Окружность: Координаты центра: ({self.center_x}; {self.center_y}), радиус: {self.radius}")
    
    def get_save_string(self):
        return f"{self.center_x},{self.center_y},{self.radius}"
    
    @classmethod
    def from_load_string(cls, data):
        parts = data.split(',')
        center_x = int(parts[0])
        center_y = int(parts[1])
        radius = int(parts[2])
        return cls(center_x, center_y, radius)

# Честно говоря, я ничего не понял из условия задачи насчет эллипса, откуда там прямоугольник и зачем он вообще нужен?
# Зачем нам координаты его верхнего угла? Какие еще параллельные оси? Где параметры самого эллипса? Малая полуось? 
# Большая полуось? Координаты центра эллипса? Выходит все так, что нам нужно вывести только параметры этого прямоугольника:
# координаты верхнего (левого или правого не сказано) угла и размеры его сторон, которые параллельны осям координат.
# Кароче говоря создать тот же самый класс прямоугольник, только с названием эллипс. Ну раз сказано, будет сделано
class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def Show(self):
        print(f"Эллипс: Координаты верхнего угла: ({self.x}; {self.y}), ширина: {self.width}, высота: {self.height}")
    
    def get_save_string(self):
        return f"{self.x},{self.y},{self.width},{self.height}"
    
    @classmethod
    def from_load_string(cls, data):
        parts = data.split(',')
        x = int(parts[0])
        y = int(parts[1])
        width = int(parts[2])
        height = int(parts[3])
        return cls(x, y, width, height)

# Пример использования одного из производных классов    
# Создание объекта Square
# square = Square(0, 0, 5)

# Сохранение объекта в файл
# square.Save('square.txt')

# Загрузка объекта из файла
# loaded_square = Square.Load('square.txt')

# Вывод информации о загруженном объекте
# loaded_square.Show() 

# Теперь создадим список из фигур, как сказано в условии задачи
shapes = [
    Square(0, 0, 5),
    Rectangle(1, 1, 6, 4),
    Circle(0, 0, 3),
    Ellipse(2, 2, 8, 5)
]
# Создадим текстовый файл shapes.txt, куда запишем наши фигуры со всеми их атрибутами
with open('shapes.txt', 'w') as file:
    for shape in shapes:
        # Сначала записываем название класса с помощью дандер-метода __name__ и двоеточие :
        file.write(type(shape).__name__ + ': ')        
        # Затем записываем значения его атрибутов c помощью функции isinstance, которая принимает два параметра: объект 
        # класса и сам класс и возращает True если объект принадлежит этому классу и, в данном случае, выполняет действие.
        # Записываем каждый класс с аргументами в отдельную строку
        if isinstance(shape, Square):
            file.write(f'{shape.x},{shape.y},{shape.side}\n')
        elif isinstance(shape, Rectangle):
            file.write(f'{shape.x},{shape.y},{shape.width},{shape.height}\n')
        elif isinstance(shape, Circle):
            file.write(f'{shape.center_x},{shape.center_y},{shape.radius}\n')
        elif isinstance(shape, Ellipse):
            file.write(f'{shape.x},{shape.y},{shape.width},{shape.height}')

# Теперь создадим новый пустой список, куда будем загружать фигуры из файла shapes.txt
loaded_shapes = []
# Прочитаем этот файл
with open('shapes.txt', 'r') as file:
    # прочтенную информацию сохраняем в виде списка строк
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(':') # разделяем каждую строку по двоеточию, чтобы получить название класса и его аргументы
        shape_type = parts[0].strip()
        arguments = parts[1].strip()
        # Теперь создадим по экземпляру для каждого класса
        if shape_type == 'Square':
            # Создаем экземпляр Square, используя метод класса from_load_string, передав ему аргументы
            loaded_shapes.append(Square.from_load_string(arguments))
        elif shape_type == 'Rectangle':
            # Создаем экземпляр Rectangle, используя метод класса from_load_string, передав ему аргументы
            loaded_shapes.append(Rectangle.from_load_string(arguments))
        elif shape_type == 'Circle':
            # Создаем экземпляр Circle, используя метод класса from_load_string, передав ему аргументы
            loaded_shapes.append(Circle.from_load_string(arguments))
        elif shape_type == 'Ellipse':
            # Создаем экземпляр Ellipse, используя метод класса from_load_string, передав ему аргументы
            loaded_shapes.append(Ellipse.from_load_string(arguments))

# Выводим информацию о каждой загруженной фигуре
for shape in loaded_shapes:
    shape.Show()