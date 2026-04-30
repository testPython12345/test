'''
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @property
    @abstractmethod
    def name(self):
        pass

class Circle(Shape):
    def __init__(self, r, name):
        self.radius = r
        self._name = name
    def area(self):
        return 3.14 * self.radius ** 2
    @property
    def name(self):
        return self._name






class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return 3.14 * self.radius ** 2
    def perimetr(self):
        return self.a
    
krug = Circle(5)
print(krug.area())
primougolnik = Rectangle(5, 10)
a = Shape()
'''


from abc import ABC, abstractmethod

class Restaurant(ABC):
    @abstractmethod
    def calc_price_of_delivery(self):
        pass
    @abstractmethod
    def get_info(self):
        pass
    def __init__(self, name, distans, price):
        self._price = price
        self._name = name
        self._distans = distans
        self._delivary_price = self._distans * self._price
class Tanuki(Restaurant):
    def __init__(self, name, distans, price):
        super().__init__(name, distans, price)
    def calc_price_of_delivery(self):
        return self._delivary_price
    def get_info(self):
        return f'{self._name}: цена - {self._delivary_price}, расстояние - {self._distans}'